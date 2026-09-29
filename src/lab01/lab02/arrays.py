# 1
def min_max(nums):
    '''возвращает минимальный и максимальный элементы списка nums в виде кортежа (min,max)'''

    if len(nums) == 0:
        raise ValueError('пустой список')

    mn = nums[0]
    mx = nums[0]
    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return (mn, mx)


# 2
def bubble_sort(l):  # пузырьковая сортировка
    n = len(l)
    for i in range(n):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def unique_sorted(nums):
    '''возвращает отсортированный список уникальных значений по возрастанию'''
    unique_nums = list(set(nums))
    return bubble_sort(unique_nums)


# 3
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


# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
# print(unique_sorted([]))

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
