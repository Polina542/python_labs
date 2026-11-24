import csv
import timeit
import random

from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, counting_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def data(n):
    """случайный список из n чисел от -1000 до 1000"""
    random.seed(42)
    return [random.randint(-10000, 10000) for _ in range(n)]


def counting_data(n):
    random.seed(42)
    return [random.randint(-1000, 1000) for _ in range(n)]


def bench_sorts(n):
    nums = data(n)
    rows = []
    functions = [sorted, bubble_sort,
                 insertion_sort, selection_sort, merge_sort, counting_sort]
    functions_n2 = [bubble_sort, insertion_sort, selection_sort]

    for fn in functions:
        if fn == counting_sort:
            t = timeit.timeit(lambda: counting_sort(
                list(nums), lo=-10000, hi=10000), number=1)
            rows.append(("sort", n, "counting_sort", t))
        else:
            if n <= 10_000 or fn not in functions_n2:
                t = timeit.timeit(lambda: fn(list(nums)), number=1)
                rows.append(("sort", n, fn.__name__, t))

    return rows


def sorted_counting_sort(n):
    nums = counting_data(n)
    rows = []
    t = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("sort", f"{n} [-1000, 1000]", "sorted", t))

    t = timeit.timeit(lambda: counting_sort(nums, lo=-1000, hi=1000), number=1)
    rows.append(("sort", f"{n} [-1000, 1000]", "counting_sort", t))

    return rows


def bench_search(n):
    nums = data(n)
    target = random.randint(-1000, 1000)
    rows = []

    t = timeit.timeit(lambda: linear_search(nums, target), number=10_000)
    rows.append(("search", n, "linear_search", t))

    nums = sorted(data(n))
    t = timeit.timeit(lambda: binary_search(
        nums, target), number=10_000)
    rows.append(("search", n, "binary_search", t))

    return rows


def bench_two_sum(n):
    nums = data(n)
    target = random.randint(-1000, 1000)
    rows = []
    functions = [two_sum_brute, two_sum_fast]

    for fn in functions:
        t = timeit.timeit(lambda: fn(nums, target), number=1)
        rows.append(("two_sum", n, fn.__name__, t))

    return rows


def main():
    with open("data/lab07/bench.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["task", "n", "impl", "seconds"])
        for n in (1000, 10_000, 100_000):
            writer.writerows(bench_sorts(n))

        writer.writerows(sorted_counting_sort(100_000))

        writer.writerows(bench_search(100_000))

        for n in (1000, 10_000):
            writer.writerows(bench_two_sum(n))

    with open("data/lab07/bench.csv", "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        headers = reader.fieldnames

        header_line = f"{headers[0]:<10} | {headers[1]:>10} | {headers[2]:<20} | {headers[3]:>12}"
        separator = "-" * len(header_line)

        print(header_line)
        print(separator)

        for row in reader:
            task = row["task"]
            try:
                n = int(row["n"])
            except ValueError:
                n = row["n"]
            impl = row["impl"]
            seconds = float(row["seconds"])
            print(f"{task:<10} | {n:>20} | {impl:<20} | {seconds:12.6f}")


if __name__ == "__main__":
    main()
