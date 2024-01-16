import numpy as np

def LRFD(D=0, L=0, Lr=0, S=0, R=0, H=0, W=0, Ev=0, Eh=0, dir="P", H_cond="max"):
    H_factor = None
    if H_cond == "max":
        H_factor = 1.6
    elif H_cond == "min":
        H_factor = 0.9
    combos = [
        (1.4*D, "1.4D"),
        (1.2*D + 1.6*L + 0.5*max(Lr, S, R), "1.2D + 1.6L + 0.5 max(Lr, S, R)"),
        (1.2*D + 1.6*max(Lr, S, R) + max(L, 0.5*W), "1.2D + 1.6 max(Lr, S, R) + max(L, 0.5W)"),
        (1.2*D + 1.0*W + L + 0.5*max(Lr, S, R), "1.2D + 1.0W + L + 0.5 max(Lr, S, R)"),
        (0.9*D + 1.0*W, "0.9D + 1.0W"),
        (1.2*D + Ev + Eh + L + 0.2*S, "1.2D + Ev + Eh + L + 0.2S"),
        (0.9*D - Ev + Eh, "0.9D - Ev + Eh")
    ]
    ultimate_load = 0
    controlling_combo = ""
    if dir=="P":
        ultimate_load, controlling_combo = max(combos)
    elif dir=="N":
        ultimate_load, controlling_combo = min(combos)
    ultimate_load += H*H_factor
    print(f"The controlling combo is: {controlling_combo}")
    return ultimate_load

def ASD(D=0, L=0, Lr=0, S=0, R=0, H=0, W=0, Ev=0, Eh=0, dir="P", H_cond="max"):
    H_factor = None
    if H_cond == "max":
        H_factor = 1.0
    elif H_cond == "min":
        H_factor = 0.6
    combos = [
        (D, "D"),
        (D + L, "D + L"),
        (D + max(Lr, S, R), "D + max(Lr, S, R)"),
        (D + 0.75*L + 0.75*max(Lr, S, R), "D + 0.75L + 0.75 max(Lr, S, R)"),
        (D + 0.6*W, "D + 0.6W"),
        (D + 0.75*L + 0.75*(0.6*W) + 0.75*max(Lr, S, R), "D + 0.75L + 0.75(0.6W) + 0.75 max(Lr, S, R)"),
        (0.6*D + 0.6*W, "0.6D + 0.6W"),
        (D + 0.7*Ev + 0.7*Eh, "D + 0.7Ev + 0.7Eh"),
        (D + 0.525*Ev + 0.525*Eh + 0.75*L + 0.75*S, "D + 0.525Ev + 0.525Eh + 0.75L + 0.75S"),
        (0.6*D - 0.7*Ev + 0.7*Eh, "0.6D - 0.7Ev + 0.7Eh"),
    ]
    allowable_load = 0
    controlling_combo = ""
    if dir=="P":
        allowable_load, controlling_combo = max(combos)
    elif dir=="N":
        allowable_load, controlling_combo = min(combos)
    allowable_load += H*H_factor
    print(f"The controlling combo is: {controlling_combo}")
    return allowable_load