# Import Python Tools:
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg


def Ta (hn, Ct=0.02, x=0.75):
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