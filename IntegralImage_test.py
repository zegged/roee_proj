import IntegralImage as im

import numpy as np

def test_IntegralImage():
    # Test case 1: Small 3x3 matrix
    A = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
    
    print("A",A)
    expected = np.array([[ 1,  3,  6],
                         [ 5, 12, 21],
                         [12, 27, 45]])
    print("expected",expected)
    
    result = im.IntegralImage(A)

    assert np.array_equal(result, expected), f"Test failed! Expected:\n{expected}\nBut got:\n{result}"

    # Test case 2: 2x2 matrix
    A = np.array([[1, 2],
                  [3, 4]])
    expected = np.array([[1, 3],
                         [4, 10]])
    
    result = im.IntegralImage(A)
    assert np.array_equal(result, expected), f"Test failed! Expected:\n{expected}\nBut got:\n{result}"

    # Test case 3: 1x1 matrix
    A = np.array([[5]])
    expected = np.array([[5]])
    
    result = im.IntegralImage(A)
    assert np.array_equal(result, expected), f"Test failed! Expected:\n{expected}\nBut got:\n{result}"

    print("All tests passed!")

# Call the test function
test_IntegralImage()
