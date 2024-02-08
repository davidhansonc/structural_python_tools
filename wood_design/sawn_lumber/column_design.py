import numpy as np

class Column:
    def __init__(self, Ep_min, le, d, Fc, CD, CM, Ct, CF, Ci):
        self.Ep_min = Ep_min
        self.le = le
        self.d = d
        self.Fc = Fc
        self.CD = CD
        self.CM = CM
        self.Ct = Ct
        self.CF = CF
        self.Ci = Ci
        self.c = 0.80

    def calculate_Cp(self):
        FcE = 0.822 * self.Ep_min / (self.le/self.d)**2
        Fc_st = self.Fc * self.CD * self.CM * self.Ct * self.CF * self.Ci
        Cp = 1 + (FcE/Fc_st)/(2*self.c) - np.sqrt((1 + (FcE/Fc_st)/(2*self.c))**2 - (FcE/Fc_st)/self.c)
        return Cp