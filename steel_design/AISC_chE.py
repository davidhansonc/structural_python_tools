import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import numpy as np
    

def E3_Fe (K, L, r, E):
    # Elastic buckling stress
    Fe = np.pi**2 * E / (K*L/r)**2
    return Fe


def E3_Fcr (K, L, r, E, Fy, Fe):
    # Critical stress
    if K*L/r <= 4.71*np.sqrt(E/Fy) or Fy/Fe <= 2.25:
        Fcr = 0.658**(Fy/Fe) * Fy
    elif K*L/r > 4.71*np.sqrt(E/Fy) or Fy/Fe > 2.25:
        Fcr = 0.877 * Fe
    
    return Fcr


def E3 (Ag, L, r, K=1.0, Fy=50, E=29000):
    '''
    - AISC section E3 flexural buckling of members without slender elements.
    - Units: kips, inches, ksi
    - type: "LRFD", "ASD", or "nominal"
    '''
    # Elastic buckling stress
    Fe = E3_Fe(K, L, r, E)

    # Critical Stress
    Fcr = E3_Fcr(K, L, r, E, Fy, Fe)

    # Nominal compressive strength (kips)
    Pn = Fcr * Ag
    return Pn


def E4 (symmetry, Ag, L, r, K=1.0, Fy=50, E=29000, type="Nom"):
    '''
    - AISC section E3 flexural buckling of members without slender elements.
    - Units: kips, inches, ksi
    - type: "LRFD", "ASD", or "nominal"
    '''

    # Elastic buckling stress
    if symmetry == "singly":
        Fe = (Fey + Fez)/(2*H) * (1 - sqrt(1 - (4*Fey*Fez*H)/(Fey + Fez)**2))
    
    # Critical stress
    if K*L/r <= 4.71*np.sqrt(E/Fy):
        Fcr = 0.658**(Fy/Fe) * Fy
    elif K*L/r > 4.71*np.sqrt(E/Fy):
        Fcr = 0.877 * Fe

    # Nominal compressive strength (kips)
    Pn = Fcr * Ag

    # Factoring
    phi = 0.9
    omega = 1.67
    if type == "LRFD":
        return phi * Pn
    elif type == "ASD":
        return Pn / omega
    elif type == "Nom":
        return Pn


def E7 (Ag, L, r, K=1.0, Fy=36, E=29000, round_HSS="No", type="Nom"):
    '''
    - AISC section E7 flexural buckling of members with slender elements.
    - Units: kips, inches, ksi
    - type: "LRFD", "ASD", or "nominal"
    - lamda = width-to-thickness ratio as defined in Section B4.1
    - lamda_r = limiting width-to-thickness ratio as defined in Table B4.1a
    '''
    phi = 0.9
    Pn = Fcr * Ae
    return Pn