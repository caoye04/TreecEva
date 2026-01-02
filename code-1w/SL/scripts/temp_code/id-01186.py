from collections import defaultdict, Counter
import math

# Simulate a nuclear reactor diagnostic system with red herrings
def analyze_reactor_metrics(metrics):
    spike_count = 0
    for reading in metrics['temperature_readings']:
        if reading > 850:
            spike_count += 1
    return spike_count

# Irrelevant function: analyzes pressure trends (dead end)
def evaluate_pressure_trend(pressure_log):
    trend_score = 0
    for i in range(1, len(pressure_log)):
        if pressure_log[i] > pressure_log[i-1]:
            trend_score += 1
    return trend_score

# Decoy function that looks important but isn't used in final calculation
def compute_neutron_flux(sequence):
    flux = 0
    for s in sequence:
        flux += (s ** 2) % 7
    return flux

# Core calculation function buried among distractions
def transform_calibration_data(data_map):
    calibrated = []
    offset = data_map['baseline'] * 0.1
    for val in data_map['readings']:
        adjusted = val - offset
        if adjusted > 500:
            adjusted = 500 + (adjusted - 500) ** 0.5
        calibrated.append(adjusted)
    return sum(calibrated) / len(calibrated)

# Main computational chain
reactor_state = {
    'status': 'active',
    'baseline': 75,
    'readings': [620, 680, 740, 790, 810],
    'temperature_readings': [860, 720, 880, 640],
    'pressure_log': [120, 125, 130, 132, 135],
    'neutron_sequence': [3, 5, 8, 6, 9]
}

# Distractor variables
pressure_diagnostic = evaluate_pressure_trend(reactor_state['pressure_log'])
spike_events = analyze_reactor_metrics(reactor_state)
neutron_analysis = compute_neutron_flux(reactor_state['neutron_sequence'])

# Hidden dependency: calibration affects thermal model
raw_calibration = transform_calibration_data(reactor_state)

# Secondary transformation chain with misleading intermediate
buffer_pool = defaultdict(int)
for i, temp in enumerate(reactor_state['readings']):
    buffer_pool[f'zone_{i}'] = (temp * raw_calibration) // 100

consistency_check = Counter(buffer_pool.values())

# Complex multi-step calculation disguised as diagnostics
def calculate_thermal_output(state):
    base_temp = sum(state['readings']) / len(state['readings'])
    variance = 0
    for t in state['readings']:
        variance += (t - base_temp) ** 2
    std_dev = math.sqrt(variance / len(state['readings']))
    
    # Apply non-linear correction based on calibration
    correction_factor = raw_calibration / 650.0
    
    # Nested logic with red herring conditions
    safety_margin = 1.0
    if std_dev > 70:
        safety_margin += 0.1
    if base_temp > 700:
        safety_margin += 0.15
    if len(state['temperature_readings']) > 3:
        # This branch looks important but has no effect due to override below
        safety_margin += 0.05
    safety_margin = 1.15  # Hard override - red herring above
    
    # Critical calculation path
    peak_load = max(state['readings'])
    load_ratio = peak_load / base_temp
    
    # Multi-factor integration
    raw_output = base_temp * load_ratio * correction_factor * safety_margin
    
    # Final adjustment using bit manipulation (obscures arithmetic)
    shifted = int(raw_output) ^ 0b1010
    shifted = shifted << 1
    shifted = shifted ^ 0b1101
    final_value = shifted / 2.0
    
    return final_value

# Execute main computation
temperature_profile = [t for t in reactor_state['readings'] if t > 600]
summary_stats = {
    'avg': sum(temperature_profile) / len(temperature_profile),
    'count': len(temperature_profile)
}

# Key assignment statement
thermal_capacity = calculate_thermal_output(reactor_state)

# Print result as required
print(f"Result: {thermal_capacity}")