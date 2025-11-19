import math

def count_cookies_divide_conquer(batches):
    if len(batches) == 0:
        return 0
    if len(batches) == 1:
        return batches[0]
    mid = len(batches) // 2
    left_sum = count_cookies_divide_conquer(batches[:mid])
    right_sum = count_cookies_divide_conquer(batches[mid:])
    return left_sum + right_sum

cookie_batches = [12, 15, 10, 8, 20, 5, 17, 13]
total_cookies = count_cookies_divide_conquer(cookie_batches)
print(f"Result: {total_cookies}")