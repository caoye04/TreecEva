from collections import defaultdict

# Simulated system performance evaluation with distractors
def analyze_component_health(temps, thresholds):
    alert_count = 0
    for sensor_id, temp in temps.items():
        if temp > thresholds.get(sensor_id, 90):
            alert_count += 1
    return alert_count  # Red herring: not used later

# Irrelevant data transformation (dead path)
def transform_data(values):
    return [v ** 0.5 for v in values if v > 0]

# Core logic disguised among distractions
def compute_efficiency_rating(inputs, outputs):
    total_in = sum(inputs)
    total_out = sum(outputs)
    if total_in == 0:
        return 0.0
    return (total_out / total_in) * 100

# Distractor function - looks important but unused
def calculate_latency_benchmark(events):
    timestamps = sorted(events)
    gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    return sum(gaps) / len(gaps) if gaps else 0

# Another red herring: complex but unused structure
class PerformanceTracker:
    def __init__(self):
        self.history = []
        self.max_recorded = 0
    
    def update(self, value):
        self.history.append(value)
        if value > self.max_recorded:
            self.max_recorded = value

# Bit manipulation decoy (seems relevant but isn't)
def obfuscate_key(n):
    n = ((n << 3) & 0xff) | (n >> 5)
    n ^= 0b10101010
    n = (n + 17) % 256
    return n

# Main evaluation logic buried in noise
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    efficiency = compute_efficiency_rating(metrics['inputs'], metrics['outputs'])
    stability = metrics['stability_factor']
    redundancy = metrics['redundancy_level']
    
    # Real computation chain
    base_score = efficiency * 0.6 + stability * 0.3 + redundancy * 0.1
    
    # Conditional adjustment (key branch)
    if stability > 85:
        base_score *= 1.15
    elif stability < 60:
        base_score *= 0.85
    
    # Apply weights through lambda (required feature)
    adjuster = lambda x, w: x * w
    final_components = [
        adjuster(base_score, weights['base']),
        adjuster(metrics['consistency'], weights['bonus'])
    ]
    
    # Final aggregation
    result = sum(final_components)
    
    # Distractor: unused intermediate
    normalized = result / max(final_components)
    
    return int(round(result))

# Setup phase with multiple irrelevant variables
sensor_temperatures = {f'sensor_{i}': 75 + i*3 for i in range(12)}
temperature_thresholds = defaultdict(lambda: 90)
for s in ['sensor_3', 'sensor_7']: temperature_thresholds[s] = 80

# Unused event simulation (misleading)
event_log = [100, 105, 112, 118, 125]
latency_metric = calculate_latency_benchmark(event_log)

# Key data structures
metrics = {
    'inputs': [120, 135, 142, 138],
    'outputs': [98, 112, 118, 115],
    'stability_factor': 88,
    'redundancy_level': 76,
    'consistency': 23
}

weights = {
    'base': 0.7,
    'bonus': 0.3
}

# Dead code path invocation (distraction)
tracker = PerformanceTracker()
for val in [45, 67, 88, 76]:
    tracker.update(val)

# Irrelevant transformation
transformed_inputs = transform_data(metrics['inputs'])

# Core execution point
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")