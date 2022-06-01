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
from IPython.display import display, Math, Markdown, Latex
import numpy as np
import pandas as pd

import os, sys

p1 = os.path.abspath('.')
sys.path.insert(1, p1)

import design_load_summary as dls
import steel_reinforcement as rebar
display(Latex(r"\newpage")) #pagebreak