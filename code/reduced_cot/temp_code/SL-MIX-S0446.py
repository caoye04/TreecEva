from functools import reduce
from bisect import bisect_left
def binary_search(arr, x):
    i = bisect_left(arr, x)
    return i != len(arr) and arr[i] == x

tags_collection = frozenset(['alpha', 'beta', 'gamma', 'delta', 'epsilon'])
transformed_tags = list(map(lambda s: len(s), tags_collection))
transformed_tags.sort()
filtered_lengths = list(filter(lambda n: n > 4, transformed_tags))
checksum = reduce(lambda a, b: a ^ b, filtered_lengths, 0)
reference_values = [3, 5, 7, 9, 11]
matches = sum(1 for val in filtered_lengths if binary_search(reference_values, val))
validation_flags = [len(filtered_lengths) > 2, checksum != 0, matches >= 1]
final_validation_score = sum(1 << i for i, flag in enumerate(validation_flags) if flag)
print(f'Result: {final_validation_score}')