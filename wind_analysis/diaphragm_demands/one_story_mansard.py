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


# Gets building geometry from WLS data
# Parameter takes Pandas dataframe pluse slope and length values.
def get_geometry(wls_data):
    WW_base_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0]
    WW_number = int(wls_data._get_value(WW_base_index, "#"))
    next_item_number = int(WW_number) + 1
    WW_index = wls_data.index[wls_data["#"] == str(next_item_number)][0] - 2
    WP_index = WW_index + 1

    eave_height = wls_data._get_value(WW_index, "z (ft)")
    parapet_height = wls_data._get_value(WP_index, "z (ft)") - eave_height

    geometry = [eave_height, parapet_height] 
    return geometry


# Calculates the diaphragm demand from WLS data.
# requires roof length and eave height in feet and slope (x/12)
def diaphragm_calc(wind_pressures, geometry, roof_length, roof_slope):
    eave_height = geometry[0]
    parapet_height = geometry[1]

    wall_load = (wind_pressures["WW"] - wind_pressures["LW"]) * eave_height/2
    parapet_load = (wind_pressures["WP"] - wind_pressures["LP"]) * parapet_height
    roof_lateral_load = (wind_pressures["WR"] - wind_pressures["LR"]) \
        * (roof_length / 2) * roof_slope/np.sqrt(roof_slope**2 + 12**2)
    
    roof_diaphragm_load = wall_load + parapet_load + roof_lateral_load
    return roof_diaphragm_load