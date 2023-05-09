import pandas as pd
import numpy as np
from numpy import sqrt, pi, average, cos, sin, tan, arcsin, arccos, arctan, deg2rad, rad2deg


def elastic_modulus (fc=2500.0, wc=150.0): #Ec calc in psi
    Ec = wc**1.5 * 33 * sqrt(fc)
    return Ec


def rigidity_modulus (Ec=3031.25, nu=0.15):
    Gc = Ec/(2*(1+nu))
    return Gc


def rupture_modulus(fc=2500.0, lmbd=1.0):
    fr = 7.5 * lmbd * sqrt(fc)
    return fr


def cracked_moment_inertia(b, d, Ec, As, Es=29000000):
    n = Es / Ec
    rho = As / (b*d)
    cs = n*rho*d*(sqrt(1 + 2/(n*rho) - 1))
    
    Icr = b*cs**3/3 + n*As*(d-cs)**2
    return Icr