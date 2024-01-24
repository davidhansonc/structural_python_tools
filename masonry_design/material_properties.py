import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg
import platform
import os

# Get the home directory
home_directory = os.path.expanduser("~")

# Define the directory name for structural_python_tools
structural_python_tools_dirname = "structural_python_tools"

# Construct the path to structural_python_tools based on the operating system
if platform.system() == 'Darwin' or platform.system() == 'Linux':
    structural_python_tools_directory = os.path.join(home_directory, structural_python_tools_dirname)
elif platform.system() == 'Windows':
    structural_python_tools_directory = os.path.join(os.environ['USERPROFILE'], structural_python_tools_dirname)
else:
    raise OSError("Unsupported operating system.")

# Construct the path to CMU_weights.xlsx within structural_python_tools
CMU_weights_file = os.path.join(structural_python_tools_directory, "masonry_design", "CMU_weights.xlsx")

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
