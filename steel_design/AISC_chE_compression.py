import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import numpy as np


def E3(Ag, L, r, K=1.0, Fy=50.0, E=29000.0, type="LRFD"):
    '''
    - AISC chapter E3 flextural buckling of members without slender elements.
    - Units: kips, inches, ksi
    - type: "LRFD", "ASD", or "nominal"
    '''
    phi = 0.9
    omega = 1.67
    Fe = np.pi**2 * E / (K*L/r)**2
    if K*L/r <= 4.71*np.sqrt(E/Fy):
        Fcr = 0.658**(Fy/Fe) * Fy
    elif K*L/r > 4.71*np.sqrt(E/Fy):
        Fcr = 0.877 * Fe

    Pn = Fcr * Ag
    if type == "LRFD":
        return phi * Pn
    elif type == "ASD":
        return Pn / omega
    else:
        return Pn