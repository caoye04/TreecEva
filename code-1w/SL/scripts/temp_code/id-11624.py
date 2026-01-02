import math

# Simulated sensor array data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = [2.1, 3.5, 4.8, 5.0, 6.2, 7.3, 8.0, 9.1, 10.5]
    offset = 0.5
    adjusted = [x + offset for x in raw_readings]
    return adjusted

# Irrelevant auxiliary function - decoy
def calculate_efficiency_factor(n):
    if n <= 1:
        return 1
    return n * calculate_efficiency_factor(n - 1)

# Unused transformation - red herring
def transform_scale(values, factor=1.1):
    return [v * factor for v in values]

# Preprocessing with slicing and filtering
def preprocess_readings(data):
    window = data[2:7]  # Slice middle portion
    filtered = [x for x in window if x > 5.0]
    padding = [0.1, 0.2]
    extended = filtered + padding  # Add irrelevant elements
    normalized = [round(x / sum(extended) * 100, 2) for x in extended]  # Diversion
    return extended  # Only extended matters for next step

# Secondary analysis with distractor variables
def compute_baseline(readings):
    total = sum(readings)
    count = len(readings)
    average = total / count
    variance_accum = 0
    for val in readings:
        variance_accum += (val - average) ** 2
    variance = variance_accum / count
    std_dev = math.sqrt(variance)
    
    # Decoy statistics
    skewness_hint = (average ** 3) / (std_dev + 1e-8)
    kurtosis_proxy = (sum([x**4 for x in readings]) / count) / (variance + 1e-8)
    
    # Actual baseline derived from std_dev, not used directly
    return average, std_dev

# Core logic buried in multiple checks
def validate_stability(metrics, limit=6.0):
    temp_record = [1.1, 2.2, 3.3]
    history_check = len(temp_record) > 2
    
    primary_metric = metrics[0] if len(metrics) > 0 else 0
    secondary_metric = math.log(primary_metric + 1) if primary_metric > 0 else 0
    
    # Distractor condition
    if secondary_metric > 2.5:
        adjustment = 1.5
    else:
        adjustment = 0.7
    
    # Stability is actually determined by this simple comparison
    stable_flag = primary_metric < limit
    return stable_flag, adjustment

# Main analysis with misleading complexity
def analyze_readings(data, thresh):
    # Redundant validations
    if not data or len(data) == 0:
        return -1
    
    # Compute aggregate measures (some irrelevant)
    magnitude = sum([x**2 for x in data])
    peak = max(data)
    duration = len(data) * 0.5
    
    # Dummy classification
    categories = ['A', 'B', 'C']
    classification_score = (peak * duration) % 3
    assigned_class = categories[int(classification_score)]
    
    # Critical but obscured computation
    cumulative_index = 0
    for i, val in enumerate(data):
        if val > thresh:
            cumulative_index += (i + 1) * val  # Weighted sum based on position
    
    # Secondary index - looks important but unused
    entropy_like = 0
    for x in data:
        if x > 0:
            entropy_like -= x * math.log(x)

    # Final decision influenced by validation
    metrics = compute_baseline(data)
    is_stable, adj = validate_stability(metrics)
    
    # Apply adjustment only if stable (this affects final result)
    if is_stable:
        cumulative_index -= adj * 10
    else:
        cumulative_index += 50
    
    # Dead code branch - never executed due to logic above
    if len(data) > 20:
        fallback = sum(data) // 2
        return fallback

    return int(cumulative_index)

# Execution flow with hidden dependencies
sensor_data = collect_sensor_readings()
processed_data = preprocess_readings(sensor_data)
threshold = 6.5

# Irrelevant counters
loop_counter = 0
status_flags = []
for item in processed_data:
    if item > 5.0:
        loop_counter += 1
        status_flags.append(True)
    else:
        status_flags.append(False)

# Decoy function calls
efficiency = calculate_efficiency_factor(4)
efficiency_scaled = efficiency * 0.3

# Unused transformations
scaled_data = transform_scale(processed_data, 1.05)
scaled_data_reversed = scaled_data[::-1]

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold)

print(f"Target result: {final_diagnostic}")