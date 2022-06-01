# linear interpolation
  
def interpolate(x_new, x=[0, 1], y=[0, 1]):
    y_new = (y[1] - y[0]) / (x[1] - x[0]) * (x_new - x[0]) + y[0]
    return y_new