def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    magnitude = sum([abs(x) for x in filtered])
    return magnitude if magnitude > 10 else 0

system_load = {'cpu': 78, 'ram': 83, 'io': 45}
signal_data = [-1.2, 0.3, 0.7, -2.1, 1.8, 0.4, -0.9]

# Irrelevant signal processing branch (dead path)
if len(signal_data) < 5:
    normalized = [x / 3 for x in signal_data]
else:
    temp_avg = sum(signal_data) / len(signal_data)
    adjusted = [x - temp_avg for x in signal_data]  # Not used later

# Simulated health trace with decoy operations
health_trace = {
    'core_temp': [62, 65, 67, 70],
    'voltage': [3.2, 3.3, 3.1, 3.4],
    'fan_speed': [1200, 1350, 1500, 1800]
}

# Unused transformation (distractor)
decoded = ''.join([str(int(v[-1])) for v in health_trace.values()])
encoded_hash = hash(decoded) % 1000

# Conditional expression with string method red herring
diagnostic_flag = 'STABLE' if system_load['cpu'] < 80 and system_load['ram'] < 85 else 'OVERRIDE'
flag_status = diagnostic_flag.lower().replace('e', 'X')  # Distractor

# Real computation begins here (non-obvious due to prior noise)
def evaluate_core_risk(temp_seq, voltage_seq):
    risk_score = 0
    for i in range(len(temp_seq)):
        if temp_seq[i] > 65:
            risk_score += voltage_seq[i] * 10
    return int(risk_score)

# Bit manipulation decoy (irrelevant)
masked_load = (system_load['cpu'] << 2) ^ 0b1101

# Core metric processor combining multiple concepts
def process_metrics(traces, load):
    temps = traces['core_temp']
    volts = traces['voltage']
    base_risk = evaluate_core_risk(temps, volts)
    
    # Logical operation chain with short-circuiting
    overload = load['cpu'] > 75 and load['ram'] > 80 or load['io'] > 90
    
    # Conditional expression determining adjustment
    adjustment = -50 if not overload else (100 if base_risk > 60 else 75)
    
    # Final integration using arithmetic and logical mix
    intermediate = base_risk + adjustment
    
    # String-based switch logic (uses string method but resolves deterministically)
    mode = 'turbo'.upper().strip()
    bonus = 25 if 'TURBO' in mode else 0
    
    # Final result influenced by multiple paths, but only some are active
    result = intermediate + bonus
    
    # Dead code: unreachable branch
    if False:
        fallback = analyze_signal(signal_data)
        result -= fallback
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(health_trace, system_load)
print(f"Result: {final_diagnostic}")