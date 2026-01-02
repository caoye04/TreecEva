def analyze_system_load(usage_log):
    peak_load = max(usage_log)
    avg_load = sum(usage_log) / len(usage_log)
    normalized = [u / peak_load for u in usage_log]
    spikes = len([n for n in normalized if n > 0.9])
    return {'peak': peak_load, 'avg': avg_load, 'spikes': spikes}

# Irrelevant system diagnostics (distractor)
def diagnose_hardware():
    cpu_temp = 67.4
    fan_speed = 2400
    voltage_rails = {'+3.3V': 3.28, '+5V': 4.98, '+12V': 11.95}
    status = 'OK' if all(abs(v - nominal) < 0.5 for v, nominal in zip(voltage_rails.values(), [3.3, 5.0, 12.0])) else 'FAIL'
    return status

def process_security_flags(flags):
    # Bit manipulation red herring
    encrypted = 0
    for f in flags:
        encrypted ^= hash(f) & 0xFFFF
    critical_flag = (encrypted >> 8) & 0xFF
    return critical_flag

# Core logic disguised among distractions
def transform_data(records):
    base_values = [r['value'] for r in records]
    adjusted = list(map(lambda x: x * 1.05 if x < 100 else x * 0.98, base_values))
    capped = [min(val, 198.4) for val in adjusted]  # Artificial cap
    return capped

def calculate_risk_factor(inputs):
    total = 0
    for i in inputs:
        if i < 0:
            total -= i ** 0.5  # Complex math distraction
        elif i % 2 == 0:
            total += i // 3
        else:
            total += i * 0.1
    return round(total, 4)

# Main evaluation function with hidden signal in noise
def evaluate_performance(metrics, weights):
    # Destructuring distraction
    load_data, sec_flags, raw_records = metrics['system'], metrics['security'], metrics['data']
    
    # Irrelevant intermediate computations
    hardware_status = diagnose_hardware()  # Dead-end call
    risk_level = calculate_risk_factor([len(sec_flags), len(load_data), 5])
    processed_data = transform_data(raw_records)
    
    # Actual relevant path begins here
    load_analysis = analyze_system_load(load_data)
    spike_penalty = load_analysis['spikes'] * 1.5
    efficiency_bonus = 10 if load_analysis['avg'] < 75 else 5
    
    # Weighted score computation (key logic)
    base_metric = sum(m * w for m, w in zip([
        load_analysis['peak'],
        len(processed_data),
        process_security_flags(sec_flags)
    ], [weights[0], weights[1], weights[2]]))
    
    # Final adjustment using case-sensitive flag check (subtle but deterministic)
    flag_sum = sum(ord(f[0]) for f in sec_flags if f[0].isupper())
    adjustment = (flag_sum % 100) * 0.2
    
    final_score = base_metric + efficiency_bonus - spike_penalty + adjustment
    
    # Early return decoy (never reached due to structure)
    if False:
        return -999  # Dead code path
        truncated = processed_data[:2]
        return sum(truncated)
    
    return int(final_score)  # Deterministic integer result

# Setup with mixed relevance
usage_log = [88, 76, 92, 67, 95, 83, 71, 98, 65, 79]
security_flags = ['AdminAccess', 'ENCRYPTED', 'UserLogin', 'FIREWALL_ON']
data_records = [
    {'id': 'A1', 'value': 85},
    {'id': 'B2', 'value': 120},
    {'id': 'C3', 'value': 93},
    {'id': 'D4', 'value': 145}
]

weights = [0.3, 0.4, 0.3]
metrics = {
    'system': usage_log,
    'security': security_flags,
    'data': data_records
}

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")