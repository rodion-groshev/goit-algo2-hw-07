## Task 1. Optimizing data access using the LRU cache

>   Implement script to optimize the processing of queries to an array of numbers using the LRU cache.

#### Specifications:

1. You are given an array of size N consisting of positive integers (1 ≤ N ≤ 100_000). You are to process Q queries (1 ≤ Q ≤ 50_000) of this type:

    -   Range(L, R) - find the sum of elements in the interval from index L to R inclusive.
    -   Update(index, value) - replace the value of the element in the array at index with the new value value.

2. Implement four functions to work with an array:


    range_sum_no_cache(array, L, R) 

The function must calculate the sum of the elements of the array in the interval from L to R inclusive without using the cache. For each request, the result must be calculated anew.

    update_no_cache(array, index, value) 

The function should update the value of an array item at the specified index without using the cache.

    range_sum_with_cache(array, L, R) 

The function must calculate the sum of the elements in the range from L to R inclusive, using the LRU cache. If the sum for this segment has already been calculated before, it should be returned from the cache, otherwise the result is calculated and added to the cache.

    update_with_cache(array, index, value) 

The function must update the value of the array element at the specified index and delete all corresponding values from the cache that have become irrelevant due to a change in the array.


## Task 2. Compare the performance of calculating Fibonacci numbers using LRU cache and Splay Tree


>   Implement a program to calculate Fibonacci numbers in two ways: using the LRU cache and using the Splay Tree to store previously calculated values. Perform a comparative analysis of their performance by measuring the average execution time for each approach.

#### Specifications:

 Implement two functions for calculating Fibonacci numbers:

    fibonacci_lru(n)

The function should use the @lru_cache decorator to cache the calculation results. This allows it to reuse previously calculated Fibonacci number values.

    fibonacci_splay(n, tree) 

The function uses the Splay Tree data structure to store the calculated values. If the Fibonacci number for the given n has already been calculated, the value must be returned from the tree, otherwise the value is calculated, stored in the Splay Tree, and returned.


