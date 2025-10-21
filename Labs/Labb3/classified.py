import numpy as np
def classified(x, y, k, m):
    x = np.array(x)
    y = np.array(y)
    above_idx= np.where(y > k*x+m)[0]
    below_idx = np.where(y <= k*x+m)[0]
    x_above = x[above_idx]
    y_above = y[above_idx]
    x_below = x[below_idx]
    y_below = y[below_idx]
    return  x_above, y_above, x_below, y_below,above_idx,below_idx