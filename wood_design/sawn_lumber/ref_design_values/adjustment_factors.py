class SawnLumberAdjustmentFactors:
	def __init__(self):
		self.C_D = 1.0
		self.C_M = 1.0
		self.C_t = 1.0
		self.C_L = 1.0
		self.C_F = 1.0
		self.C_fu = 1.0
		self.C_i = 1.0
		self.C_r = 1.0
		self.C_P = 1.0
		self.C_T = 1.0
		self.C_b = 1.0


	def calculate_Cp(self):
		r = self.d / sqrt(12)
		FcE = pi**2 * self.Ep_min / (self.le/r)**2
		Fc_st = self.Fc * self.CD * self.CM * self.Ct * self.CF * self.Ci
		Cp = 1 + (FcE/Fc_st)/(2*self.c) - np.sqrt((1 + (FcE/Fc_st)/(2*self.c))**2 - (FcE/Fc_st)/self.c)
		return Cp