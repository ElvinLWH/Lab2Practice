import Lab2Practice
def test_find_min_max():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7]
    test_arr = [1, 7]

    result = Lab2Practice.find_min_max(input_arr)

    assert (result == test_arr)

def test_calc_average():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7]
    expected_result = 4

    result = Lab2Practice.calc_average(input_arr)

    assert (result == expected_result)

def test_calc_median_temperature():
    result = []
    input_arr = [1, 2, 3, 4, 5, 6, 7]
    expected_result = 4

    result = Lab2Practice.calc_median_temperature(input_arr)

    assert (result == expected_result)