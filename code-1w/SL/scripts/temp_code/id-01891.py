import math

# Sensor simulation data (irrelevant but looks important)
baseline_offsets = [0.12, -0.34, 0.56, -0.78, 0.91]
signal_noise_ratio = {'alpha': 2.3, 'beta': 1.7, 'gamma': 3.1}

def generate_synthetic_readings(count):
    return [round(math.sin(i) * 100 + baseline_offsets[i % len(baseline_offsets)], 2) for i in range(count)]

# Unused signal processing function (dead code path)
def filter_signal(data, kernel_size=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - kernel_size // 2)
        end = min(len(data), i + kernel_size // 2 + 1)
        window = data[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Core diagnostic logic
operational_ranges = {
    'temp': (15, 30),
    'pressure': (950, 1050),
    'humidity': (30, 60),
    'vibration': (0, 10)
}

def validate_reading(reading, sensor_type):
    low, high = operational_ranges.get(sensor_type, (0, 100))
    return 1 if low <= reading <= high else 0

# Data transformation pipeline
def preprocess_readings(raw_list):
    scaled = [x * 1.05 for x in raw_list]  # calibration factor
    clipped = [max(0, min(x, 100)) for x in scaled]  # bound to 0-100
    normalized = [round(x / 100.0, 3) for x in clipped]
    return normalized

# Red herring: irrelevant combinatorics function
def count_valid_combinations(items, limit):
    if limit == 0 or items < limit:
        return 0
    numerator = math.factorial(items)
    denominator = math.factorial(limit) * math.factorial(items - limit)
    return numerator // denominator

# Threshold mapping with decoy entries
device_profiles = {
    'A': {'sensitivity': 0.8, 'tolerance': 0.05},
    'B': {'sensitivity': 0.9, 'tolerance': 0.03},
    'C': {'sensitivity': 0.7, 'tolerance': 0.07}
}

def build_threshold_map(profiles):
    t_map = {}
    for k, v in profiles.items():
        # Only 'B' matters in actual logic
        threshold = v['sensitivity'] * (1 - v['tolerance'])
        t_map[k] = round(threshold, 3)
    return t_map

# Main analysis with conditional nesting and list comprehension
def analyze_readings(data_sequence, thresholds):
    results = []
    
    # Real logic hidden among distractions
    for i, val in enumerate(data_sequence):
        # Simulate multi-sensor evaluation
        temp_score = validate_reading(val * 50, 'temp')  # maps to 0-50 scale
        pressure_score = validate_reading(val * 10 + 1000, 'pressure')
        humidity_score = validate_reading(val * 40, 'humidity')
        vibration_score = validate_reading(val * 8, 'vibration')
        
        total_score = temp_score + pressure_score + humidity_score + vibration_score
        
        # Critical condition buried in nesting
        if total_score >= 3:
            category = 'A' if val > 0.65 else ('B' if val > 0.45 else 'C')
            
            # Actual key computation
            if category == 'B':
                adjustment = thresholds['B'] * 100  # from map
                adjusted_val = int((val * 100) + adjustment)
                if adjusted_val % 2 == 0:
                    results.append(adjusted_val // 2)
                else:
                    results.append((adjusted_val + 1) // 2)
            elif category == 'A':
                # Dead branch - never contributes to final result due to input distribution
                results.append(int(val * 10))
            else:
                results.append(0)
        else:
            # Low score path - ignored in final analysis
            continue
    
    # Final aggregation using list comprehension (key step)
    filtered_results = [x for x in results if x > 10]
    return sum(filtered_results) + len(filtered_results)

# Irrelevant global tracking variables
current_session_id = 'DIAG_8842'
last_updated = '2023-11-05T14:22:30Z'
active_sensors = set(['temp', 'pressure'])

# Execution flow
raw_diagnostics = generate_synthetic_readings(12)
processed_data = preprocess_readings(raw_diagnostics)
threshold_map = build_threshold_map(device_profiles)

# Key assignment statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")