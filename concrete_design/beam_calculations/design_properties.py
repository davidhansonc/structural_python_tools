import numpy as np


def beta_1_calc(fc):
    if fc <= 4000:
        beta_1 = 0.85
    elif fc > 4000 and fc < 8000:
        beta_1 = 0.85 - 0.05*(fc-4000)/1000
    elif fc >= 8000:
        beta_1 = 0.65
    return beta_1


def compression_block(As, fy, Es, b, fc, Apr_s=0, dpr=0, eps_cu=0.003):
    beta_1 = beta_1_calc(fc)

    n1 = 0.85*fc*beta_1*b
    n2 = Es*eps_cu*Apr_s - As*fy
    n3 = -Es*eps_cu*Apr_s*dpr

    c = (-n2 + np.sqrt(n2**2 - 4*n1*n3)) / (2*n1)
    return c


def equiv_compr_block(c):
    a = 0.85 * c
    return a


def compr_steel_strain(c, eps_t, d_t):
    eps_cs = eps_t*c / (d_t - c)
    return eps_cs


def tension_steel_strain(d_t, c):
    eps_cu = 0.003

    eps_t = eps_cu * (d_t - c)/c
    return eps_t


def phi_factor(eps_t, fy=60000, Es=29000000):
    eps_ty = fy / Es
    if eps_t >= eps_ty + 0.003:
        phi_b = 0.9
    elif eps_t <= eps_ty:
        phi_b = 0.65
    else:
        phi_b = 0.65 + 0.25 * (eps_t - eps_ty) / 0.003

    return phi_b