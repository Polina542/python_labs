import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(
            nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_counting_sort(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        if nums:
            lo = random.randint(min(nums) - 100, min(nums))
            hi = random.randint(max(nums), max(nums) + 100)

            original = list(nums)
            result = counting_sort(nums, lo, hi)
            assert result == sorted(
                nums), f"counting_sort ошиблась на {nums}: {result}"
            assert nums == original, f"counting_sort изменила исходный список"
        else:
            assert n == 0, "понятия не имею"


def check_linear_search(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        target = random.randint(-150, 150)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums, target)
        try:
            answer = nums.index(target)
        except ValueError:
            answer = -1
        assert result == answer, f"{fn.__name__} ошиблась на {nums}: {result}, верный ответ: {answer}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_binary_search(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        target = random.randint(-150, 150)
        nums = sorted([random.randint(-100, 100) for _ in range(n)])
        original = list(nums)
        result = fn(nums, target)
        try:
            answer = nums.index(target)
        except ValueError:
            answer = -1
        assert result == answer, f"{fn.__name__} ошиблась на {nums}: {result}, верный ответ: {answer}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_two_sum(trials=1000):
    for trial in range(trials):
        n = random.randint(0, 50)
        target = random.randint(-50, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        res1 = two_sum_brute(nums, target)
        res2 = two_sum_fast(nums, target)

        if res1 is None and res2 is None:
            continue

        if res1 is not None and res2 is not None:
            i1, j1 = res1
            i2, j2 = res2

            assert i1 != j1, f"Индексы совпали в two_sum_brute: {res1} на nums={nums}, target={target}"
            assert all(0 <= idx < len(nums) for idx in (i1, j1)
                       ), f"Неверные индексы в two_sum_brute: {res1}"
            assert nums[i1] + \
                nums[j1] == target, f"Сумма не совпадает в two_sum_brute: {nums[i1]} + {nums[j1]} != {target}"

            assert i2 != j2, f"Индексы совпали в two_sum_fast: {res2} на nums={nums}, target={target}"
            assert all(0 <= idx < len(nums) for idx in (i2, j2)
                       ), f"Неверные индексы в two_sum_fast: {res2}"
            assert nums[i2] + \
                nums[j2] == target, f"Сумма не совпадает в two_sum_fast: {nums[i2]} + {nums[j2]} != {target}"
            continue

        raise AssertionError(
            f"Разные результаты на nums={nums}, target={target}\n"
            f"two_sum_brute={res1}, two_sum_fast={res2}"
        )


def main():
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort, merge_sort):
        check_sorting(fn)
    print("сортировки - OK")

    check_counting_sort()

    check_linear_search(linear_search)
    print("линейный поиск - OK")

    check_binary_search(binary_search)
    print("бинарный поиск - OK")

    check_two_sum()
    print("two_sum - OK")


if __name__ == "__main__":
    main()
