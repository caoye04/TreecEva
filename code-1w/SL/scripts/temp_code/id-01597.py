from itertools import combinations

# System performance evaluation under varying load conditions
def generate_load_profiles(base_load, variance):
    profiles = []
    for i in range(3):
        fluctuated = base_load + (variance * (i - 1))
        if fluctuated > 0:
            profiles.append(fluctuated)
    return profiles

# Simulate resource contention across subsystems
def compute_contention_factor(subsystems, active_count):
    max_pairs = 0
    if len(subsystems) >= 2:
        for pair in combinations(subsystems, 2):
            max_pairs += 1
    contention = max_pairs / (active_count + 1) if active_count else 0
    return round(contention, 3)

# Assess thermal efficiency based on fan speed and ambient conditions
def calculate_thermal_ratio(fan_rpm, ambient_temp):
    baseline = 3500
    temp_ratio = (ambient_temp + 25) / 25
    adjusted_rpm = baseline / fan_rpm
    efficiency = adjusted_rpm / temp_ratio
    return efficiency * 0.87

# Misleading auxiliary function - appears relevant but not used in final score
def predict_failure_rate(age_years, cycles):
    base_rate = 0.02
    degradation = (age_years * 0.015) + (cycles * 1e-5)
    return base_rate + degradation

# Core evaluation logic with combined metrics
weights = {'throughput': 0.4, 'latency': 0.3, 'power': 0.2, 'stability': 0.1}

def evaluate_performance(metrics, weights_map):
    normalized = {}
    raw_values = {
        'throughput': metrics['ops_per_sec'] * 0.001,
        'latency': 1000 / (metrics['avg_delay'] + 1),
        'power': 100 / (metrics['watts'] + 50),
        'stability': 1 - (metrics['error_rate'] / 100)
    }
    
    # Apply weighting scheme
    total_weighted = 0.0
    for key in weights_map:
        normalized[key] = min(raw_values[key], 1.5)
        total_weighted += normalized[key] * weights_map[key]
    
    # Hidden adjustment: stability cannot exceed throughput contribution
    if normalized['stability'] > normalized['throughput']:
        total_weighted -= (normalized['stability'] - normalized['throughput']) * 0.05
    
    return int(total_weighted * 100)

# Initialize system telemetry data
system_metrics = {
    'ops_per_sec': 4200,
    'avg_delay': 14,
    'watts': 180,
    'error_rate': 2.5,
    'core_count': 8,
    'clock_speed': 3.6
}

# Generate auxiliary diagnostics (distractor block)
load_scenarios = generate_load_profiles(100, 20)
average_load = sum(load_scenarios) / len(load_scenarios)
contention_level = compute_contention_factor(['cpu', 'memory', 'disk', 'gpu'], 3)
temp_efficiency = calculate_thermal_ratio(2800, 32)
failure_prediction = predict_failure_rate(3, 12500)  # Computed but unused

# Critical execution point
final_score = evaluate_performance(system_metrics, weights)

print(f"Result: {final_score}")