import math

# Irrelevant helper function (dead code path)
def unused_signal_transform(x):
    return [math.sin(xi) * 0.5 for xi in x]

# Misleading intermediate processing
def decoy_analysis(data):
    temp = sum([d ** 2 for d in data]) / len(data)
    return temp * 0.9  # Distractor computation

# Real transformation logic
transform_fn = lambda x: math.log(abs(x) + 1) * 2.0

# Simulated sensor inputs (irrelevant and relevant components)
sensor_readings = {
    'temp_core': [78, 85, 90, 88],
    'voltage_rails': [3.3, 3.4, 3.2, 3.5],
    'fan_speeds': [2000, 2200, 2100, 2300]
}

# Derived metrics with red herrings
raw_metrics = []
for key, values in sensor_readings.items():
    avg = sum(values) / len(values)
    if 'temp' in key:
        raw_metrics.append(('temperature_factor', avg * 1.1))
    elif 'voltage' in key:
        raw_metrics.append(('voltage_stability', abs(avg - 3.3) < 0.2))
    else:
        raw_metrics.append(('rpm_fluctuation', max(values) - min(values)))

# Unused data structure (distractor)
cached_fft = {k: [abs(hash(str(v)) % 100) for v in vs] for k, vs in sensor_readings.items()}

# System state with multiple fields (some irrelevant)
system_state = {
    'uptime_hours': 142,
    'load_profile': [0.65, 0.7, 0.8, 0.75],
    'security_lock': True,
    'last_reboot_cause': 'firmware_update'
}

# Core diagnostic vector (partially derived from real and fake sources)
diagnostics = []
for item in raw_metrics:
    if item[0] == 'temperature_factor':
        diagnostics.append(transform_fn(item[1]))
    elif item[0] == 'rpm_fluctuation':
        # This branch is never taken due to logic flow — misleading
        diagnostics.append(transform_fn(item[1] + 10))

# Add fixed synthetic metric (hidden relevance)
diagnostics.append(math.sqrt(system_state['uptime_hours']))

def process_metrics(metrics, state):
    result = 0.0
    # Nested conditional with distractors
    if state.get('security_lock'):
        result += metrics[0] * 1.5
    
    load_avg = sum(state['load_profile']) / len(state['load_profile'])
    fluctuation_score = (max(state['load_profile']) - min(state['load_profile'])) * 100
    
    # Red herring: fluctuation score not used
    _ = fluctuation_score * 2  
    
    # Key update using actual dependency
    result += load_avg * 20
    
    # Conditional mutation based on hidden rule
    if len(metrics) > 1:
        adjustment = math.sin(math.pi * load_avg / 2)
        result += adjustment * metrics[1]  # metrics[1] is boolean -> float
    
    # Dead branch: unreachable due to construction
    if 'invalid_flag' in state:
        result -= 100
    
    # Final nonlinear scaling
    result = math.floor(result * 100) / 100  # Round down to two decimals
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(diagnostics, system_state)

# Output the target result
print(f"Target result: {final_diagnostic}")