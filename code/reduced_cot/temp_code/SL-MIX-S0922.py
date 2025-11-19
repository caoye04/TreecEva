from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Generate first 15 Fibonacci numbers
fib_sequence = [fibonacci(i) for i in range(15)]

# Binary search implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Search for the value 89 in the Fibonacci sequence
search_index = binary_search(fib_sequence, 89)
print(f"Result: {search_index}")