import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

import numpy as np
from IPython.display import display, Latex


def dowel_shear(Z_nominal, C_D=1.0, C_M=1.0, C_t=1.0, C_g=1.0, C_delta=1.0, C_eg=1.0, C_di=1.0, toe_nailing="N", print="N"):
    '''
    - NDS Table 11.3.1
    - All adjustment factors are 1.0 by default
    '''
    if toe_nailing == "Y":
        C_tn = 0.83   
    else:
        C_tn = 1.0 
    Z_factored = Z_nominal * C_D * C_M * C_t * C_g * C_delta * C_eg * C_di * C_tn
    if print == "Y":
        display(Latex("$Z'=Z C_D C_M C_t C_g C_{\\delta} C_{eg} C_{di}$"))
        display(Latex(f"$Z'= {Z_nominal} lbs * {C_D} * {C_M} * {C_t} * {round(C_g, 3)} * {C_delta} * {C_eg} * {C_di} * {C_tn} $"))
        display(Latex(f"$Z' = {round(Z_factored, 2)} lbs$"))
    return Z_factored


def dowel_withdrawal(W_nominal, penetration=1.0, C_D=1.0, C_M=1.0, C_t=1.0, C_eg=1.0, C_tn="N"):
    W = W_nominal * penetration
    if toe_nailing == "Y":
        C_tn = 0.67
    else:
        C_tn = 1.0
    W_factored = W_nominal * C_D * C_M**2 * C_t * C_eg * C_tn
    return W_factored

# alpha angle from pure shear in degrees
def combo_screw_shear_withdrawal(Z_factored, W_factored, penetration=1.0, alpha=0.0):
    Wp = W_factored * penetration
    alpha_rad = np.deg2rad(alpha)
    Z_alpha_factored = Wp * Z_factored / (Wp * np.cos(alpha_rad) + Z_factored * np.sin(alpha_rad))
    return Z_alpha_factored