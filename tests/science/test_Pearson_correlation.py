from science.Pearson_correlation import *


def roughly_equal(a, b, d:int=1000000) -> bool:
    differance = a - b
    abs_diff = abs(differance)
    if abs_diff > 1/d:
        return False
    return True


def test_average():
    vector = [1, 5, 9, 2, 3]
    assert sum(vector) == 20
    result = average(vector)
    assert type(result) is float
    assert result == 4


def test_top_sum():
    X = [1, 5, 9, 2, 3]
    Y = [3, 5, 1, 6, 8]
    expected_result = (1-4)*(3-4.6) + (5-4)*(5-4.6) + (9-4)*(1-4.6) + (2-4)*(6-4.6) + (3-4)*(8-4.6) # == -19

    result = top_sum(X, Y, 4.0, 4.6)
    assert type(result) is float
    assert result == expected_result


def test_bottom_sum():
    vector1 = [1, 5, 9, 2, 3]
    expected_result1 = (1-4)**2 + (5-4)**2 + (9-4)**2 + (2-4)**2 + (3-4)**2 # == 40

    result1 = bottom_sum(vector1, 4.0)
    assert type(result1) is float
    assert result1 == expected_result1 == 40

    vector2 = [3, 7, 2, 6, 8]
    expected_result2 = (3-5.2)**2 + (7-5.2)**2 + (2-5.2)**2 + (6-5.2)**2 + (8-5.2)**2 # == 26.8
    
    result2 = bottom_sum(vector2, 5.2)
    assert type(result2) is float
    assert result2 == expected_result2 == 26.8


def test_Pearson_correlation():
    X = [1, 5, 9, 2, 3]
    Y = [3, 5, 1, 6, 8]
    result1 = Pearson_correlation(X, Y)
    assert type(result1) is float
    assert result1 >= -1 and result1 <= 1

    result2 = Pearson_correlation(X, X)
    assert roughly_equal(result2, 1)

    X_ = [1, 2, 3, 4, 5]
    Y_ = [5, 4, 3, 2, 1]
    result3 = Pearson_correlation(X_, Y_)
    assert roughly_equal(result3, -1)

    # Example values from:
    # https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
    wiki_X = [1, 2, 3, 4, 5, 8]
    wiki_Y = [0.11, 0.12, 0.13, 0.14, 0.15, 0.18]
    result4 = Pearson_correlation(wiki_X, wiki_Y)
    assert roughly_equal(result4, 1) # 0.920814711)

    # Example values from:
    # https://www.spss-tutorials.com/pearson-correlation-coefficient/
    spss_X = [0, 7, 6, 2, 3, 3, 3, 4, 3, 0]
    spss_Y = [3, 7, 6, 4, 3, 4, 5, 4, 1, 0]
    result5 = Pearson_correlation(spss_X, spss_Y)
    assert roughly_equal(result5, 0.785, d=1000)


def test_Pearson_on_list_of_lists():
    a = [1, 5, 9, 2, 3]
    b = [3, 5, 1, 6, 8]
    c = [1, 2, 3, 4, 5]
    d = [5, 4, 3, 2, 1]
    X = [a, b, c, d]

    results = Pearson_on_list_of_lists(X)

    assert type(results) is list
    assert len(results) == 3
    
    # Test [0] and [1] are assumed from the output.
    # Test [2] is calculated.
    assert roughly_equal(results[0], -0.5559454491816201)
    assert roughly_equal(results[1], 0.643726309578718)
    assert roughly_equal(results[2], -1)
