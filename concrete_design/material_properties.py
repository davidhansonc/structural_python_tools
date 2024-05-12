import pandas as pd
import numpy as np
from numpy import sqrt


def elastic_modulus (fc=2500.0, wc=145.0): #Ec calc in psi
    Ec = wc**1.5 * 33 * sqrt(fc)
    return Ec


def rigidity_modulus (Ec=elastic_modulus(), nu=0.15):
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