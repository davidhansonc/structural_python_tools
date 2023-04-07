import numpy as np


# For fasteners with D <= 1"
def group_factor(conn_type, D, n, s, Am, As, Em=1.6*10**6, Es="default`"):
    '''
    - Calculation is valid for dowel type fasteners with a diameter <= 1/4"
    - conn_type = "ww" (wood-to-wood) or "wm" (wood-to-metal)
    - D = dowel diameter (in)
    - n = number of dowels in a line
    - s = dowel spacing on center (in)
    - Em = main member elastic modulus (psi) (default for DF #2)
    - Es = side member elastic modulus (psi) (default for DF #2 or for steel)
    - Am = main member cross-sectional area (in^2) (default for 2x6)
    - As = side member cross-sectional area (in^2) (default for 2x6)
    '''
    if D < 0.25:
        C_g = 1.0
        return C_g

    gamma = 0
    try:
        if conn_type == "ww":
            gamma = 180000 * D**1.5
            if Es == "default":
                Es = 1.6*10**6
        elif conn_type == "wm":
            gamma = 270000 * D**1.5
            Es = 29000000
    except:
        print('Invalid connection type. Try "ww" (wood-to-wood) or "wm" (wood-to-metal)"')
    u = 1 + gamma * s / 2 * (1 / (Em * Am) + 1 / (Es * As))
    m = u - np.sqrt(u**2 - 1)
    R_ea = min(Es * As / Em / Am, Em * Am / Es / As)

    C_g = (m / n * (1 - m**(2*n)) / ((1 + R_ea * m**n) * (1 + m) - 1 + m**(2*n))) \
        * ((1 + R_ea) / (1 - m))
    return C_g