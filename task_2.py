from functools import lru_cache
import matplotlib.pyplot as plt
import time
from splay_tree import SplayTree


@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree):
    if n <= 1:
        return n

    cached_value = tree.find(n)
    if cached_value is not None:
        return cached_value
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


def measure_time(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start


def visualization(numbers, lru, splay):
    plt.plot(numbers, lru, label="LRU Cache", marker="o")
    plt.plot(numbers, splay, label="Splay Tree", marker="x")
    plt.xlabel("n (Fibonacci Number Index)")
    plt.ylabel("Execution Time (s)")
    plt.title("Performance Comparison: LRU Cache vs Splay Tree")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    fibonacci_numbers = list(range(0, 951, 50))
    lru_times = []
    splay_times = []
    tree = SplayTree()

    for n in fibonacci_numbers:
        lru_times.append(measure_time(fibonacci_lru, n))
        splay_times.append(measure_time(fibonacci_splay, n, tree))

    visualization(fibonacci_numbers, lru_times, splay_times)

    print(f"{'n':<10}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)':<25}")
    print("-" * 60)
    for n, lru, splay in zip(fibonacci_numbers, lru_times, splay_times):
        print(f"{n:<10}{lru:<25.8f}{splay:<25.8f}")
