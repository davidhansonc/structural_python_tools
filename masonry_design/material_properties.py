import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg
import platform
import os

system = platform.system()

# Check the operating system
if system == 'Darwin':
    current_directory = "~/structural_python_tools"
    CMU_weights_file = current_directory + "/masonry_design/CMU_weights.xlsx"
elif system == 'Windows':
    current_directory = "C:\\structural_python_tools"
    CMU_weights_file = current_directory + "\\masonry_design\\CMU_weights.xlsx"
elif system == 'Linux':
    current_directory = "/structural_python_tools"
    CMU_weights_file = current_directory + "/masonry_design/CMU_weights.xlsx"
else:
    raise OSError("Unsupported operating system.")

# Weights in PSF
LW_CMU = pd.read_excel(CMU_weights_file, sheet_name="LW CMU (PSF)", index_col=0)
MW_CMU = pd.read_excel(CMU_weights_file, sheet_name="MW CMU (PSF)", index_col=0)
NW_CMU = pd.read_excel(CMU_weights_file, sheet_name="NW CMU (PSF)", index_col=0)

eq_thicknesses = pd.read_excel(CMU_weights_file, sheet_name="Eq Thickness (in)", index_col=0)

# Elastic Modulus, E (ksi)
def elastic_modulus(fm=1500.0, material="cmu"):
    if material == "cmu":
        Em = 900 * fm / 1000
    elif material == "clay":
        Em = 700 * fm / 1000
    return Em

def aac_elastic_modulus(faac=290.0):
    Eaac = 6500 * faac**0.6 / 1000
    return Eaac

def grout_elastic_modulus(fg=2000.0):
    Eg = 500 * fg / 1000
    return Eg

# Modulus of Rigidity, G (ksi)
def shear_modulus(Em=1350.0):
    Gm = 0.4 * Em
    return Gm

def rupture_modulus(fm=1500.0, material="cmu"):
    if material == "cmu":
        Gr = 0.33 * fm  # You need to define the rupture modulus calculation for CMU
    elif material == "clay":
        Gr = 0.25 * fm  # You need to define the rupture modulus calculation for clay
    else:
        Gr = 0.0  # Adjust this based on the behavior of other materials
    return Gr
