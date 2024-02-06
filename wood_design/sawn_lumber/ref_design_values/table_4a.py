import pandas as pd
import numpy as np
import os

# Get the home directory
home_directory = os.path.expanduser("~")
# Construct the path to structural_python_tools
structural_python_tools_directory = os.path.join(home_directory, "structural_python_tools")
# Construct the path to Table_4A.xlsx within structural_python_tools
table_4a_file = os.path.join(structural_python_tools_directory, "wood_design", "sawn_lumber", "ref_design_values", "Table_4A.xlsx")

def table_4a_load(species, table_4a_data=table_4a_file):
    table_4a = pd.read_excel(table_4a_data, sheet_name=species, index_col=0)
    table_4a.replace("-", np.nan, inplace=True)
    return table_4a