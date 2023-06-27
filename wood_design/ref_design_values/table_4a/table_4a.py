import os
import pandas as pd
import numpy as np


if os.name == 'posix':  # Unix/Linux/MacOS
    table_4a_file = "/Users/davidhansonc/Desktop/structural_python_tools/wood_design/ref_design_values/table_4a/Table_4A.xlsx"
elif os.name == 'nt':  # Windows
    table_4a_file = r"C:\Users\dhanson\Desktop\Resources\structural_python_tools\wood_design\ref_design_values\table_4a\Table_4A.xlsx"
else:
    raise OSError("Unsupported operating system.")


def table_4a_load(species, table_4a_data=table_4a_file):
    table_4a = pd.read_excel(table_4a_data, sheet_name=species, index_col=0)
    table_4a.replace("-", np.nan, inplace=True)
    return table_4a