import pandas as pd
import numpy as np
import platform
import os

system = platform.system()
# current_directory = os.getcwd()

# Check the operating system
if system == 'Darwin':
    current_directory = "~/structural_python_tools"
    table_4a_file = current_directory + "/wood_design/sawn_lumber/ref_design_values/Table_4A.xlsx"
elif system == 'Windows':
    current_directory = "C:\\Users\\dhanson\\structural_python_tools"
    table_4a_file = current_directory + "\\wood_design\\sawn_lumber\\ref_design_values\\Table_4A.xlsx"
elif system == 'Linux':
    current_directory = "/structural_python_tools"
    table_4a_file = current_directory + "/wood_design/sawn_lumber/ref_design_values/Table_4A.xlsx"
else:
    raise OSError("Unsupported operating system.")


def table_4a_load(species, table_4a_data=table_4a_file):
    table_4a = pd.read_excel(table_4a_data, sheet_name=species, index_col=0)
    table_4a.replace("-", np.nan, inplace=True)
    return table_4a