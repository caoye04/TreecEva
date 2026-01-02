def analyze_signal(data, multiplier=1.5):
    smoothed = []
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg * multiplier)

    outliers = []
    mean_val = sum(smoothed) / len(smoothed)
    variance_accum = 0
    for val in smoothed:
        variance_accum += (val - mean_val) ** 2
    std_dev = (variance_accum / len(smoothed)) ** 0.5

    for val in smoothed:
        if abs(val - mean_val) > 2 * std_dev:
            outliers.append(val)

    # Irrelevant transformation
    scaled_outliers = [x * 0.1 for x in outliers]
    noise_floor = 0.5 * std_dev

    filtered = [x for x in smoothed if x >= noise_floor]
    return filtered if filtered else [0]


def compress_data(sequence):
    compressed = []
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            count += 1
        else:
            compressed.append((sequence[i-1], count))
            count = 1
    compressed.append((sequence[-1], count))
    
    # Dead code path - never used
    temp_stats = {'max_run': max([c for _, c in compressed], default=0),
                  'total_elements': sum(c for _, c in compressed)}
    
    return [val for val, cnt in compressed if cnt >= 2]


def process_results(buffer, limit):
    if not buffer:
        return 0
    
    squared_sum = sum(x**2 for x in buffer)
    root_mean_square = (squared_sum / len(buffer)) ** 0.5
    
    # Distractor calculation
    harmonic_mean = len(buffer) / sum(1/x for x in buffer if x != 0)
    
    adjustment_factor = 1.0 if root_mean_square > limit else 0.5
    
    # Key branching with conditional expression
    final_value = root_mean_square * adjustment_factor if len(buffer) > 5 else root_mean_square / 2
    
    return int(final_value)

# Main execution
raw_input = [3, 7, 2, 8, 5, 6, 9, 4, 7, 8]
denoised_signal = analyze_signal(raw_input)

# Unnecessary intermediate processing
inverted = [10 - x for x in denoised_signal if x < 8]
duplicated = inverteded_signal = [x for x in inverted if x in denoised_signal]

# Another irrelevant aggregation
sum_check = 0
for num in raw_input:
    if num % 2 == 0:
        sum_check += num * 2

# Buffer construction used in target statement
temp_buffer = compress_data(denoised_signal)
threshold = 4.0
final_output = process_results(temp_buffer, threshold)
print(f"Result: {final_output}")