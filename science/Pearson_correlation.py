import math


def average(vector:list) -> float:
    """Find the average of a list."""
    total = 0
    for number in vector:
        total += number
    
    avg = total / len(vector)
    return avg


def covariance(X:list, Y:list) -> float:
    """Find the coveriance of X and Y."""
    avg_X = average(X)
    avg_Y = average(Y)

    total = 0
    for i in range(len(X)):
        total += (X[i] - avg_X) * (Y[i] - avg_Y)
    
    return total


def standard_deviation(vector:list) -> float:
    """Find the standard deviation of the vector."""
    avg = average(vector)

    total = 0
    for value in vector:
        total += (value - avg)**2

    return total


def Pearson_correlation_coefficient(X:list, Y:list) -> float:
    """Find the Pearson correlation coefficient (r)
    between two vectors or lists (X and Y) of equal length. 

    r_{X,Y} = ( covariance(X,Y) )/( standard_deviation(X), standard_deviation(Y) )
    """
    assert len(X) == len(Y)

    numenator = covariance(X, Y)
    
    sd_X = standard_deviation(X)
    sd_Y = standard_deviation(Y)
    denominator = math.sqrt(sd_X) * math.sqrt(sd_Y)

    if denominator == 0:
        return 0
    r = numenator / denominator
    return r


def Pearson_on_list_of_lists(X:list) -> list:
    """Compare one element to the next in a list of lists.
    Return the list of results.
    Input: list of lists
    Output: list."""
    assert len(X) > 1
    assert type(X[0]) is list
    print(type(X[0][0]), X[0][0])
    assert type(X[0][0]) is int or type(X[0][0]) is float

    results = []

    for i in range(len(X) - 1):
        results.append(Pearson_correlation_coefficient(X[i], X[i + 1]))
    
    return results


if __name__ == '__main__':
    a = [2, 7, 8, 4, 6]
    b = [8, 4, 3, 2, 3]
    
    c = Pearson_correlation_coefficient(a, b)
    print(c)
