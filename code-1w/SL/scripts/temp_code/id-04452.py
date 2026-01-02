from itertools import compress, count
import math

# Sensor simulation and diagnostic system for environmental monitoring
base_signals = [0.3, 0.7, 1.2, 1.8, 2.1, 2.5, 3.0, 3.4, 3.9, 4.2]
sample_timestamps = list(count(1000, step=5))

# Irrelevant auxiliary data (distractor)
event_log = {'start': 1000, 'calibration': 1015, 'reset': 1030}
baseline_offset = 0.15
dummy_weights = [0.9, 0.85, 0.8, 0.75, 0.7]

# Simulate noisy sensor readings (relevant)
raw_readings = [round(math.sin(x) + 0.2 * math.cos(2*x) + 0.05, 3) for x in base_signals]

# Misleading transformation chain (red herring)
transformed = []
for val in raw_readings:
    temp = val * 1.1
    if temp > 1.0:
        temp = math.sqrt(temp)
    transformed.append(round(temp, 3))

# Decoy function that's defined but not used in critical path
def analyze_trend(data, window=3):
    trends = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        trends.append(round(window_avg, 3))
    return trends

# Another decoy: complex but unused weighting
weighted_mask = [math.exp(-i*0.1) for i in range(len(raw_readings))]
weighted_sum = sum(a*b for a, b in zip(raw_readings, weighted_mask))

# Real signal processing begins here
valid_range = lambda x: 0.4 <= x <= 0.8
filtered_data = list(compress(raw_readings, [valid_range(x) for x in raw_readings]))

def generate_threshold_engine(bias=0.05):
    # Nested function with distraction
    adjustment_counter = [0]
    
    def adjust(x):
        adjustment_counter[0] += 1
        return x + bias if x < 0.6 else x - bias
    
    def engine(val):
        if val < 0.5:
            return adjust(val) > 0.52
        else:
            return adjust(val) > 0.58
    
    return engine, adjustment_counter

# Create threshold function
threshold_func, counter_ref = generate_threshold_engine(0.07)

# Dead code path - never executed (distraction)
if len(dummy_weights) > 10:
    fallback_data = [x * 1.5 for x in filtered_data]
else:
    debug_snapshot = filtered_data.copy()  # Used only for inspection

# Core logic with early termination pattern
intermediate_scores = []
for reading in filtered_data:
    score = 0
    if reading < 0.55:
        score += int((reading + 0.1) * 100)
        if score > 60:
            break  # Early exit possibility
    elif reading < 0.65:
        score += int(reading * 90)
    else:
        score += int((reading - 0.05) * 85)
    intermediate_scores.append(score)

# Critical red herring: complex-looking but irrelevant bitwise calc
obfuscation_key = 0
for i in range(len(base_signals)):
    obfuscation_key ^= int(base_signals[i] * 10) & 7

# Actual diagnostic processor (key function)
def process_readings(readings, threshold_fn):
    if not readings:
        return -1
    
    # Lambda-based dynamic scoring (required feature)
    scaler = lambda x: round(x * 123.45, 2)
    scaled_values = [scaler(x) for x in readings]
    
    # Determine activation based on threshold function
    activations = [threshold_fn(x) for x in readings]
    
    # Mix of relevant and irrelevant aggregations
    sum_active = sum(scaled_values[i] for i in range(len(scaled_values)) if activations[i])
    sum_inactive = sum(scaled_values[i] for i in range(len(scaled_values)) if not activations[i])
    
    # Final computation - only this matters
    result = int(sum_active - sum_inactive)
    
    # Distracting secondary calculations
    avg_spread = (sum_active / len(scaled_values)) if scaled_values else 0
    entropy_proxy = -sum(math.log(abs(x)+1e-8) for x in scaled_values)  # Unused
    
    return result

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_func)

# Output requirement
print(f"Result: {final_diagnostic}")