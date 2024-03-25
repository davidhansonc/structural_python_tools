# Import Python Tools:
import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg
# import sectionproperties as shape
from WhatIfAnalysis import GoalSeek

from ASCE import load_combos
import sys
sys.path.append('/Users/davidhansonc/Desktop') #add desktop to PATH for development modules
from WLS.WindParameters import WindParameters #Wind Loads Module

from steel_design.AISC import aisc
steel_density = 0.2833 #pci