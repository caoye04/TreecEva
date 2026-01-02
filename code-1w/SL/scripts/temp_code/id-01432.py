from collections import defaultdict, Counter
import math

# Simulated system metrics for a distributed processing node
task_load = [120, 150, 130, 180, 90, 200, 140, 160]
error_rates = [0.01, 0.03, 0.02, 0.05, 0.01, 0.07, 0.04, 0.06]
response_times = [230, 210, 250, 300, 190, 320, 240, 280]

# Irrelevant telemetry data (distractor)
telemetry_log = {
    'cpu_temp': [68, 70, 72, 75, 73, 77, 76, 74],
    'fan_speed': [2000, 2100, 2200, 2400, 2300, 2500, 2450, 2350],
    'power_draw': [85.3, 87.1, 89.4, 92.7, 90.2, 95.6, 93.8, 91.9]
}

# Baseline thresholds (used later)
baseline = {
    'load_threshold': 140,
    'error_tolerable': 0.04,
    'response_limit': 250
}

# Distractor function - appears useful but unused in final calculation
def analyze_telemetry(log):
    avg_temp = sum(log['cpu_temp']) / len(log['cpu_temp'])
    max_speed = max(log['fan_speed'])
    return avg_temp * max_speed // 100

# Secondary distractor: dead code path
class PerformanceMonitor:
    def __init__(self, data):
        self.raw = data
        self.stats = defaultdict(float)
    
    def compute_health(self):
        # This is never called
        self.stats['health'] = sum(self.raw) / len(self.raw) * 0.9
        return self.stats['health']

# Auxiliary function with partial relevance
def calculate_efficiency(tasks, times):
    total_task_units = sum(tasks)
    total_time = sum(times)
    efficiency = total_task_units / (total_time + 1e-9)
    return efficiency * 100

# Misleading intermediate metric (red herring)
efficiency_score = calculate_efficiency(task_load, response_times)
projected_yield = efficiency_score * 1.23  # Looks important, but not used

# Core logic: assess each metric against baseline
def evaluate_dimension(data, threshold, weight, reverse=False):
    count_above = 0
    for val in data:
        if reverse:
            count_above += 1 if val < threshold else 0
        else:
            count_above += 1 if val > threshold else 0
    return count_above * weight

# Another red herring: complex but unused statistical transform
def entropy_based_weight(vector):
    counts = Counter(vector)
    total = len(vector)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log(p)
    return round(entropy, 3)

# Weights derived from domain knowledge (some are decoys)
decoy_weights = {
    'w1': entropy_based_weight(task_load),
    'w2': entropy_based_weight(error_rates),
    'w3': 1.7  # Arbitrary
}

# Primary evaluation function
metrics = {
    'high_load_count': evaluate_dimension(task_load, baseline['load_threshold'], 1.0),
    'excess_error_count': evaluate_dimension(error_rates, baseline['error_tolerable'], 2.5),
    'slow_response_count': evaluate_dimension(response_times, baseline['response_limit'], 1.8)
}

# Simulate conditional degradation adjustment
if metrics['high_load_count'] > 4:
    metrics['degradation_factor'] = 1.5
else:
    metrics['degradation_factor'] = 1.0

# Introduce fake compensation mechanism (distractor)
compensation_pool = 0
for i in range(len(task_load)):
    if error_rates[i] > 0.05 and response_times[i] > 300:
        compensation_pool += 5

# Real scoring logic hidden among noise
def evaluate_performance(met, base):
    load_penalty = met['high_load_count'] * 8
    error_penalty = met['excess_error_count'] * 12
    speed_penalty = met['slow_response_count'] * 10
    factor = met.get('degradation_factor', 1.0)
    
    # Base score before penalties
    base_score = 1000
    total_penalty = (load_penalty + error_penalty + speed_penalty) * factor
    
    # Apply penalty decay for small deviations (advanced logic)
    if met['high_load_count'] < 3:
        total_penalty *= 0.85
    if met['excess_error_count'] == 0:
        total_penalty *= 0.9
    
    # Final score computation
    final = base_score - total_penalty
    
    # Irrelevant rounding based on unused telemetry
    # fake_round = int(telemetry_log['power_draw'][0]) % 7
    # final = round(final / fake_round) * fake_round
    
    return final

# Execute key statement
temp_monitor = PerformanceMonitor(task_load)  # Object created but not used
unused_result = analyze_telemetry(telemetry_log)  # Dead call
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")