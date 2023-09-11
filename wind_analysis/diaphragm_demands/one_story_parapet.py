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
    WW_base_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0]
    WW_number = int(wls_data._get_value(WW_base_index, "#"))
    next_item_number = int(WW_number) + 1
    WW_index = wls_data.index[wls_data["#"] == str(next_item_number)][0] - 2
    WW = wls_data._get_value(WW_index, "Net w/ +GCpi (psf)")
    print(WW)

    LW = wls_data.loc[wls_data["Surface"] == \
        "Leeward Wall", "Net w/ +GCpi (psf)"].values[0]

    # Windward Parapet Pressure
    WP_index = WW_index + 1
    WP = wls_data._get_value(WP_index, "Ext Pres (psf)")

    LP_index = wls_data.index[wls_data["Surface"] == "Leeward Wall"][0] + 1
    LP = wls_data._get_value(LP_index, "Ext Pres (psf)")

    R = wls_data.loc[wls_data["Surface"] == \
        "Roof", "Net w/ +GCpi (psf)"].values[0]

    wind_pressures = {
        "WW" : WW,
        "LW" : LW,
        "WP" : WP,
        "LP" : LP,
        "R"  : R
    }
    return wind_pressures


# Gets building geometry from WLS data
# Parameter takes Pandas dataframe plus slope and length values.
def get_geometry(wls_data, roof_slope, roof_length):
    eave_height = int(wls_data.loc[wls_data["Surface"] == \
        "Windward Wall", "z (ft)"].values[0])

    WP_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0] + 1
    parapet_height = int(wls_data._get_value(WP_index, "z (ft)")) - eave_height

    geometry = {
        "eave height" : eave_height,
        "parapet height" : parapet_height,        
        "roof length" : roof_length,
        "roof slope" : roof_slope,
    }
    return geometry


# Calculates the diaphragm demand from WLS data.
def diaphragm_calc(wind_pressures, eave_height, parapet_height, roof_length=0, roof_slope=0):
    wall_load = (wind_pressures["WW"] - wind_pressures["LW"]) * eave_height/2
    parapet_load = (wind_pressures["WP"] - wind_pressures["LP"]) * parapet_height
    roof_lateral_load = wind_pressures["R"] * roof_length \
        * roof_slope/np.sqrt(roof_slope**2 + 12**2)
    
    roof_diaphragm_load = wall_load + parapet_load - roof_lateral_load
    return roof_diaphragm_load