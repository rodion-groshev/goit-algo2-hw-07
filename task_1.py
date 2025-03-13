import time
from functools import lru_cache
from random import randint, random


def range_sum_no_cache(array, L, R):
    return sum(array[L:R])


def update_no_cache(array, index, value):
    array[index] = value


@lru_cache(maxsize=1000)
def range_sum_with_cache(tuple_arr, L, R):
    return sum(tuple_arr[L:R])


def update_with_cache(array, index, value):
    array[index] = value
    range_sum_with_cache.cache_clear()


len_array = 100000
requests_number = 50000

array = [randint(1, 100) for _ in range(len_array)]


requests = [
    (
        ("Range", randint(0, len_array - 1), randint(0, len_array - 1))
        if random() > 0.7
        else ("Update", randint(0, len_array - 1), randint(1, 100))
    )
    for _ in range(requests_number)
]


start = time.time()
for request in requests:
    if request[0] == "Range":
        L, R = min(request[1], request[2]), max(request[1], request[2])
        range_sum_no_cache(array, L, R)
    else:
        update_no_cache(array, request[1], request[2])
print("Execution time without caching:", time.time() - start, "секунд")

start = time.time()
for request in requests:
    if request[0] == "Range":
        L, R = min(request[1], request[2]), max(request[1], request[2])
        range_sum_with_cache(tuple(array), L, R)
    else:
        update_with_cache(array, request[1], request[2])
print("Execution time with LRU-cache:", time.time() - start, "секунд")
