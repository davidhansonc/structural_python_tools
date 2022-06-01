import numpy as np
import pandas as pd


def clean_data(wls_csv):
    wls_data = pd.read_csv(wls_csv)
    wls_data = wls_data.dropna(how="all")
    wls_data = wls_data.dropna(axis=1, how="all")
    wls_data.fillna("-", inplace=True)
    return wls_data


# Gets wind pressures from WLS data. 
# Parameter filepath string to CSV of WLS data
def get_pressures(wls_data):
    WW = wls_data.loc[wls_data["Surface"] == \
        "Windward Wall", "Net w/ +GCpi (psf)"].values[0]
    LW = wls_data.loc[wls_data["Surface"] == \
        "Leeward Wall", "Net w/ +GCpi (psf)"].values[0]

    WP_index = wls_data.index[wls_data["Surface"] == "Windward Wall"][0] + 1
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
# Parameter takes Pandas dataframe pluse slope and length values.
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
def diaphragm_calc(wind_pressures, geometry):
    wall_load = (wind_pressures["WWP"] - wind_pressures["LWP"]) * geometry["eave height"]/2
    parapet_load = (wind_pressures["WPP"] - wind_pressures["LPP"]) * geometry["parapet height"]
    roof_lateral_load = wind_pressures["RP"] * geometry["roof length"] \
        * geometry["roof slope"]/np.sqrt(geometry["roof slope"]**2 + 12**2)
    
    roof_diaphragm_load = wall_load + parapet_load - roof_lateral_load
    return roof_diaphragm_load