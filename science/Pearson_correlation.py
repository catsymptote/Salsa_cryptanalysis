import math


def average(vector:list) -> float:
    """Find the average of a list."""
    total = 0
    for number in vector:
        total += number
    
    avg = total / len(vector)
    return avg


def top_sum(X, Y, avg_X, avg_Y):
    """Find the numerator of the Pearson correlation discrerte equation."""
    total = 0
    for i in range(len(X)):
        total += (X[i] - avg_X) * (Y[i] - avg_Y)
    
    return total


def bottom_sum(vector, avg):
    """Find one of the denominators of the Pearson correlation discrerte equation."""
    total = 0
    for value in vector:
        total += (value - avg)**2

    return total


def Pearson_correlation(X:list, Y:list) -> int:
    """Find the Pearson correlation between two vectors of equal length."""
    assert len(X) == len(Y)

    avg_X = average(X)
    avg_Y = average(Y)

    top = top_sum(X, Y, avg_X, avg_Y)
    
    bottom_X = bottom_sum(X, avg_X)
    bottom_Y = bottom_sum(Y, avg_Y)
    bottom = math.sqrt(bottom_X) * math.sqrt(bottom_Y)

    r = top / bottom
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
        results.append(Pearson_correlation(X[i], X[i + 1]))
    
    return results


if __name__ == '__main__':
    a = [2, 7, 8, 4, 6]
    b = [8, 4, 3, 2, 3]
    
    c = Pearson_correlation(a, b)
    print(c)
