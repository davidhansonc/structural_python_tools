import pandas as pd

shapes_database_file = r"C:\Users\dhanson\Desktop\Resources\python_resources\steel_design\aisc-shapes-database-v15.0.xlsx"

aisc = pd.read_excel(shapes_database_file, sheet_name="Database v15.0", index_col=0)