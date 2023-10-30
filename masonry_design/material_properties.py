import os
import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg


# Check the operating system
if os.name == 'posix':  # Unix/Linux/MacOS
    CMU_weights_file = "/Users/davidhansonc/Desktop/structural_python_tools/masonry_design/CMU_weights.xlsx"
elif os.name == 'nt':  # Windows
    CMU_weights_file = r"C:\Users\david\structural_python_tools\masonry_design\CMU_weights.xlsx"
else:
    raise OSError("Unsupported operating system.")


# Weights in PSF

LW_CMU = pd.read_excel(CMU_weights_file, sheet_name="LW CMU (PSF)", index_col=0)
MW_CMU = pd.read_excel(CMU_weights_file, sheet_name="MW CMU (PSF)", index_col=0)
NW_CMU = pd.read_excel(CMU_weights_file, sheet_name="NW CMU (PSF)", index_col=0)

eq_thicknesses = pd.read_excel(CMU_weights_file, sheet_name="Eq Thickness (in)", index_col=0)


# Elastic Modulus, E (ksi)
def elastic_modulus (fm=1500.0, material="cmu"):
    if material == "cmu":
        Em = 900 * fm / 1000
    elif material == "clay":
        Em = 700 * fm / 1000
    return Em

def aac_elastic_modulus (faac=290.0):
    Eaac = 6500 * faac**0.6 / 1000
    return Eaac

def grout_elastic_modulus (fg=2000.0):
    Eg = 500 * fg / 1000
    return Eg

# Modulus of Rigidity, G (ksi)
def shear_modulus (Em=1350.0):
    Gm = 0.4 * Em
    return Gm

def rupture_modulus(fm=1500.0, material="cmu"):
    pass