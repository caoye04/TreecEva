def operation_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper

@operation_counter
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

@operation_counter
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Generate test data using dictionary comprehension
raw_data = {f'key_{i}': i*3 % 7 for i in range(10)}
test_array = list(raw_data.values())

# Perform sorting
sorted_result = merge_sort(test_array)

# Get the total number of operations
operation_count = merge_sort.counter + merge.counter
print(f'Result: {operation_count}')