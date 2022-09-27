import math
import numpy as np

def  fit_2D_normal_distribution( data: np.array, factor: float ):
    """The function takes the data and performs a PCA analysis in order to 
        compute the main ellipse axes and sizes. The latter are proportional to 
        the standard deviations of the distribution. It also computes points
        that can be used to plot the ellips of size factor*sigma

    Args:
        data (np.array()): the factor with which the scale the ellipse. 
            For example to contain 95% of the data points, the factor should be 2.45.
        factor (float): the factor with which the scale the ellipse. 
            For example to contain 95% of the data points, the factor should be 2.45.

    Returns:
        sigma_max: the standard deviation in the largest direction
        sigma_min: the standard deviation in the smallest direction
        ellipse: a matrix of size (N,2) with X,Y coordinates of the ellipse
        e1: large axis of the ellipse [e1x e1y]
        e2: small axis of the ellipse [e2x e2y]
    """

    [N,c] = len(data)
    if (N < 2):
        print('Please specify at least 2 solutions in the data')
        return
    if (c != 2):
        print('Number of columns in data should be 2')
        return

    P = math.mean(data,0)
    # compute PCA, using SVD
    [_, S, V] = np.linalg.svd(data-np.ones(N,1)*P)
    # compute actual sigmas from singular values
    sigma_max = S[0,0]/math.sqrt((N-1))
    sigma_min = S[1,1]/math.sqrt((N-1))

    # Compute e1 e2
    e1 = [V[0,0], V[1,0]]
    e2 = [V[0,1], V[1,1]]

    # First compute ellipse with x and y axis as main axes
    theta = range(0, 0.01, 2 * math.pi)
    x = factor * sigma_max * math.cos(theta)
    y = factor * sigma_min * math.sin(theta)
    # Now rotate to angles in V and move to P
    angle = math.atan2(V[1,0], V[0,0])
    co = math.cos(angle)
    si = math.sin(angle)
    x1 = x * co - y * si + P[0]
    y1 = x * si + y * co + P[1]

    ellipse = [x1.T, y1.T]

    return (sigma_max, sigma_min, ellipse, e1, e2)