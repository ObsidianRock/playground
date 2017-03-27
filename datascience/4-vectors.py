


def vector_add(v, w):

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_sub(v, w):
    return  [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):

    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

#vector_sum(([1,2,5], [6,1,6]))  # 1+6, 2+1, 5+6

def scalar_multiply(c, v):
    return [c * v_i for v_i in v ]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n , vector_sum(vectors))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


if __name__ == '__main__':

    pass