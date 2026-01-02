def analyze_readings(readings):
    cumulative = 0
    for val in readings:
        if val > 0:
            cumulative += val ** 0.5
    return int(cumulative)

# Irrelevant helper (distractor)
def deprecated_normalizer(x):
    return x % 7 + 2  # Unused in logic

# Misleading preprocessing block
temp_log = [12, 15, 18, 22, 25]
offset = sum(temp_log) // len(temp_log)
adjusted_offsets = [x - offset for x in temp_log if x % 2 == 1]

# Core data
vital_signs = {
    'hr': [72, 68, 74, 71, 69],
    'spo2': [98, 97, 99, 98, 96],
    'bp_sys': [120, 118, 122, 119, 121]
}

# Decoy structure (not used)
system_flags = {
    'debug': False,
    'legacy_mode': True,
    'version': '2.1-alpha'
}

# Threshold configuration (used)
threshold_map = {
    'low_risk': 5,
    'moderate_risk': 10,
    'high_risk': 15
}

# Auxiliary computation (red herring)
baseline_score = 0
for key in vital_signs:
    baseline_score += len(vital_signs[key]) * 3  # Distractor: not used later

# Data transformation chain
aggregated = []
for metric in vital_signs.values():
    aggregated.extend([x // 10 for x in metric if x > 70])

# Conditional expression with distractors
flag_state = 'active' if len(aggregated) > 10 else 'standby'
override_code = 4 if flag_state == 'inactive' else 8  # Dead branch

# Real processing path
health_data = [
    sum(vital_signs['hr']) // len(vital_signs['hr']),
    min(vital_signs['spo2']),
    max(vital_signs['bp_sys']) - min(vital_signs['bp_sys'])
]

# Simulated noise injection (irrelevant)
noise_pattern = []
for i in range(3):
    noise_pattern.append((i * 2) ^ 5)  # Bitwise decoy

# Key function with dictionary and conditionals
def process_metrics(data, limits):
    risk_level = 'low_risk'
    if data[0] > 70:
        risk_level = 'moderate_risk'
    if data[2] >= 5:
        risk_level = 'high_risk'
    
    # Conditional expression (required feature)
    base = data[1] if risk_level == 'low_risk' else (data[1] + 2)
    
    # Dictionary-driven adjustment
    adjustment = {
        'low_risk': base * 0.9,
        'moderate_risk': base * 1.1,
        'high_risk': base * 1.3
    }[risk_level]
    
    # Final computation with hidden logic
    temp_result = adjustment * limits[risk_level]
    intermediate = int(temp_result) + (1 if data[0] % 2 == 0 else 0)
    
    # Dead code path (misleading)
    if override_code == 9:
        intermediate -= 100  # Never executed
    
    return intermediate + analyze_readings(aggregated)

# Trigger execution
diagnostic_trace = []
for i in range(2):  # Loop with no effect on answer
    diagnostic_trace.append(process_metrics(health_data, threshold_map) - i)

final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Target result: {final_diagnostic}")