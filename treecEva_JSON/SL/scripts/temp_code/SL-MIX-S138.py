from collections import defaultdict

def bit_reverse(num, bits):
    result = 0
    for _ in range(bits):
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

def custom_sort_key(x):
    return bit_reverse(x, 4)

# Frequency bins from a signal analysis
freq_bins = [15, 7, 12, 3, 9, 6, 10, 5]

# Logical filter: values must be even AND greater than 4
filtered_bins = list(filter(lambda x: x > 4 and x % 2 == 0, freq_bins))

# Sort using custom bit-reversed key
sorted_bins = sorted(filtered_bins, key=custom_sort_key)

# Divide and conquer aggregation using defaultdict
aggregation = defaultdict(int)
for idx, val in enumerate(sorted_bins):
    if idx % 2 == 0:
        aggregation['even'] += val
    else:
        aggregation['odd'] += val

# Final metric calculation
final_metric = (aggregation['even'] >> 1) ^ (aggregation['odd'] << 1)

print(f"Result: {final_metric}")