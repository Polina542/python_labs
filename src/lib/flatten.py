def flatten(mat):
    '''расплющивает матрицу в один список по строкам'''

    if type(mat) != list:
        raise TypeError('Введен не список')

    l = []
    for row in mat:
        if type(row) == list or type(row) == tuple:
            l.extend(row)
        else:
            raise TypeError(
                'элемент внутри списка не является списком или кортежем')
    return l
