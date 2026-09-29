def row_sums(mat):
    '''возвращает список с суммой чисел в каждой строке матрицы'''
    if len(mat) == 0:
        return []

    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("строки разной длины")

    return [sum(row) for row in mat]
