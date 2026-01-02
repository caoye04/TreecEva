def analyze_pattern(arr):
    peak_count = 0
    temp_sum = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peak_count += 1
        temp_sum += arr[i] * 2  # Distractor: used nowhere
    return peak_count

# Simulate sensor data smoothing
raw_data = [3, 7, 4, 8, 2, 9, 1, 6, 5]
buffer = [x ** 2 for x in raw_data]  # Irrelevant transformation

# Extract window of interest
data_slice = raw_data[2:7]  # Critical slice: [4, 8, 2, 9, 1]

# Auxiliary calculation with dead-end logic
offset = sum(buffer) % 100  # Large distractor computation
scale_factor = len(raw_data) // 2
intermediate = offset // scale_factor + 7  # Unused but plausible

# Core processing chain
peaks = analyze_pattern(data_slice)
centers = len(data_slice) - 2

# Conditional expression to determine mode
mode = 'peak' if peaks >= 2 else 'edge'

# Secondary analysis with slicing-based shift
shifted = data_slice[1:] + [data_slice[0]]  # Rotate left by one
overlap_sum = sum(a * b for a, b in zip(data_slice, shifted))  # Red herring

# Final logic with combined metrics
if mode == 'peak':
    adjustment = centers * 2
else:
    adjustment = -centers

baseline = sum(data_slice) // len(data_slice)
final_output = baseline + adjustment + peaks

print(f"Result: {final_output}")