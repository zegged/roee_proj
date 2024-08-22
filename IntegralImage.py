import numpy as np

def IntegralImage(A):
    """
    This function calculates the integral image of 'A'.
    
    Parameters:
    A : 2D numpy array
        Input image
    
    Returns:
    I : 2D numpy array
        Integral image of A
    """
    N, M = A.shape
    I = np.zeros((N, M))
    
    # Calculate cumulative sum along rows
    z = np.cumsum(A, axis=1)
    
    # Calculate cumulative sum of z along columns
    I = np.cumsum(z, axis=0)
    
    return I