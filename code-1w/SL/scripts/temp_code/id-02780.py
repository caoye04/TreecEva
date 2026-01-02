import math

# Simulated sensor data and system telemetry
temperature_readings = [72.1, 73.5, 74.0, 71.8, 75.3, 76.0, 73.9]
pressure_levels = [1013.25, 1012.8, 1014.1, 1011.9, 1013.0]
humidity_data = [45, 47, 50, 44, 52, 48]

# Irrelevant calibration constants (distractors)
CALIBRATION_OFFSET_A = 0.0012
CALIBRATION_OFFSET_B = -0.0008
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256

# System state variables
system_load = sum([i * 0.77 for i in range(1, 11)])
uptime_hours = 142
maintenance_cycle = False

# Complex preprocessing pipeline
smoothed_temp = list(map(lambda x: round(x * 1.02 - 0.35, 2), temperature_readings))
adjusted_pressure = [round(p * (1 + 0.00012 * (t - 72)), 2) 
                   for p, t in zip(pressure_levels, temperature_readings)]

# Checksum decoy function (never used)
def compute_checksum(data):
    chk = 0
    for d in data:
        chk ^= int(d * 100) & 0xFF
    return chk

# Auxiliary transformation (looks important but unused)
effective_humidity = [min(max(h * 1.1 - 5, 0), 100) for h in humidity_data]

# Core diagnostic signature generator (key logic)
def generate_signature(temp, hum):
    base = (temp[0] + temp[-1]) / 2
    variation = max(temp) - min(temp)
    trend = sum(temp[i] < temp[i+1] for i in range(len(temp)-1))
    return round(base * 100 + variation * 10 + trend, 4)

# Health scoring with red herring parameters
HEALTH_WEIGHT_A = 0.67
HEALTH_WEIGHT_B = 0.33
DECOY_THRESHOLD = 85.5

# Another unused diagnostic path (dead code)
def legacy_diagnostic(pressure):
    avg_p = sum(pressure) / len(pressure)
    if avg_p < 1012.0:
        return 'WARNING'
    else:
        return 'STABLE'

# Recursive feature extractor (used in critical path)
def extract_features(data, depth=0):
    if depth >= 3 or len(data) <= 1:
        return data[0] if data else 0
    split_idx = len(data) // 2
    left = extract_features(data[:split_idx], depth + 1)
    right = extract_features(data[split_idx:], depth + 1)
    return round((left + right) / 2.0 + depth * 0.1, 3)

# Key health signature derived from temperature trends
health_signature = generate_signature(smoothed_temp, humidity_data)

# Misleading intermediate metrics (distractors)
criticality_index = (max(smoothed_temp) - 70) * 3.2
stability_score = 100 - abs(criticality_index) * 0.8

# Decoy state machine
state_transitions = {
    'idle': 'monitoring',
    'monitoring': 'diagnosing',
    'diagnosing': 'idle'
}
current_state = 'idle'
for _ in range(int(min(smoothed_temp))):
    current_state = state_transitions.get(current_state, 'idle')

# Primary processing function with embedded lambda and recursion
def process_metrics(signature, load):
    # Nested helper with distractor logic
    def normalize(value, min_val, max_val):
        return (value - min_val) / (max_val - min_val) if max_val != min_val else 0
    
    # Bit manipulation decoy
    fingerprint = int(signature * 100) ^ int(load)
    fingerprint = (fingerprint << 3) | (fingerprint >> 5)
    
    # Real computation hidden among distractions
    feature_1 = extract_features([signature, load, system_load])
    feature_2 = math.log(abs(signature) + 1) * 50
    
    # Weighted combination using lambda
    aggregator = lambda a, b: (a * 0.7 + b * 0.3) if a > b else (a * 0.4 + b * 0.6)
    
    # Intermediate blend
    raw_blend = aggregator(feature_1, feature_2)
    
    # Final adjustment based on uptime (irrelevant but plausible)
    adjustment_factor = (uptime_hours % 24) / 100.0
    
    # ACTUAL ANSWER COMPUTATION (non-obvious)
    result = round(raw_blend - adjustment_factor + 17.3, 4)
    
    # Dead code block (misleading)
    if result > 100:
        post_process = result / 1.5
        return round(post_process, 4)
    
    return result

# Critical assignment statement
final_diagnostic = process_metrics(health_signature, system_load)

# Output the target result
print(f"Target result: {final_diagnostic}")