# Latex in Jupyter Notebook
from IPython.display import display, Math, Markdown, Latex
import numpy as np
import pandas as pd
display(Latex(r"\newpage")) #pagebreak
display(Latex(f'$x_{i}$')) #math display
display(Markdown('<img src="image.png" style="height: 300px;"/>'))

# Importing my own module
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)
import mymodule

import matplotlib as plt
%matplotlib inline

# import beam and supports
from indeterminatebeam import Beam, Support

# import loads (all load types imported for reference)
from indeterminatebeam import (
    PointTorque,
    PointLoad,
    PointLoadV,
    PointLoadH,
    UDL,
    UDLV,
    UDLH,
    TrapezoidalLoad,
    TrapezoidalLoadV,
    TrapezoidalLoadH,
    DistributedLoad,
    DistributedLoadV,
    DistributedLoadH
)


### EXAMPLE HEADER ###
# Import Python Tools:
import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg
import sectionproperties as shape

import ASCE.load_combos

from steel_design.AISC import aisc
steel_density = 0.2833 #pci

from concrete_design import material_properties as conc
from concrete_design.steel_reinforcement import rebar_df as rebar
conc_density = 150.0 #pcf

from masonry_design import material_properties as cmu
from masonry_design.material_properties import NW_CMU

from wood_design.ref_design_values.table_4a.table_4a import table_4a_load
table_4a = table_4a_load(species="DF")

conc_density = 150.0 #pcf
steel_density = 0.2833 #pci