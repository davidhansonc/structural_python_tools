import pandas as pd
import numpy as np
import platform
import os

# Assuming structural_python_tools is in the user's home directory
home_directory = os.path.expanduser("~")
structural_python_tools_directory = os.path.join(home_directory, "structural_python_tools")
shapes_database_file = os.path.join(structural_python_tools_directory, "steel_design", "Aisc Shapes Database v15.0.xlsx")

aisc = pd.read_excel(shapes_database_file, sheet_name="Database v15.0", index_col=0)
aisc.replace("-", np.nan, inplace=True)

aisc_W = pd.read_excel(shapes_database_file, sheet_name="W", index_col=0)
aisc_W.replace("-", np.nan, inplace=True)

aisc_HSS = pd.read_excel(shapes_database_file, sheet_name="HSS", index_col=0)
aisc_HSS.replace("-", np.nan, inplace=True)

aisc_L = pd.read_excel(shapes_database_file, sheet_name="L", index_col=0)
aisc_L.replace("-", np.nan, inplace=True)