import itertools

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.013
CALIBRATION_C = 2.45  # Unused in logic
OFFSET_X = -0.5   # Unused
OFFSET_Y = 0.3    # Unused

# Simulated raw sensor readings (temperature, pressure, vibration)
raw_readings = [
    (23.4, 101.3, 0.012),
    (22.9, 102.1, 0.015),
    (24.1, 100.8, 0.009),
    (23.0, 101.5, 0.011),
    (25.3, 99.7,  0.021),
    (22.7, 103.0, 0.008),
    (26.8, 98.2,  0.031),  # Anomalous reading
    (23.6, 101.9, 0.010)
]

# Irrelevant transformation function (dead code path)
def transform_coordinates(x, y):
    return (x * 0.8 + 1.2, y * 1.1 - 0.7)

# Misleading auxiliary computation (no effect on result)
baseline_avg = sum(r[0] for r in raw_readings) / len(raw_readings)
adjusted_baseline = baseline_avg * CALIBRATION_A

# Filter out high-vibration readings (> 0.02)
filtered_data = [r for r in raw_readings if r[2] <= 0.02]

# Red herring: complex-looking but unused list comprehension
decoy_aggregates = [
    (r[0] ** 2 + r[1] / 10) * CALIBRATION_B for r in raw_readings
    if r[0] > 24 and r[1] < 100
]

# Decoy function using itertools (not part of critical path)
def generate_pairs(data):
    return list(itertools.combinations(data, 2))

unused_pairs = generate_pairs([r[0] for r in filtered_data])

# Real processing begins here
vibration_sum = sum(r[2] for r in filtered_data)
pressure_min = min(r[1] for r in filtered_data)
temp_max = max(r[0] for r in filtered_data)

# Compute weighted health index
weight_vib = 0.6
weight_temp = 0.3
weight_press = 0.1

# Health degradation based on deviation
health_index = (
    (temp_max - 23.0) * weight_temp +
    (102.0 - pressure_min) * weight_press +
    (vibration_sum * 100) * weight_vib
)

# Secondary processing function
def analyze_trends(data):
    diffs = [data[i+1][0] - data[i][0] for i in range(len(data)-1)]
    smoothed = [sum(diffs[max(0, i-1):i+2]) / len(diffs[max(0, i-1):i+2]) 
                for i in range(len(diffs))]
    trend_score = sum(abs(s) for s in smoothed) * 5
    return trend_score

# Another decoy function that does nothing meaningful
def calculate_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

entropy_probe = calculate_entropy([r[2] for r in filtered_data])

# Actual core logic chain
smoothed_temp = sum(r[0] for r in filtered_data) / len(filtered_data)
scaled_vibration = vibration_sum * 1000

# Multi-step transformation with distraction variables
interim_result = (smoothed_temp * 2) + scaled_vibration
decoy_mask = 0b11010110
bit_interference = (len(filtered_data) << 3) & decoy_mask  # Looks important

# Key intermediate calculation
normalized_score = interim_result - (bit_interference * 1.5)

# Final processing with case conversion red herring
status_flags = ['OK', 'WARNING', 'ERROR']
mode_str = 'Operational'.upper()[::-1]  # Reversed string - irrelevant

# Sorting distraction
sorted_pressures = sorted([r[1] for r in filtered_data], reverse=True)
median_pressure = sorted_pressures[len(sorted_pressures)//2]

# The real final computation
def process_readings(data):
    base = normalized_score  # Depends on earlier chain
    adjustment = 0
    
    # Simple recursion to compute depth factor
    def depth_factor(n):
        if n <= 1:
            return 1
        return n * 0.7 + depth_factor(n - 1) * 0.3
    
    levels = len(data) % 4
    enhancement = depth_factor(levels) if levels > 0 else 1
    
    # Final mixing using itertools.cycle (actual usage)
    pattern = [1, -1, 2]
    cycle = itertools.cycle(pattern)
    cycle_adjust = sum(next(cycle) for _ in range(len(data)))
    
    adjustment = enhancement * cycle_adjust
    
    # Final diagnostic value
    return int(base + adjustment)

final_diagnostic = process_readings(filtered_data)

print(f"Result: {final_diagnostic}")