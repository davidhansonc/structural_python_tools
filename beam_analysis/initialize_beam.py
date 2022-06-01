import indeterminatebeam as b


def initialize_beam_lbs(beam_object):
    beam_object.update_units(key='length', unit='ft')
    beam_object.update_units('force', 'lbf')
    beam_object.update_units('distributed', 'lbf/ft')
    beam_object.update_units('moment', 'lbf.ft')
    beam_object.update_units('E', 'kip/in2')
    beam_object.update_units('I', 'in4')
    beam_object.update_units('deflection', 'in')
    return beam_object


def initialize_beam_kips(beam_object):
    beam_object.update_units(key='length', unit='ft')
    beam_object.update_units('force', 'kip')
    beam_object.update_units('distributed', 'kip/ft')
    beam_object.update_units('moment', 'kip.ft')
    beam_object.update_units('E', 'kip/in2')
    beam_object.update_units('I', 'in4')
    beam_object.update_units('deflection', 'in')
    return beam_object