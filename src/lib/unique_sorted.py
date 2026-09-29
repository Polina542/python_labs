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
