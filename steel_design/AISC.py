import pandas as pd
import numpy as np
import platform

system = platform.system()

shapes_database_file = ""

if system == 'Darwin':
	shapes_database_file = "/Users/davidhansonc/Desktop/structural_python_tools/steel_design/aisc-shapes-database-v15.0.xlsx"
elif system == 'Windows':
	shapes_database_file = r"C:\Users\dhanson\Desktop\Resources\structural_python_tools\steel_design\aisc-shapes-database-v15.0.xlsx"
elif system == 'Linux':
	shapes_database_file = "/Users/davidhansonc/Desktop/structural_python_tools/steel_design/aisc-shapes-database-v15.0.xlsx"
else:
	print('Unknown')


aisc = pd.read_excel(shapes_database_file, sheet_name="Database v15.0", index_col=0)
aisc.replace("-", np.nan, inplace=True)