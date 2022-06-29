from operator import index
import pandas as pd

aisc_shapes = pd.read_excel("./aisc-shapes-database-v15.0.xlsx", sheet_name="Database v15.0", index_col=0)