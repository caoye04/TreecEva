import math

# Simulated sensor data processing pipeline for environmental monitoring
def collect_sensor_data():
    raw_readings = [23.4, 19.5, 20.1, 18.8, 25.3, 22.7, 17.9, 24.6, 20.3, 19.8]
    calibration_offset = 0.7
    adjusted = [x + calibration_offset for x in raw_readings]
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def calculate_wind_chill(temps):
    return [13.12 + 0.6215*t - 11.37*(3**0.16) + 0.3965*t*(3**0.16) for t in temps]

# Data filtering with distractor logic
def filter_outliers(data, low=15, high=30):
    # Excessive and partially irrelevant computations
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    temp_flags = [False] * len(data)
    for i, x in enumerate(data):
        if abs(x - mean_val) > 2 * std_dev:
            temp_flags[i] = True
    
    # Actual filtering logic (simple range check)
    result = [x for x in data if low <= x <= high]
    
    # Unused and misleading intermediate
    outlier_count = len(data) - len(result)
    stability_score = (1 - (outlier_count / len(data))) * 100 if data else 100
    
    return result

# Complex conditional threshold logic
is_critical = lambda x: x > 23.5
is_elevated = lambda x: 22.0 < x <= 23.5
is_normal = lambda x: x >= 19.0

# Composite function that combines multiple lambdas (relevant)
def threshold_func(x):
    if is_critical(x):
        return 3
    elif is_elevated(x):
        return 2
    elif is_normal(x):
        return 1
    else:
        return 0

# Recursive transformation (bit manipulation red herring)
def transform_sequence(seq, depth=0):
    if depth >= 3 or not seq:
        return seq
    
    # Bitwise distraction - never actually used in final computation
    bit_shifted = [(int(x * 10) << 1) >> 1 for x in seq]
    shifted_back = [b / 10 for b in bit_shifted]
    
    # Real operation: square root dampening
    dampened = [math.sqrt(x * 10) for x in shifted_back]
    
    return transform_sequence(dampened, depth + 1)

# Core analysis function with decoy operations
def analyze_readings(readings, score_fn):
    # Multiple layers of processing with irrelevant counters
    total_samples = len(readings)
    category_counts = {"critical": 0, "elevated": 0, "normal": 0, "low": 0}
    cumulative_index = 0
    
    # Primary logic chain
    for val in readings:
        score = score_fn(val)
        if score == 3:
            category_counts["critical"] += 1
            cumulative_index += 17
        elif score == 2:
            category_counts["elevated"] += 1
            cumulative_index += 7
        elif score == 1:
            category_counts["normal"] += 1
            cumulative_index += 3
        else:
            category_counts["low"] += 1
            cumulative_index -= 1
    
    # Distractor: unused complex aggregation
    weighted_sum = sum(
        val * (score_fn(val) + 1) 
        for val in readings if score_fn(val) > 0
    )
    
    average_weighting = weighted_sum / len(readings) if readings else 0
    
    # Decoy transformation tree (never accessed)
    def build_diagnostic_tree(data):
        if not data:
            return {'node': 'empty', 'value': 0}
        mid = len(data) // 2
        return {
            'node': 'branch',
            'left': build_diagnostic_tree(data[:mid]),
            'right': build_diagnostic_tree(data[mid+1:]),
            'value': data[mid]
        }
    
    tree = build_diagnostic_tree(readings)  # Computed but unused
    
    # Final diagnostic calculation (this is the real answer)
    critical_penalty = category_counts["critical"] * 15
    elevated_bonus = category_counts["elevated"] * 5
    normal_base = category_counts["normal"] * 2
    low_penalty = category_counts["low"] * 10
    
    final_diagnostic = cumulative_index + critical_penalty - low_penalty
    
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_data()
filtered_data = filter_outliers(sensor_data)

# Dead function call - does nothing (distractor)
wind_chill_values = calculate_wind_chill(sensor_data)

# Unused recursive transformation
transformed = transform_sequence(filtered_data)

# Key statement
final_diagnostic = analyze_readings(filtered_data, threshold_func)

print(f"Result: {final_diagnostic}")