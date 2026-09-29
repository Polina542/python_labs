def transpose(mat):
    '''транспонирует прямоугольную матрицу'''
    if len(mat) == 0:
        return mat
    m = len(mat)
    n = len(mat[0])

    for row in mat:
        if len(row) != n:
            raise ValueError('строки разной длины')

    if len(mat[0]) == 0:
        return []

    # создание нулевой матрицы размера n*m (для исходной матрицы m*n)
    transposed_mat = [[mat[i][j] for i in range(m)] for j in range(n)]

    for i in range(m):
        for j in range(n):
            transposed_mat[j][i] = mat[i][j]

    return transposed_mat


def row_sums(mat):
    '''возвращает список с суммой чисел в каждой строке матрицы'''
    if len(mat) == 0:
        return []

    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("строки разной длины")

    return [sum(row) for row in mat]


def col_sums(mat):
    '''возвращает список с суммой чисел в каждом столбце матрицы'''
    if len(mat) == 0:
        return []

    transposed_mat = transpose(mat)
    return row_sums(transposed_mat)
