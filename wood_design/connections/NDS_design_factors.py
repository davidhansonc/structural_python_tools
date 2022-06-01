import numpy as np


def group_factor(conn_type="ww", D=0.5, n=2, s=3, Em=1.6*10**6, Es=1.6*10**6, Am=1.5*5.5, As=1.5*5.5):
    '''
    - Calculation is valid for dowel type fasteners with a diameter <= 1/4"
    - conn_type = "ww" (wood-to-wood) or "wm" (wood-to-metal)
    - D = dowel diameter (in)
    - n = number of dowels in a line
    - s = dowel spacing on center (in)
    - Em = main member elastic modulus (psi) (default for DF #2)
    - Es = side member elastic modulus (psi) (default for DF #2)
    - Am = main member cross-sectional area (in^2) (default for 2x6)
    - As = side member cross-sectional area (in^2) (default for 2x6)
    '''
    gamma = 0
    try:
        if conn_type == "ww":
            gamma = 180000 * D**1.5
        elif conn_type == "wm":
            gamma = 270000 * D**1.5
    except:
        print('Invalid connection type. Try "ww" (wood-to-wood) or "wm" (wood-to-metal)"')
    u = 1 + gamma * s / 2 * (1 / (Em * Am) + 1 / (Es * As))
    m = u - np.sqrt(u**2 - 1)
    R_ea = min(Es * As / Em / Am, Em * Am / Es / As)

    C_g = (m / n * (1 - m**(2*n)) / ((1 + R_ea * m**n) * (1 + m) - 1 + m**(2*n))) \
        * ((1 + R_ea) / (1 - m))
    return C_g