from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (irrelevant preprocessing)
sensor_logs = [
    {'id': 'A7', 'values': [0.8, 0.9, 1.1, 1.3], 'type': 'temp'},
    {'id': 'B4', 'values': [0.6, 0.4, 0.5], 'type': 'pressure'},
    {'id': 'A7', 'values': [1.0, 1.2], 'type': 'temp'}
]

aggregated = defaultdict(list)
for log in sensor_logs:
    aggregated[log['id']].extend(log['values'])

averages = {k: sum(v) / len(v) for k, v in aggregated.items()}
scaling_factor = 2.1  # unused scaling hint (red herring)

# Irrelevant statistical analysis (dead path)
def analyze_trend(data, mode='linear'):
    if mode == 'fourier':
        return sum(math.sin(x) for x in data)  # never used
    return sum(x * i for i, x in enumerate(data))  # distracting logic

# Core diagnostic system
baseline_readings = [0.85, 0.92, 0.78, 0.96, 0.81]
thresholds = {
    'warning': 0.88,
    'critical': 0.95
}

# Misleading transformation chain
temp_cache = [x ** 2 for x in baseline_readings if x > 0.8]
filtered = list(filter(lambda x: x < 1.0, temp_cache))
shifted = [round(x + 0.1, 2) for x in filtered]  # looks important, not used later

# Real processing begins here
health_data = [round(math.log(x), 3) for x in baseline_readings]

# Bit manipulation decoy
defect_flag = 0b1010 ^ 0b1100 & 0b1111  # XOR/AND red herring
parity_check = bin(defect_flag).count('1') % 2  # irrelevant

# Conditional expression web
diagnostic_levels = [
    'normal' if val < thresholds['warning'] else
    'elevated' if val < thresholds['critical'] else
    'critical'
    for val in health_data
]

classification_count = Counter(diagnostic_levels)

# Data structure cross-reference distraction
data_map = defaultdict(dict)
for i, val in enumerate(health_data):
    data_map[i]['raw'] = baseline_readings[i]
    data_map[i]['log_val'] = val
    data_map[i]['category'] = diagnostic_levels[i]
    if val > 0.9:
        data_map[i]['flag'] = (1 << 3) | 2  # bitfield decoy

# Unused recursive function (distractor)
def compute_stability_index(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = compute_stability_index(n-1) + compute_stability_index(n-2)
    return cache[n]

# Main metric processor (key function)
def process_metrics(readings, limits):
    avg_log = sum(readings) / len(readings)
    
    # Composite score with fake components
    stability = len([x for x in readings if x > limits['warning']])
    volatility = sum(1 for x in readings if x > avg_log)  # misleading term
    
    # Critical calculation buried in logic
    if stability > 2:
        base_score = avg_log * 1000
    else:
        base_score = avg_log * 500
    
    # Hidden adjustment via slicing and lambda
    adjustments = list(map(lambda x: x * 0.1, readings[:3]))
    net_adjustment = sum(adjustments) * 100
    
    # Final computation
    result = base_score + net_adjustment
    
    # Dead comparison (misleads about branching)
    if result > 1000 and parity_check:  # parity_check always 0
        result -= 50
        
    return round(result, 4)

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)

# Print required output
print(f"Target result: {final_diagnostic}")