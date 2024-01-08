import pandas as pd
import numpy as np
import platform
# import os

system = platform.system()
# current_directory = os.getcwd()

if system == 'Darwin':
    current_directory = "~/structural_python_tools"
    shapes_database_file = current_directory + "/steel_design/aisc-shapes-database-v15.0.xlsx"
elif system == 'Windows':
    current_directory = "C:\\structural_python_tools"
    shapes_database_file = current_directory + "\\steel_design\\aisc-shapes-database-v15.0.xlsx"
elif system == 'Linux':
    current_directory = "/structural_python_tools"
    shapes_database_file = current_directory + "/steel_design/aisc-shapes-database-v15.0.xlsx"
else:
    raise OSError("Unsupported operating system.")


aisc = pd.read_excel(shapes_database_file, sheet_name="Database v15.0", index_col=0)
aisc.replace("-", np.nan, inplace=True)