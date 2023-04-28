import numpy as np
from numpy import sqrt
"""
D = dowel diameter
F_yb = dowel bending yield strength, psi
R_d = reduction term (Table 12.3.1B)
R_e = F_em / F_es
R_t = l_m / l_s
l_m = main member dowel bearing length, in
l_s = side member dowel bearing length, in
F_em = main member dowel bearing strength, psi (Table 12.3.3)
F_es = side member dowel bearing strength, psi (Table 12.3.3)
"""


def single_shear(D, l_m, l_s, F_yb, theta, F_em, F_es):
    R_e = F_em / F_es
    R_t = l_m / l_s
    R_d = None
    yield_modes = {
        "Z_Im" : D * l_m * F_em / reduction_term(D, "Im", theta),
        "Z_Is" : D * l_s * F_es / reduction_term(D, "Is", theta),
        "Z_II" : k1 * D * l_s * F_es / reduction_term(D, "II", theta),
        "Z_IIIm" : k2 * D * l_m * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIm", theta)),
        "Z_IIIs" : k3 * D * l_s * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIs", theta)),
        "Z_IV" : D**2 / reduction_term(D, "IV", theta) * sqrt((2 * F_em * F_yb) / (3*(1 + R_e))),
    }

    Z = min(yield_modes, key=yield_modes.get)
    return Z


def double_shear(D, l_m, l_s, F_yb, theta, F_em, F_es):
    R_e = F_em / F_es
    R_t = l_m / l_s
    R_d = None
    yield_modes = {
        "Z_Im" : D * l_m * F_em / reduction_term(D, "Im", theta),
        "Z_Is" : D * l_s * F_es / reduction_term(D, "Is", theta),
        "Z_II" : k1 * D * l_s * F_es / reduction_term(D, "II", theta),
        "Z_IIIm" : k2 * D * l_m * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIm", theta)),
        "Z_IIIs" : k3 * D * l_s * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIs", theta)),
        "Z_IV" : D**2 / reduction_term(D, "IV", theta) * sqrt((2 * F_em * F_yb) / (3*(1 + R_e))),
    }

    Z = min(yield_modes, key=yield_modes.get)
    return Z


def reduction_term(D, yield_mode, theta=90):
    K_theta = 1 + 0.25*(theta/90)

    R_d = None
    if 0.25 <= D < 1:
        if yield_mode in ["Im", "Is"]:
            R_d = 4*K_theta
        elif yield_mode == "II":
            R_d = 3.6*K_theta
        else:
            R_d = 3.2*K_theta
    if D < 0.25:
        K_D = None
        if D <= 0.17:
            K_D = 2.2
        elif 0.17 < D < 0.25:
            K_D = 10*D + 0.5
        R_d = K_D

    return R_d


def k1():
    k1 = (sqrt(R_e + 2*R_e**2*(1 + R_t + R_t**2) + R_t**2*R_e**3) - R_e * (1 + R_t)) / (1 + R_e)
    return k1

def k2():
    k2 = -1 + sqrt(2*(1 + R_e) + (2*F_yb*(1 + 2*R_e)*D**2) / (3*F_em * l_m**2))

def k3():
    k3 = -1 + sqrt(2*(1 + R_e)/R_e + (2*F_yb*(2 + R_e)*D**2) / (3*F_em * l_m**2))