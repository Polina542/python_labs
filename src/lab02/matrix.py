# 1
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


# 2
def row_sums(mat):
    '''возвращает список с суммой чисел в каждой строке матрицы'''
    if len(mat) == 0:
        return []

    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("строки разной длины")

    return [sum(row) for row in mat]


# 3
def col_sums(mat):
    '''возвращает список с суммой чисел в каждом столбце матрицы'''
    if len(mat) == 0:
        return []

    transposed_mat = transpose(mat)
    return row_sums(transposed_mat)


# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))


# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([]))
# print(row_sums([[1, 2], [3]]))

# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([]))
# print(col_sums([[1, 2], [3]]))
