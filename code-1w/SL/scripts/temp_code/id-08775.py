from collections import defaultdict, Counter

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 130, 90, 200, 180, 160, 110]
node_loads = [0.65, 0.82, 0.47, 0.93, 0.71, 0.68, 0.88, 0.55]
packet_loss_rates = [0.002, 0.005, 0.001, 0.015, 0.003, 0.004, 0.012, 0.002]

# Irrelevant telemetry data (distractor)
temperature_readings = [23.5, 25.1, 22.8, 26.3, 24.0, 23.9, 25.7, 22.4]  # CPU temps (unused)
humidity_levels = [45, 48, 53, 41, 47, 46, 49, 50]  # ambient humidity (unused)

# Misleading intermediate computations (red herring)
avg_temp = sum(temperature_readings) / len(temperature_readings)
highest_humidity = max(humidity_levels)
deviation_index = sum(abs(t - avg_temp) for t in temperature_readings)

# Data aggregation using defaultdict (relevant but indirect)
metrics = defaultdict(float)
metrics['total_duration'] = sum(task_durations)
metrics['avg_load'] = sum(node_loads) / len(node_loads)
metrics['max_loss'] = max(packet_loss_rates)
metrics['stability_ratio'] = len([x for x in packet_loss_rates if x < 0.01]) / len(packet_loss_rates)

# Decoy function that looks important but is unused
def calculate_thermal_efficiency(readings):
    return sum(r ** 0.8 for r in readings) / len(readings)

# Another decoy: complex transformation with no impact
class PerformanceModel:
    def __init__(self, data):
        self.data = data
        self.baseline = sum(data) / len(data)
    
    def predict_anomaly(self):
        return [x > self.baseline * 1.5 for x in self.data]

model = PerformanceModel(task_durations)
anomalies = model.predict_anomaly()  # Computed but unused

# Bit manipulation red herring (irrelevant to final result)
encoded_signature = 0
for i, dur in enumerate(task_durations):
    encoded_signature ^= (dur << 1) | (i & 1)

# Weight assignments (some are misleading)
weights = {}
weights['total_duration'] = 0.3
weights['avg_load'] = 0.25
weights['max_loss'] = 0.35
weights['stability_ratio'] = 0.1
# Unused weight (distractor)
weights['thermal_factor'] = 0.0  # Never applied

# Conditional expression with nested logic (core relevant part)
def evaluate_performance(met, w):
    base_score = 0.0
    for key in w:
        if key not in met:
            continue
        contribution = 0.0
        
        if key == 'total_duration':
            # Inverse scoring: lower duration → higher score
            normalized = max(0, (300 - met[key]) / 100)
            contribution = normalized * w[key]
        elif key == 'avg_load':
            # Optimal load is ~0.7; penalize extremes
            deviation = abs(met[key] - 0.7)
            normalized = max(0, (0.3 - deviation) / 0.3)
            contribution = normalized * w[key]
        elif key == 'max_loss':
            # Lower loss is better
            normalized = max(0, (0.02 - met[key]) / 0.02)
            contribution = normalized * w[key]
        elif key == 'stability_ratio':
            # Higher ratio is better
            contribution = met[key] * w[key]
        
        base_score += contribution
    
    # Final nonlinear adjustment
    adjusted_score = (base_score ** 1.2) * 100
    
    # Dead code branch (misleading)
    if base_score > 100:  # Impossible due to normalization
        adjusted_score = 100 + (base_score - 100) / 2
    
    return int(round(adjusted_score))

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Output the target result
print(f"Target result: {final_score}")