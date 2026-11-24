def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums_copy = list(nums)
    n = len(nums_copy)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums_copy[j] > nums_copy[j + 1]:
                nums_copy[j], nums_copy[j + 1] = nums_copy[j + 1], nums_copy[j]
                swapped = True
        if not swapped:
            break
    return nums_copy


def insertion_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""

    nums_copy = list(nums)
    n = len(nums_copy)

    for i in range(1, n):
        num = nums_copy[i]
        j = i - 1
        while j >= 0 and nums_copy[j] > num:
            nums_copy[j + 1] = nums_copy[j]
            j -= 1
        nums_copy[j + 1] = num

    return nums_copy


def selection_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""

    nums_copy = list(nums)
    n = len(nums_copy)

    for i in range(n):
        mn_index = i
        for j in range(i, n):
            if nums_copy[j] < nums_copy[mn_index]:
                mn_index = j
        if i != mn_index:
            nums_copy[i], nums_copy[mn_index] = nums_copy[mn_index], nums_copy[i]
    return nums_copy


def merge_sort(nums):
    """
    сортировка слиянием без рекурсии

    возвращает список, отсортированный по возрастанию. Исходный не меняется.

    merge_sort([3, 1, 2]) -> [1, 2, 3]
    merge_sort([1]) -> [1]
    merge_sort([]) -> []
    """

    n = len(nums)
    if n <= 1:
        return list(nums)

    nums_copy = list(nums)
    temp = [0] * n

    ln = 1
    while ln < n:
        i = 0
        while i < n:
            left = i
            mid = min(i + ln, n)
            right = min(i + 2 * ln, n)

            l, r, k = left, mid, left

            while l < mid and r < right:
                if nums_copy[l] <= nums_copy[r]:
                    temp[k] = nums_copy[l]
                    l += 1
                else:
                    temp[k] = nums_copy[r]
                    r += 1
                k += 1

            while l < mid:
                temp[k] = nums_copy[l]
                l += 1
                k += 1
            while r < right:
                temp[k] = nums_copy[r]
                r += 1
                k += 1

            for idx in range(left, right):
                nums_copy[idx] = temp[idx]
            i += 2 * ln
        ln *= 2

    return nums_copy


def counting_sort(nums, lo, hi):
    """
    сортировка подсчётом для целых чисел в известном диапазоне [lo, hi]
    возвращает новый список, отсортированный по возрастанию. Исходный не меняется

    counting_sort([3, 1, 2, 3], 1, 5) -> [1, 2, 3, 3]
    counting_sort([5, 5, 5], 5, 10) -> [5, 5, 5]
    counting_sort([], 0, 10) -> []
    """

    n = len(nums)
    if n <= 1:
        return list(nums)

    range_size = hi - lo + 1
    count = [0] * range_size

    for x in nums:
        count[x - lo] += 1

    res = []
    for offset, c in enumerate(count):
        if c > 0:
            value = lo + offset
            res.extend([value] * c)

    return res


if __name__ == "__main__":
    print(bubble_sort([3, 1, 2]))
    print(bubble_sort([3, 2, 1]))
    print(bubble_sort([]))

    print(insertion_sort([3, 1, 2]))
    print(insertion_sort([3, 2, 1]))
    print(insertion_sort([]))

    print(selection_sort([3, 1, 2]))
    print(selection_sort([3, 2, 1]))
    print(selection_sort([]))

    print(merge_sort([3, 1, 2]))
    print(merge_sort([1]))
    print(merge_sort([]))

    print(counting_sort([3, 1, 2, 3], 1, 5))
    print(counting_sort([5, 5, 5], 5, 10))
    print(counting_sort([], 0, 10))
