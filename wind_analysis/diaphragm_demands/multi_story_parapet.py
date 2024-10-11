import numpy as np
import pandas as pd


def clean_data(wls_csv):
    wls_data = pd.read_csv(wls_csv)
    wls_data = wls_data.dropna(how="all")
    wls_data = wls_data.dropna(axis=1, how="all")
    
    # Only fill NaN values in non-numeric columns
    non_numeric_cols = wls_data.select_dtypes(exclude=["number"]).columns
    wls_data[non_numeric_cols] = wls_data[non_numeric_cols].fillna("-")
    
    # Reset the index
    wls_data.index = range(len(wls_data.index))
    return wls_data


# Gets wind pressures from WLS data for a multistory building
def get_pressures_multistory(wls_data):
    pressures = {
        "windward_wall": [],
        "leeward_wall": [],
        "windward_parapet": None,
        "leeward_parapet": None,
        "roof": None,
    }

    # Extract pressures for each story's windward wall
    story_indices = wls_data.index[wls_data["Surface"] == "Windward Wall"]
    for index in story_indices:
        WW_number = int(wls_data._get_value(index, "#"))
        next_item_number = int(WW_number) + 1
        WW_index = wls_data.index[wls_data["#"] == str(next_item_number)][0] - 2
        WW_pressure = wls_data._get_value(WW_index, "Net w/ +GCpi (psf)")
        pressures["windward_wall"].append(WW_pressure)

    # Extract pressure for leeward wall (same for all stories)
    pressures["leeward_wall"] = wls_data.loc[
        wls_data["Surface"] == "Leeward Wall", "Net w/ +GCpi (psf)"
    ].values[0]

    # Windward parapet pressure (top of building)
    WP_index = story_indices[-1] + 1
    pressures["windward_parapet"] = wls_data._get_value(WP_index, "Ext Pres (psf)")

    # Leeward parapet pressure
    LP_index = wls_data.index[wls_data["Surface"] == "Leeward Wall"][0] + 1
    pressures["leeward_parapet"] = wls_data._get_value(LP_index, "Ext Pres (psf)")

    # Roof pressure
    pressures["roof"] = wls_data.loc[
        wls_data["Surface"] == "Roof", "Net w/ +GCpi (psf)"
    ].values[0]

    return pressures


# Gets building geometry from WLS data for multistory building
def get_geometry_multistory(wls_data, story_heights, roof_slope, roof_length):
    num_stories = len(story_heights)

    # Calculate total building height
    total_height = sum(story_heights)

    # Parapet height (from top story's windward wall)
    WP_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][-1] + 1
    parapet_height = int(wls_data._get_value(WP_index, "z (ft)")) - total_height

    geometry = {
        "story_heights": story_heights,
        "total_height": total_height,
        "parapet_height": parapet_height,
        "roof_length": roof_length,
        "roof_slope": roof_slope,
    }
    return geometry


# Calculates the diaphragm demand from WLS data for a multistory building
def diaphragm_calc_multistory(pressures, geometry):
    story_heights = geometry["story_heights"]
    total_height = geometry["total_height"]
    parapet_height = geometry["parapet_height"]
    roof_length = geometry["roof_length"]
    roof_slope = geometry["roof_slope"]

    # Calculate wall loads for each story
    wall_load = 0
    for i, height in enumerate(story_heights):
        WW_pressure = pressures["windward_wall"][i]
        story_load = (WW_pressure - pressures["leeward_wall"]) * height / 2
        wall_load += story_load

    # Parapet load (top story only)
    parapet_load = (pressures["windward_parapet"] - pressures["leeward_parapet"]) * parapet_height

    # Roof lateral load
    roof_lateral_load = (
        pressures["roof"]
        * roof_length
        * roof_slope
        / np.sqrt(roof_slope**2 + 12**2)
    )

    # Total diaphragm load
    roof_diaphragm_load = wall_load + parapet_load - roof_lateral_load
    return roof_diaphragm_load
