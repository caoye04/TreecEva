import math

# Simulated sensor data processing pipeline for environmental monitoring station
def analyze_temperature(raw_readings):
    adjusted = [r * 1.02 + 0.5 for r in raw_readings]
    filtered = [t for t in adjusted if 15 <= t <= 45]
    return sum(filtered) / len(filtered) if filtered else 0

def compute_humidity_index(sequence):
    base = sum(sequence) / len(sequence)
    deviation = math.sqrt(sum((x - base) ** 2 for x in sequence) / len(sequence))
    return base * (1 + deviation / 100)

def detect_anomaly_pattern(values):
    # Irrelevant recursive anomaly detector (dead-end logic)
    def recurse_check(data, threshold):
        if len(data) < 2:
            return False
        if abs(data[1] - data[0]) > threshold:
            return True
        return recurse_check(data[1:], threshold - 1)
    return recurse_check(values, 10)

def deprecated_calculate_windspeed_factor(data):
    # Unused function - red herring
    factor = 1.0
    for d in sorted(data, reverse=True):
        if d > 20:
            factor *= 1.1
    return round(factor, 2)

def normalize_pressure(readings):
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5 for _ in readings]
    return [(r - min_val) / (max_val - min_val) for r in readings]

def calculate_altitude_bias(pressure_norm):
    total = 0
    for p in pressure_norm:
        if p > 0.7:
            total += math.log(p) * 100
        elif p > 0.3:
            total += math.sin(p * math.pi) * 50
        else:
            total += math.cos(p * math.pi) * 30
    return int(total // len(pressure_norm))

# Distractor: fake calibration chain
last_calibration_checksum = 0
for i in range(5):
    last_calibration_checksum ^= (i * 137) % 97

# Sensor fusion metric generator
generate_weight_map = lambda sizes: {i: (s ** 0.5) for i, s in enumerate(sizes)}

# Main evaluation logic
raw_temp_data = [23.1, 24.6, 19.8, 45.2, 17.3, 22.0, 26.5]
humidity_sequence = [48, 52, 55, 44, 60, 53, 49]
pressure_readings = [980, 975, 990, 960, 985, 970, 955]
wind_vector = [12, 18, 15, 22, 14, 20, 16]

avg_temp = analyze_temperature(raw_temp_data)
humidity_index = compute_humidity_index(humidity_sequence)
normalized_pressure = normalize_pressure(pressure_readings)
altitude_correction = calculate_altitude_bias(normalized_pressure)

# Fake intermediate metrics (distraction)
consistency_score = 0
for w in wind_vector:
    if w % 2 == 0:
        consistency_score += 1
consistency_score = (consistency_score / len(wind_vector)) * 100

# Weight mapping based on channel stability (real use of lambda)
channel_stability = [0.91, 0.88, 0.95, 0.70, 0.82, 0.85, 0.78]
weights = generate_weight_map(channel_stability)

total_weighted_value = 0
weight_sum = 0
for i, w in weights.items():
    if channel_stability[i] > 0.8:
        total_weighted_value += w * (humidity_sequence[i] + raw_temp_data[i])
        weight_sum += w

fusion_metric = total_weighted_value / weight_sum if weight_sum else 0

# Misleading short-circuit evaluation chain
sensor_reliability_flag = (len(raw_temp_data) > 5) and (max(raw_temp_data) < 50) or detect_anomaly_pattern(wind_vector)

# Final performance metric set
metric_set = {
    'thermal': avg_temp,
    'humidity_factor': humidity_index,
    'fusion': fusion_metric,
    'altitude_bias': altitude_correction,
    'reliability': 1 if sensor_reliability_flag else 0
}

# Core answer computation path
threshold_filter = lambda x: 1 if x > 0 else 0

# Evaluate performance using weighted combination
def evaluate_performance(metrics):
    # Multiple layers of logic masking the key calculation
    base_score = metrics['thermal'] * 2.1
    bonus = 0
    
    if metrics['humidity_factor'] > 50:
        bonus += 15
    
    # Nested conditional with distractors
    if metrics['fusion'] > 70:
        adjustment = metrics['fusion'] / 10
        if metrics['altitude_bias'] > 0:
            adjustment -= metrics['altitude_bias'] / 5
        bonus += int(adjustment)
    else:
        # Dead branch - never executed due to data
        bonus -= 10
    
    # Critical interference: redundant but similar-looking computations
    temp_debug_value = 0
    for i in range(3):
        temp_debug_value += (i + 1) * 17
    temp_debug_value = temp_debug_value % 11  # Irrelevant modulo
    
    # Decoy assignment
    final_calculation_trace = []
    for step in ['init', 'scale', 'adjust', 'finalize']:
        final_calculation_trace.append(hash(step) % 100)
    
    # Real score assembly
    raw_score = base_score + bonus + (metrics['reliability'] * 10)
    
    # Final transformation
    if raw_score > 100:
        raw_score = raw_score * 0.95 + 5
    
    # Key rounding behavior
    return int(round(raw_score))

# Execution point of interest
final_score = evaluate_performance(metric_set)

# Output result as required
print(f"Result: {final_score}")