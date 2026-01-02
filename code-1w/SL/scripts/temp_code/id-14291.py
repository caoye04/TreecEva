import math

# Sensor simulation data (irrelevant for final result but adds distraction)
sensor_offsets = [0.1, -0.3, 0.5, 0.0, -0.2]
baseline_correction = sum([abs(x) for x in sensor_offsets])

# Irrelevant calibration function
def calibrate_sensor(x):
    if x < 0:
        return math.log(abs(x) + 1) * 1.5
    else:
        return math.exp(x / 10) - 1

# Unused but plausible-looking transformation
def frequency_transform(data_list):
    transformed = []
    for i, val in enumerate(data_list):
        phase = math.sin(i * math.pi / 4)
        transformed.append(val * phase)
    return transformed  # Never called

# Core data processing chain
raw_readings = [12, 15, 10, 23, 8, 19, 14, 16, 11, 20]

# Distractor: complex-looking but unused filtering
temp_filtered = list(filter(lambda x: x > 10, raw_readings))

# Real processing begins here
processed_data = [
    x ** 2 - 2 * x + 1 for x in raw_readings  # (x-1)^2 transformation
]

# Multiple irrelevant intermediate calculations
aggregate_score = sum([math.ceil(math.sqrt(x)) for x in processed_data]) // 3
weighting_factor = max(aggregate_score // 100, 1)

# Decoy conditional with misleading logic
if len(raw_readings) % 2 == 0 and aggregate_score > 50:
    dummy_result = (weighting_factor + 5) * 8
else:
    dummy_result = 0

dummy_result *= 2  # Dead-end computation

# Define threshold function using lambda and conditional expression
threshold_func = lambda x: x > (150 if len(processed_data) > 8 else 100)

# Simulated auxiliary analysis (unused result)
def analyze_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum([(x - mean_val) ** 2 for x in data]) / len(data))
    return [x for x in data if abs(x - mean_val) > 2 * std_dev]

# Real analysis function with nested logic
min_acceptable = 100
def analyze_readings(data, threshold_strategy):
    count_above = 0
    running_total = 0
    for idx, reading in enumerate(data):
        # Complex conditional with side-effect-like structure but no real side effects
        adjustment = (idx % 3) + 1
        adjusted_reading = reading - adjustment * 2
        
        # Critical logic step: only readings above min_acceptable are counted
        if adjusted_reading > min_acceptable:
            count_above += 1
        
        # Running total accumulates all adjusted readings
        running_total += adjusted_reading
    
    # Determine diagnostic level based on multiple factors
    if count_above >= 6 and running_total > 700:
        level = 9
    elif count_above >= 4 and running_total > 500:
        level = 7
    elif threshold_strategy(running_total):  # Uses lambda strategy
        level = 5
    else:
        level = 3
    
    # Final transformation (key step)
    diagnostic_code = (level * 11) + (running_total % 10)
    return diagnostic_code

# Misleading secondary function that looks important
def compute_system_health(readings):
    peak = max(readings)
    normalized = [x / peak for x in readings]
    entropy = -sum([p * math.log(p) for p in normalized if p > 0])
    return int(entropy * 10)

# Unused recursive red herring
def binary_weight(n):
    if n <= 1:
        return n
    return (n % 2) + binary_weight(n // 2)

health_estimate = compute_system_health(raw_readings)  # Dead end

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_func)

# Output the target result
print(f"Result: {final_diagnostic}")