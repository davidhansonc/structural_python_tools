import numpy as np
import pandas as pd


def clean_data(wls_csv):
    wls_data = pd.read_csv(wls_csv)
    wls_data = wls_data.dropna(how="all")
    wls_data = wls_data.dropna(axis=1, how="all")
    wls_data.fillna("-", inplace=True)
    wls_data.index = range(len(wls_data.index))
    return wls_data


# Gets wind pressures from WLS data. 
# Parameter filepath string to CSV of WLS data
def get_pressures(wls_data):
    # Windward wall pressure
    WW_base_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0]
    WW_number = int(wls_data._get_value(WW_base_index, "#"))
    next_item_number = int(WW_number) + 1
    WW_index = wls_data.index[wls_data["#"] == str(next_item_number)][0] - 2
    WW = wls_data._get_value(WW_index, "Net w/ +GCpi (psf)")

    # Leeward Wall Pressure
    LW = wls_data.loc[wls_data["Surface"] == \
        "Leeward Wall", "Net w/ +GCpi (psf)"].values[0]

    # Windward Parapet Pressure
    WP_index = WW_index + 1
    WP = wls_data._get_value(WP_index, "Ext Pres (psf)")

    # Leeward Parapet Pressure
    LP_index = wls_data.index[wls_data["Surface"] == "Leeward Wall"][0] + 1
    LP = wls_data._get_value(LP_index, "Ext Pres (psf)")

    # Windward Roof Pressure
    WR = wls_data.loc[wls_data["Surface"] == \
        "Windward Roof", "Net w/ +GCpi (psf)"].values[0]

    # Leeward Roof Pressure
    LR = wls_data.loc[wls_data["Surface"] == \
        "Leeward Roof", "Net w/ +GCpi (psf)"].values[0]

    wind_pressures = {
        "WW" : WW,
        "LW" : LW,
        "WP" : WP,
        "LP" : LP,
        "WR" : WR,
        "LR" : LR
    }
    return wind_pressures


'''
# Gets building geometry from WLS data
# Parameter takes Pandas dataframe pluse slope and length values.
def get_geometry(wls_data):
    WW_base_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0]
    WW_number = int(wls_data._get_value(WW_base_index, "#"))
    next_item_number = int(WW_number) + 1
    WW_index = wls_data.index[wls_data["#"] == str(next_item_number)][0] - 2
    WP_index = WW_index + 1
    WR_index = wls_data.index[wls_data["Surface"] == "Windward Roof"][0]

    eave_height = wls_data._get_value(WW_index, "z (ft)")
    parapet_height = wls_data._get_value(WP_index, "z (ft)") - wls_data._get_value(WR_index, "z (ft)")

    geometry = [eave_height, parapet_height] 
    return geometry
    '''


def windward_load(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories=2):
    wall_load = pressures["WW"] * story_height
    parapet_load = pressures["WP"] * parapet
    roof_lateral_load = pressures["WR"] * mansard_slope/np.sqrt(mansard_slope**2 + 12**2) \
                                * mansard_slope/12*sloped_width

    windward_total = wall_load/2 + parapet_load + roof_lateral_load
    story_load = wall_load
    
    windward_loads = {
        "roof load" : windward_total,
        "story load" : story_load
    }
    return windward_loads


def leeward_load(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories=2):
    wall_load = pressures["LW"] * story_height
    parapet_load = pressures["LP"] * parapet
    roof_lateral_load = pressures["LR"] * mansard_slope/np.sqrt(mansard_slope**2 + 12**2) \
                                * mansard_slope/12*sloped_width

    leeward_total = wall_load/2 + parapet_load + roof_lateral_load
    story_load = wall_load

    leeward_loads = {
        "roof load" : leeward_total,
        "story load" : story_load
    }
    return leeward_loads


def total_diaphragm_load2(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories=2):
    WW = windward_load(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories)
    LW = leeward_load(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories)

    total_diaphragm = {
        "roof load" : WW["roof load"] - LW["roof load"],
        "story load" : WW["story load"] - LW["story load"]
    }
    return total_diaphragm


# Calculates the diaphragm demand from WLS data.
# requires roof length and eave height in feet and slope (x/12)
def total_diaphragm_load(pressures, story_height, parapet, eave, sloped_width, mansard_slope, stories=2):
    # roof load
    wall_load = (pressures["WW"] - pressures["LW"]) * story_height
    parapet_load = (pressures["WP"] - pressures["LP"]) * parapet
    roof_lateral_load = (pressures["WR"] - pressures["LR"]) \
        * mansard_slope/np.sqrt(mansard_slope**2 + 12**2) * mansard_slope/12*sloped_width
    print(roof_lateral_load)
    
    roof_load = wall_load/2 + parapet_load + roof_lateral_load

    # typical story load
    story_load = wall_load

    diaphragm_loads = {
        "roof load" : roof_load,
        "story load" : story_load
    }
    return diaphragm_loads