import numpy as np
from numpy import sqrt


def single_shear(D, l_m, l_s, F_yb, theta, dir_m, dir_s, G_m=0.5, G_s = 0.5):
    """
    D = dowel diameter
    F_yb = dowel bending yield strength, psi
    R_d = reduction term (Table 12.3.1B)
    R_e = F_em / F_es
    R_t = l_m / l_s
    l_m = main member dowel bearing length, in
    l_s = side member dowel bearing length, in
    theta = angle between the direction of the load and the direction of the grain (longitudinal axis of member)
    G_m = main member specific gravity
    G_s = side member specific gravity
    dir_m = main member bearing direction (parallel or perpendicular)
    dir_m = side member bearing direction (parallel or perpendicular)
    """
    if 
        F_em = 11200*G_m
        F_es = 11200*G_s
    R_e = F_em / F_es
    R_t = l_m / l_s

    k1 = k1_calc(R_e, R_t)
    k2 = k2_calc(D, l_m, R_e, F_yb, F_em)
    k3 = k3_calc(D, l_m, R_e, F_yb, F_em)

    yield_modes = {
        "Z_Im" : D * l_m * F_em / reduction_term(D, "Im", theta),
        "Z_Is" : D * l_s * F_es / reduction_term(D, "Is", theta),
        "Z_II" : k1 * D * l_s * F_es / reduction_term(D, "II", theta),
        "Z_IIIm" : k2 * D * l_m * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIm", theta)),
        "Z_IIIs" : k3 * D * l_s * F_em / ((1 + 2*R_e) * reduction_term(D, "IIIs", theta)),
        "Z_IV" : D**2 / reduction_term(D, "IV", theta) * sqrt((2 * F_em * F_yb) / (3*(1 + R_e))),
    }

    Z = yield_modes[min(yield_modes, key=yield_modes.get)]
    return Z


def double_shear(D, l_m, l_s, F_yb, theta, F_em, F_es):
    pass


def reduction_term(D, yield_mode, theta=90):
    K_theta = 1 + 0.25*(theta/90)

    R_d = 0
    if 0.25 <= D < 1:
        if yield_mode in ["Im", "Is"]:
            R_d = 4*K_theta
        elif yield_mode == "II":
            R_d = 3.6*K_theta
        else:
            R_d = 3.2*K_theta
    if D < 0.25:
        K_D = 0
        if D <= 0.17:
            K_D = 2.2
        elif 0.17 < D < 0.25:
            K_D = 10*D + 0.5
        R_d = K_D

    return R_d


def k1_calc(R_e, R_t):
    k1 = (sqrt(R_e + 2*R_e**2*(1 + R_t + R_t**2) + R_t**2*R_e**3) - R_e * (1 + R_t)) / (1 + R_e)
    return k1

def k2_calc(D, l_m, R_e, F_yb, F_em):
    k2 = -1 + sqrt(2*(1 + R_e) + (2*F_yb*(1 + 2*R_e)*D**2) / (3*F_em * l_m**2))
    return k2

def k3_calc(D, l_m, R_e, F_yb, F_em):
    k3 = -1 + sqrt(2*(1 + R_e)/R_e + (2*F_yb*(2 + R_e)*D**2) / (3*F_em * l_m**2))
    return k3