import numpy as np
# import beam and supports
from indeterminatebeam import Beam, Support

# import loads (all load types imported for reference)
from indeterminatebeam import (
    PointTorque,
    PointLoad,
    PointLoadV,
    PointLoadH,
    UDL,
    UDLV,
    UDLH,
    TrapezoidalLoad,
    TrapezoidalLoadV,
    TrapezoidalLoadH,
    DistributedLoad,
    DistributedLoadV,
    DistributedLoadH
)

class shear_wall_footing():

    def __init__(self, h=10.0, L=12.0, L_w=10.0, D=12.0):
        self.L = L
        self.L_1 = (L - L_w) / 2
        self.L_w = L_w
        self.D = D
        beam_SI = Beam(self.L)
        self.beam = self.update_beam_units(beam_SI)
        
    
    def update_beam_units(self, beam):
        beam.update_units(key='length', unit='ft')
        beam.update_units('force', 'lbf')
        beam.update_units('distributed', 'lbf/ft')
        beam.update_units('moment', 'lbf.ft')
        beam.update_units('E', 'kip/in2')
        beam.update_units('I', 'in4')
        beam.update_units('deflection', 'in')
        return beam


    def moment_overturning(self):
        M_o = (h + D) + M
        return M_o


    def moment_resisting(self):
        M_R = P_rDL * (L_1 + a) + P_f * (L / 2) + P_w * (L_1 + L_w / 2)
        return M_R

    
    def soil_capacity(self):
        pass


    def concrete_capacity(self):
        pass