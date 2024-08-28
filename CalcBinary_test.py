import CalcBinary as CB
import numpy as np

def test_calc_binary_4x4():
    print("in 1")
    # Test input (4x4 matrix)
    img = np.array([[0.1, 0.3, 0.2, 0.4],
                    [0.5, 0.8, 0.7, 0.6],
                    [0.4, 0.3, 0.9, 0.7],
                    [0.8, 0.5, 0.6, 0.2]])
    
    # Expected output (manually computed or from MATLAB)
    expected_output = np.array([[0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
    
    # Run the function
    output = CB.CalcBinary(img)
    
    # Check if the output matches the expected output
    assert np.allclose(output, expected_output), "Test failed for 4x4 matrix!"
    print("Test passed for 4x4 matrix!")

def test_calc_binary_5x5():
    # Test input (5x5 matrix)
    img = np.array([[0.1, 0.3, 0.2, 0.4, 0.7],
                    [0.5, 0.8, 0.7, 0.6, 0.9],
                    [0.4, 0.3, 0.9, 0.7, 0.5],
                    [0.8, 0.5, 0.6, 0.2, 0.1],
                    [0.6, 0.7, 0.8, 0.9, 0.4]])
    
    # Expected output (manually computed or from MATLAB)
    expected_output = np.array([[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]])
    
    # Run the function
    output = CB.CalcBinary(img)
    
    # Check if the output matches the expected output
    assert np.allclose(output, expected_output), "Test failed for 5x5 matrix!"
    print("Test passed for 5x5 matrix!")



def test_calc_binary2():
    print("in 2")

    # Test input
    img = np.array([[0.1, 0.3, 0.2],
                    [0.4, 0.8, 0.5],
                    [0.7, 0.6, 0.9]])
    
    # Expected output (manually computed or from MATLAB)
    expected_output = np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
    
    # Run the function
    output = CB.calc_binary(img)
    
    # Check if the output matches the expected output
    assert np.allclose(output, expected_output), "Test failed!"
    print("Test passed!")


def test_CalcBinary():
    result = CB.CalcBinary(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    expected = np.array([[0, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert np.array_equal(result, expected), f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    
    # Run the tests
    test_calc_binary_5x5()
    print("1 passed")
    test_calc_binary_4x4()
    print("2 passed")
    test_calc_binary2()
    print("3 passed")
    test_CalcBinary()
    print("Everything passed")
