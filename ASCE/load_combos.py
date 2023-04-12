from errno import EHOSTDOWN
from re import L, S
from this import d
from tkinter import W
import numpy as np

def LRFD(D=0, L=0, Lr=0, S=0, R=0, W=0, Ev=0, Eh=0, dir="P"):
    combos = [
        1.4*D,
        1.2*D + 1.6*L + 0.5*max(Lr, S, R),
        1.2*D + 1.6*max(Lr, S, R) + max(L, 0.5*W),
        1.2*D + 1.0*W + L + 0.5*max(Lr, S, R),
        0.9*D + 1.0*W,
        1.2*D + Ev + Eh + L + 0.2*S,
        0.9*D - Ev + Eh
    ]
    ultimate_load = 0
    if dir=="P":
        ultimate_load = max(combos)
    elif dir=="N":
        ultimate_load = min(combos)
    return ultimate_load

def ASD(D=0, L=0, Lr=0, S=0, R=0, W=0, Ev=0, Eh=0, dir="P"):
    combos = [
        D,
        D + L,
        D + max(Lr, S, R),
        D + 0.75*L + 0.75*max(Lr, S, R),
        D + 0.6*W,
        D + 0.75*L + 0.75*(0.6*W) + 0.75*max(Lr, S, R),
        0.6*D + 0.6*W,
        D + 0.7*Ev + 0.7*Eh,
        D + 0.525*Ev + 0.525*Eh + 0.75*L + 0.75*S,
        0.6*D - 0.7*Ev + 0.7*Eh,
    ]
    allowable_load = 0
    if dir=="P":
        allowable_load = max(combos)
    elif dir=="N":
        allowable_load = min(combos)
    return allowable_load