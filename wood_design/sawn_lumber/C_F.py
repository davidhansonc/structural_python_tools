import pandas as pd
import numpy as np

C_F_file = r"C:\Users\dhanson\Desktop\Resources\python_resources\wood_design\sawn_lumber\C_F_factors.xlsx"

def C_F_load(design_value, width, thick=None, C_F_data=C_F_file):
    C_F_table = pd.read_excel(C_F_data, sheet_name=design_value, index_col=0)
    C_F_table.replace("-", np.nan, inplace=True)

    C_F = C_F_table.loc[width, design_value]
    return C_F