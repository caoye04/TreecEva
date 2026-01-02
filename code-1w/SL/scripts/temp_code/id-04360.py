import math

def analyze_component_health(raw_readings, tolerance_level):
    # Irrelevant transformation (dead-end function)
    adjusted = [x * 0.98 + 2 for x in raw_readings]
    normalized = [max(0, math.log(x) - tolerance_level) for x in adjusted]
    return sum(normalized) // len(normalized)


def generate_simulation_data(size):
    # Distractor function: generates unused data
    return [i ** 2 % 17 for i in range(size)]

# Unused but plausible-looking constants
CALIBRATION_FACTOR = 0.857
REFERENCE_BASELINE = 42.0
MAX_BUFFER_CAPACITY = 1024

# System metrics with realistic naming
log_entries = {
    'node_01': {'load': 85, 'temp': 67, 'errors': 3},
    'node_02': {'load': 92, 'temp': 73, 'errors': 7},
    'node_03': {'load': 76, 'temp': 61, 'errors': 1},
    'node_04': {'load': 89, 'temp': 70, 'errors': 5}
}

system_thresholds = {
    'critical_load': 90,
    'overheat_temp': 75,
    'error_spike': 5,
    'weighting': {'load': 0.5, 'temp': 0.3, 'errors': 0.2}
}

# Misleading intermediate calculations
aggregated_stats = []
for node, metrics in log_entries.items():
    score = 0
    if metrics['load'] > system_thresholds['critical_load']:
        score += 3
    if metrics['temp'] > system_thresholds['overheat_temp']:
        score += 2
    if metrics['errors'] >= system_thresholds['error_spike']:
        score += 2
    aggregated_stats.append(score)

# Dead code path — looks important but unused
consensus_rating = sum(aggregated_stats) / len(aggregated_stats) if aggregated_stats else 0

# Unused simulation data generation
simulated_loads = generate_simulation_data(50)

# Real processing begins here — nested and interdependent logic
primary_weights = system_thresholds['weighting']
diagnostic_vector = []

for node_id, readings in log_entries.items():
    weighted_value = 0
    # Load component: scaled by inverse exponential decay
    if readings['load'] > 0:
        load_score = readings['load'] * primary_weights['load']
        temp_factor = readings['temp'] / (readings['temp'] - 20) if readings['temp'] > 20 else 1
        weighted_value += load_score * temp_factor
    
    # Error penalty: quadratic impact above threshold
    if readings['errors'] > system_thresholds['error_spike']:
        excess = readings['errors'] - system_thresholds['error_spike']
        weighted_value += excess ** 2 * 10
    
    # Conditional override for specific node (red herring logic)
    if node_id == 'node_01':
        weighted_value = max(weighted_value, 50)  # Looks like correction, but not decisive
    
    diagnostic_vector.append(weighted_value)

# Secondary transformation with dictionary operations
transformed_diagnostics = {f'd_{i}': round(val, 2) for i, val in enumerate(diagnostic_vector)}

# Accumulate final metric through multiple steps
running_total = 0
scaling_modifier = 1.0

for key, value in transformed_diagnostics.items():
    if 'd_' in key:
        idx = int(key[2:])
        if idx % 2 == 0:
            running_total += value * 0.9
        else:
            # Apply modular adjustment
            running_total += (value * 1.1) % 89

# Additional interference: unused recursive function
def compute_residual(n):
    if n <= 1:
        return 1
    return compute_residual(n-1) + compute_residual(n-2)

# Final computation chain
baseline_shift = math.floor(running_total / 4)

# Integer division and rounding combination
intermediate_result = running_total // 3
adjusted_result = round(intermediate_result + (running_total % 3), 1)

# Key statement
final_diagnostic = int((adjusted_result - baseline_shift) * 2)

# Print result as required
print(f"Target result: {final_diagnostic}")