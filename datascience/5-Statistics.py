
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


def mode(x):

    count = Counter(x)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.iteritems() if count = max_count]