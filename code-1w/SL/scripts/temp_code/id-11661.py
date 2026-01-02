from collections import defaultdict
import math

# Simulated sensor data aggregation (irrelevant but plausible)
sensor_cache = defaultdict(list)
for i in range(5):
    sensor_cache[f'sensor_{i}'].extend([i*2 + j for j in range(3)])

# Core system: Health metric analyzer with red herrings
def analyze_risk_level(value, baseline):
    return abs(value - baseline) > 15

# Distractor function: Unused in final flow
def legacy_calculate_stress(data):
    stress = 0
    for x in data:
        if x % 3 == 0:
            stress += math.log(x + 1)
    return stress

# Real processing function
def compute_deviation_score(sequence, weight_factor):
    mean_val = sum(sequence) / len(sequence)
    variance = sum((x - mean_val)**2 for x in sequence) / len(sequence)
    return round(math.sqrt(variance) * weight_factor, 4)

# Misleading normalization path (never called)
normalization_map = {k: v**0.5 for k, v in enumerate(range(10, 20))}

def adjust_for_bias(arr, correction):
    return [x * correction if x > 0 else x for x in arr]

# Key data structures
raw_readings = [88, 92, 76, 85, 103, 64, 91]

# Irrelevant transformation chain
temp_analysis = list(map(lambda x: (x + 5) // 2, raw_readings))
decay_weights = [0.8**i for i in range(len(temp_analysis))]
weighted_temp = [a*b for a, b in zip(temp_analysis, decay_weights)]

# Real signal extraction
signal_peaks = [x for x in raw_readings if x > 80]
noise_floor = min(raw_readings) + 10
valid_signals = list(filter(lambda x: x > noise_floor, signal_peaks))

# Decoy state variables
current_mode = 'diagnostic'
override_flag = False
emergency_threshold = 999
buffer_state = (0, 0, 0)

# Complex conditional mask (partially used)
mask_flags = [
    len(valid_signals) > 3,
    sum(valid_signals) % 7 == 0,
    any(x < 75 for x in raw_readings),
    all(x > 50 for x in raw_readings)
]

# Red herring: Bit manipulation with no impact
diagnostic_key = 0xABCD
for val in raw_readings[:4]:
    diagnostic_key ^= (val << 2)
diagnostic_key &= 0xFFFF

# Actual computation begins here
baseline_template = (70, 85, 90)
active_range = raw_readings[1:6]  # Critical slice

# Tuple unpacking with distraction
primary, secondary = active_range[0], active_range[-1]
third = active_range[len(active_range)//2]

# Multi-step derivation
aggregate = primary + secondary * 2 - third
scaling_factor = 0.25 if aggregate > 200 else 0.4
interim_score = compute_deviation_score(active_range, scaling_factor)

# Control flow with dead branch
if interim_score < 10:
    adjustment = math.sin(interim_score)
elif interim_score > 15:
    adjustment = math.cos(interim_score)
else:
    adjustment = 0.7  # This branch taken

refined_score = interim_score * adjustment

# Threshold policy map (distractor structure)
policy_registry = {
    'strict': lambda x: x < 5,
    'balanced': lambda x: 5 <= x <= 12,
    'lenient': lambda x: x > 12
}

# Main configuration
evaluation_matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

thresholds = {
    'critical': 18.5,
    'warning': 12.0,
    'normal': 5.0
}

health_data = {
    'metrics': raw_readings,
    'profile': 'standard',
    'version': '2.1b'
}

# Central processing with decoy complexity
def process_metrics(data, config):
    metrics = data['metrics']
    window = metrics[2:5]
    
    # Spurious nested function
    def validate_segment(seg):
        return all(isinstance(x, int) and x >= 0 for x in seg)
    
    if not validate_segment(window):
        return -1
    
    # Real logic buried in distractions
    a, b, c = window
    temp_result = (a ^ b) | (c << 1)  # Bitwise red herring
    temp_result %= 100
    
    # Actual relevant calculation
    mean_win = (a + b + c) / 3
    deviation = abs(mean_win - config['warning'])
    
    # Conditional mutation
    if deviation > 10:
        multiplier = 2.1
    elif deviation > 5:
        multiplier = 1.6
    else:
        multiplier = 0.9  # This path taken
    
    # Final composition
    score_base = compute_deviation_score(metrics, 0.3)
    enhancement = len([x for x in metrics if x > 85])
    final_value = (score_base * multiplier) + enhancement
    
    # Last-minute adjustment based on tuple condition
    flag_state = (len(metrics) > 5, mean_win > 80, enhancement >= 2)
    if all(flag_state) or flag_state.count(True) == 2:
        final_value *= 1.1
    
    return round(final_value, 4)

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")