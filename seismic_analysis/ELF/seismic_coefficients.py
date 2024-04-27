import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg


def shear_wave_velocity(site_class):
    Vs_30 = 2500 #ft/sec
    if site_class == "B":
        Vs_30 = 2295
    elif site_class == "C":
        Vs_30 = 1604
    elif site_class == "D" or site_class == "Default":
        Vs_30 = 873
    elif site_class == "E":
        Vs_30 = 509 #check this
    return Vs_30


def short_period_site_coefficient(V_s30, S_s):
    V_s30_SI = V_s30 * 0.3048 #m/s
    F_a = np.exp(-0.727 * np.log(V_s30_SI/760) \
        - 0.2298 * (np.exp(-0.00638 * (min(V_s30_SI, 760) - 360)) \
        - np.exp(-0.00638 * 400)) \
        * np.log(((S_s/2.3) + 0.1) / 0.1) )

    return F_a 


def long_period_site_coefficient (V_s30, S_1):
    V_s30_SI = V_s30 * 0.3048 #m/s
    F_v = np.exp(-1.03 * np.log(V_s30_SI/760) \
        - 0.118 * (np.exp(-0.00756 * (min(V_s30_SI, 760) - 360)) \
        - np.exp(-0.00756 * 400)) \
        * np.log(((S_1/0.7) + 0.1) / 0.1) )
    
    return F_v


def Ta_calc (hn, Ct=0.02, x=0.75):
    Ta = Ct*hn**x

    return Ta


def Cs_calc (Sd1, Sds, R, T, T_L, Ie=1.0):
    Cs_calc = Sds / (R/Ie)

    if T <= T_L:
        Cs_update = min(Cs_calc, Sd1 / (T*R/Ie))
    elif T > T_L:
        Cs_update = min(Cs_calc, Sd1 / (T**2*R/Ie))
    
    Cs = max(0.044 * Sds * Ie, Cs_update)

    return Cs