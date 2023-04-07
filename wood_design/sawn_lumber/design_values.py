# Import Python Tools:
import pandas as pd
import numpy as np
import wood_design.sawn_lumber.C_F as size_factor

def bending():
    pass


def tension(Ft, nom_width, C_D=0.9, C_M=1.0, C_t=1.0, C_i=1.0, design_ref_table="4A"):
    C_F = size_factor.C_F_load("Ft", width=nom_width)
    Ft_pr = Ft * C_D * C_M * C_t * C_F * C_i
    return Ft_pr


def shear():
    pass


def compression():
    pass


def compr_perp():
    pass


def elastic_modulus():
    pass


def elastic_modulus_min():
    pass