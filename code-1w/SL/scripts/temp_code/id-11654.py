def transform_value(x):
    if x < 0:
        return x ** 2 + 3
    elif x == 0:
        return 7
    else:
        return x * 2 - 1

# Sensor simulation (irrelevant but plausible)
sensor_offsets = {'A': 2.1, 'B': -1.3, 'C': 0.7}
baseline_readings = [15, -8, 0, 12, 22]

# Irrelevant transformation chain
temp_results = []
for val in baseline_readings:
    temp = val * sensor_offsets['A'] + sensor_offsets['B']
    temp_results.append(transform_value(int(temp)))

# Real data path begins
raw_data = [18, -6, 14, 9, -11, 7]
scaling_factor = 1.5
adjusted_data = [x * scaling_factor for x in raw_data]

# Distractor: unused function
def compute_integral(values):
    total = 0
    for i in range(1, len(values)):
        total += (values[i] + values[i-1]) / 2
    return total

# Processing with decoy operations
decoy_matrix = [[i * j for j in range(3)] for i in range(3)]
weight_map = {i: (i % 4) + 1 for i in range(6)}  # Unused in final logic

processed_data = []
for idx, val in enumerate(adjusted_data):
    if idx % 2 == 0:
        processed_data.append(int(val) + 5)
    else:
        processed_data.append(int(val) - 3)

# Threshold system with red herring parameters
defect_flags = [False] * len(processed_data)
counterfeit_weights = [0.1, 0.2, 0.3]  # Unused
threshold_map = {
    'low': -10,
    'normal': 0,
    'high': 15
}

# Misleading early analysis
preliminary_scores = []
for x in processed_data:
    if x < -5:
        preliminary_scores.append(1)
    elif x > 20:
        preliminary_scores.append(-1)
    else:
        preliminary_scores.append(0)

# Core recursive diagnostic engine (key logic)
def evaluate_severity(value, depth=0):
    if depth >= 3 or abs(value) < 2:
        return value
    if value > 0:
        return evaluate_severity(value // 2, depth + 1)
    else:
        return evaluate_severity(value + 4, depth + 1)

# Actual analysis function
def analyze_readings(data, thresholds):
    result = 0
    high_count = 0
    for val in data:
        if val > thresholds['high']:
            outcome = evaluate_severity(val)
            result += outcome
            high_count += 1
        elif val < thresholds['low']:
            # Special handling
            transformed = abs(val) % 7
            result += transformed * 2
        else:
            result += val // 3
    
    # Final adjustment based on pattern
    pattern_key = high_count % 4
    adjustment_map = {0: 5, 1: -3, 2: 8, 3: 0}
    return result + adjustment_map[pattern_key]

# Dead code path (never called)
def legacy_diagnostic(seq):
    return sum(x ** 0.5 for x in seq if x > 0)

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")