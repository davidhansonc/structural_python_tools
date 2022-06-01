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
    WW_index = wls_data.index[wls_data["Surface"] == "Overhang Top"][0] - 1
    WW = wls_data._get_value(WW_index, "Net w/ +GCpi (psf)")

    LW = wls_data.loc[wls_data["Surface"] == \
        "Leeward Wall", "Net w/ +GCpi (psf)"].values[0]

    R_index = wls_data.index[wls_data["Surface"] == "Roof"][0]
    R = wls_data.iloc[R_index:R_index + 4, 8].mean()

    wind_pressures = {
        "WW" : WW,
        "LW" : LW,
        "R"  : R
    }
    return wind_pressures


# Calculates the diaphragm demand from WLS data.
# requires roof length and eave height in feet and slope (x/12)
def diaphragm_calc(wind_pressures, eave_height, roof_length, roof_slope):
    wall_load = (wind_pressures["WW"] - wind_pressures["LW"]) * eave_height/2
    roof_lateral_load = wind_pressures["R"] * (roof_length / 2) \
            * roof_slope/np.sqrt(roof_slope**2 + 12**2)
    
    roof_diaphragm_load = wall_load + roof_lateral_load
    return roof_diaphragm_load