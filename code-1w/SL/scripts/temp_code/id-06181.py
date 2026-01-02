def analyze_component_health(reading, threshold=75, penalty_factor=0.8):
    if reading > threshold:
        return reading * 1.1
    else:
        return max(reading * penalty_factor, 10)

# Irrelevant sensor calibration data (distractor)
calibration_offset = 3.14159
temp_buffer = [0] * 100
sample_rate = 44100

# Simulated system metrics from various subsystems
raw_metrics = [68, 82, 74, 90, 65]

# Misleading transformation (dead path)
processed_data = [x ** 0.5 for x in temp_buffer if x > 50]

# Actual relevant processing begins here
metrics = [analyze_component_health(val) for val in raw_metrics]

# Weight configuration for performance aggregation
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Decoy function that is never called
def compute_stress_index(values, exponent=2):
    return sum(v ** exponent for v in values if v > 80) / len(values)

# Auxiliary calculation with plausible but unused intermediate result
baseline_avg = sum(raw_metrics) / len(raw_metrics)
adjustment_curve = [round((i + 1) * 0.7, 2) for i in range(len(metrics))]

# Red herring: fake normalization
normalized_fake = [m / 100 for m in metrics if m > 70]

# Core logic disguised among distractors
def aggregate_performance(measures, importance_weights):
    weighted_sum = 0.0
    for i in range(len(measures)):
        contribution = measures[i] * importance_weights[i]
        weighted_sum += contribution
        
        # Introduce side computation that looks important
        if i % 2 == 0:
            weighted_sum -= 0.5  # minor correction factor
        
        # Extra distraction: simulate diagnostic trace
        debug_flag = False
        if debug_flag:
            print(f'Step {i}: added {contribution}')
    
    # Final adjustment based on pattern presence
    high_performers = [m for m in measures if m >= 80]
    if len(high_performers) >= 2:
        weighted_sum += 5.0
    
    return round(weighted_sum, 4)

# Additional irrelevant variables
diagnostic_log = {}
heartbeat_interval = 1000
data_checksum = 0

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Output required format
print(f"Result: {final_score}")