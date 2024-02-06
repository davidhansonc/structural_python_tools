import numpy as np

def group_factor(conn_type, D, n, s, Am, As, Em=1.6*10**6, Es="default"):
    '''
    Calculates the Group Action Factor (C_g) for dowel type fasteners with a diameter <= 1/4".

    Parameters:
    - conn_type (str): "ww" (wood-to-wood) or "wm" (wood-to-metal)
    - D (float): Dowel diameter (in)
    - n (int): Number of dowels in a line
    - s (float): Dowel spacing on center (in)
    - Am (float): Main member cross-sectional area (in^2)
    - As (float): Side member cross-sectional area (in^2)
    - Em (float): Main member elastic modulus (psi), default for DF #2
    - Es (float or str): Side member elastic modulus (psi), default for DF #2 or for steel

    Returns:
    - float: The Group Action Factor (C_g).
    '''
    if D <= 0.25:
        C_g = 1.0
        print("C_g = 1.0 for D <= 0.25 inches")
        return C_g

    gamma = 0
    try:
        if conn_type == "ww":
            gamma = 180000 * D**1.5
            if Es == "default":
                Es = 1.6*10**6
        elif conn_type == "wm":
            gamma = 270000 * D**1.5
            if Es == "default":
                Es = 29000000
    except:
        print('Invalid connection type. Try "ww" (wood-to-wood) or "wm" (wood-to-metal)"')
        return None

    u = 1 + gamma * s / 2 * (1 / (Em * Am) + 1 / (Es * As))
    m = u - np.sqrt(u**2 - 1)
    R_ea = min(Es * As / Em / Am, Em * Am / Es / As)

    C_g = (m / n * (1 - m**(2*n)) / ((1 + R_ea * m**n) * (1 + m) - 1 + m**(2*n))) * ((1 + R_ea) / (1 - m))
    
    # Print the formula used for calculation
    print(f"C_g Formula used: C_g = (m / n * (1 - m^(2*n)) / ((1 + R_ea * m^n) * (1 + m) - 1 + m^(2*n))) * ((1 + R_ea) / (1 - m))")
    print(f"Where m = {round(m, 3)}, R_ea = {round(R_ea, 3)}, n = {n}, and gamma = {round(gamma, 1)}")
    
    return C_g