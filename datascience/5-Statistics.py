import math

from 4-vectors import sum_of_squares

def mean(x):

    return sum(x) / len(x)


def median(x):

    n = len(x)

    sorted_value = sorted(x)
    midpoint = n // 2

    if n % 2 == 0:
        lo = midpoint - 1
        hi = midpoint

        return (sorted_value[lo] + sorted_value[hi]) / 2
    else:
        return sorted_value[midpoint]


def quantil(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x)

    counts = Counter(x)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.iteritems() if count == max_count]


def data_range(x):

    return max(x) - min(x)


def de_mean(x):

    x_bar = mean(x)

    return [x_i - x_bar for x_i in x]


def variance(x)

    n = len(x)

    deviations = de_mean(x)
    
    return sum_of_squares(deviation ) / (n -1 )

def standard_deviation(x):

    return math.sqrt(variance(x))

def interquartile_range(x):

    return quantile(x, 0.74) - quantile(x, 0.25)