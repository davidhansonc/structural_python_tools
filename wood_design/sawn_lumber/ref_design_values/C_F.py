import os
import pandas as pd
import numpy as np


if os.name == 'posix':  # Unix/Linux/MacOS
    C_F_file = "/Users/davidhansonc/Desktop/structural_python_tools\wood_design\sawn_lumber\ref_design_values\C_F_factors.xlsx"
elif os.name == 'nt':  # Windows
    C_F_file = r"C:Program Files\Desktop\Resources\structural_python_tools\wood_design\sawn_lumber\ref_design_values\C_F_factors.xlsx"
else:
    raise OSError("Unsupported operating system.")


def C_F_load(design_value_type, nominal_width, C_F_data=C_F_file):
    C_F_table = pd.read_excel(C_F_data, sheet_name=design_value_type, index_col=0)
    C_F_table.replace("-", np.nan, inplace=True)

    C_F = C_F_table.loc[nominal_width, design_value_type]
    return C_F