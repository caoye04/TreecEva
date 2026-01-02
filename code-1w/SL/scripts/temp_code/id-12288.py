import math

# Simulated system performance metrics over time
def generate_metrics():
    raw_data = [15, 22, 8, 43, 19, 31, 14, 37]
    processed = []
    for val in raw_data:
        if val > 20:
            processed.append(val * 0.85)
        else:
            processed.append(val * 1.1)
    return processed

# Noise injection: irrelevant data generation (distractor)
def generate_noise(n):
    result = []
    for i in range(n):
        result.append((i * i + 3 * i + 7) % 100)
    return result

noise = generate_noise(10)

# Weighted average with decay factor (semi-relevant computation)
def moving_average(data, alpha=0.3):
    if not data:
        return 0
    avg = data[0]
    for i in range(1, len(data)):
        avg = alpha * data[i] + (1 - alpha) * avg
    return round(avg, 3)

# Bitwise masking to simulate 'data corruption check' (distractor)
def validate_integrity(x):
    mask = 0xFF
    return (x & mask) ^ 0xAA == (x ^ 0xAA) & mask

# Threshold function using lambda (required Python feature)
threshold_func = lambda x: x > 20.0

# Combinatoric helper: counts pairs satisfying condition (some relevant, some not)
def count_pairs(arr, condition):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if condition(arr[i], arr[j]):
                count += 1
    return count

# Real pair analysis used later
def significant_jump(a, b):
    return b - a >= 5

# Unused distractor function
def correlation_approx(x_arr, y_arr):
    if len(x_arr) != len(y_arr) or len(x_arr) == 0:
        return 0.0
    mean_x = sum(x_arr) / len(x_arr)
    mean_y = sum(y_arr) / len(y_arr)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_arr, y_arr))
    den = math.sqrt(sum((x - mean_x)**2 for x in x_arr)) * math.sqrt(sum((y - mean_y)**2 for y in y_arr))
    return round(num / den if den != 0 else 0, 4)

# Main assessment logic
metrics_log = generate_metrics()

# Irrelevant transformation chain (distractor)
temp_scaled = [round(x * 1.07, 2) for x in metrics_log]
deviations = [abs(x - moving_average(metrics_log)) for x in temp_scaled]

# Core logic begins
above_threshold = [threshold_func(x) for x in metrics_log]
valid_entries = [x for x in metrics_log if x > 10]

# Counting pattern of interest
jump_count = count_pairs(valid_entries, significant_jump)

# Data filtering and transformation
filtered_metrics = list(filter(lambda x: x > 15, metrics_log))

# Redundant state tracking (intermediate distractor)
counter_state = {
    'total': len(metrics_log),
    'above_thresh': sum(above_threshold),
    'processed': len(filtered_metrics)
}

# Final performance assessment
assess_performance = lambda data, thresh: (
    sum(thresh(x) for x in data) * 10 + 
    len(data) // 2 - 
    count_pairs(data[:len(data)//2], lambda a, b: a > b)
)

final_analysis = assess_performance(metrics_log, threshold_func)

# Efficiency score derived from final analysis and jump pattern
baseline_score = moving_average(metrics_log)
efficiency_score = final_analysis + jump_count - int(baseline_score)

# Print target result
print(f"Target result: {efficiency_score}")