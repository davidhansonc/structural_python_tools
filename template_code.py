# Import Python Tools:
import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg
# import sectionproperties as shape
# from WhatIfAnalysis import GoalSeek

from ASCE import load_combos

from steel_design.AISC import aisc_W, aisc_HSS, aisc_L

from concrete_design import material_properties as conc
from concrete_design.steel_reinforcement import rebar_df as rebar

from masonry_design import material_properties as cmu
from masonry_design.material_properties import NW_CMU #psf

Fy = 50 #ksi
E = 29000 #ksi
γ_stl = 0.2833 #pci

fc = 2500 #psi
fy = 60000 #psi
conc_density = 150 #pcf

def cmu():
    print(f"CMU weights (psf):\n {NW_CMU}\n")

def rebar_info():
    print(f"ACI rebar info:\n {rebar}")