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

import load_combos
from steel_design.AISC import aisc
from concrete_design.material_properties import elastic_modulus, rigidity_modulus
from concrete_design.steel_reinforcement import rebar_df as rebar
from masonry_design.material_properties import NW_CMU, cmu_elastic_modulus
conc_density = 150.0 #pcf
steel_density = 0.2833 #pci