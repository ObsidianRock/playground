


def vector_add(v, w):

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_sub(v, w):
    return  [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):

    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

vector_sum(([1,2,5], [6,1,6]))  # 1+6, 2+1, 5+6

if __name__ == '__main__':

    pass