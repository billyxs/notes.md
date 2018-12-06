# Add Matrix
# https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/
# https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/solution/

from itertools import zip_longest


def add(*matrices):
    """Solution - Add corresponding numbers in given 2-D matrices."""
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e


def add_a(*matrices):
    """Solution - Add corresponding numbers in given 2-D matrices."""
    matrix_shapes = {
        tuple(len(r) for r in matrix)
        for matrix in matrices
    }
    if len(set(matrix_shapes)) > 1:
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]


def add_1(*lists):
    "my solution - add matrices"
    res = []
    for parent in lists:
        if len(parent) != len(lists[0]):
            raise ValueError
        for cidx, citem in enumerate(parent):
            if len(citem) != len(parent[0]):
                raise ValueError
            for ccidx, value in enumerate(citem):
                if len(res) <= cidx:
                    res.append([])
                if len(res) and len(res[cidx]) <= ccidx:
                    res[cidx].append(0)
                res[cidx][ccidx] += value

    print(res)
    return res




