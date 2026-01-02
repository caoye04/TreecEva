import math

def analyze_vital(vital):
    if vital < 50:
        return 'critical'
    elif vital < 75:
        return 'elevated'
    else:
        return 'normal'

# Irrelevant helper function (dead code path)
def legacy_score(value):
    temp = value * 0.87
    offset = 12.4
    adjusted = temp + offset
    return int(adjusted % 100)

# Decoy data transformation
historical_logs = [
    {'ts': 1623456000, 'val': 88, 'type': 'temp'},
    {'ts': 1623456060, 'val': 45, 'type': 'o2'},
    {'ts': 1623456120, 'val': 70, 'type': 'hr'}
]

log_summary = []
for entry in historical_logs:
    if entry['type'] == 'temp':
        log_summary.append(entry['val'] * 1.02)
    elif entry['type'] == 'o2':
        log_summary.append(entry['val'] * 0.98)
    else:
        log_summary.append(entry['val'])

# Unused transformation result
total_log_weight = sum(log_summary) / len(log_summary) if log_summary else 0

# Core processing begins
vital_signs = [88, 92, 76, 85, 67, 54, 90, 81, 73]
symptom_flags = {v: analyze_vital(v) for v in vital_signs}

flag_counts = {
    'critical': len([f for f in symptom_flags.values() if f == 'critical']),
    'elevated': len([f for f in symptom_flags.values() if f == 'elevated']),
    'normal': len([f for f in symptom_flags.values() if f == 'normal'])
}

# Bit manipulation red herring
obfuscation_key = 0b110101
scrambled = [(v ^ obfuscation_key) % 100 for v in vital_signs]
masked_values = [v | 0b100000 for v in scrambled]  # Unused list

# Set operations (required feature)
baseline_norms = {75, 78, 80, 82, 85, 88}
current_set = set(vital_signs)
converged = baseline_norms & current_set  # Intersection
variance_score = abs(len(baseline_norms) - len(current_set)) + (10 - len(converged))

# Secondary distraction: mock calibration sequence
calibration_phases = ['init', 'align', 'stabilize', 'verify']
phase_codes = {}
for i, phase in enumerate(calibration_phases):
    code = (i + 1) * 17
    phase_codes[phase] = code * code  # Computed but mostly unused

# Only 'verify' code used
verification_seal = phase_codes.get('verify', 0) % 97

# Main metric computation chain
severity_index = 0
if flag_counts['critical'] > 0:
    severity_index += 40 * flag_counts['critical']
if flag_counts['elevated'] > 0:
    severity_index += 15 * flag_counts['elevated']

# Normalize using convergence and variance
if converged:
    base_stability = len(converged) * 5
    adjustment = variance_score * 0.7
    stability_rating = base_stability - adjustment
else:
    stability_rating = 10

# Final aggregation logic
health_data = {
    'signs': vital_signs,
    'flags': flag_counts,
    'stability': stability_rating,
    'size_factor': len(vital_signs)
}

def aggregate_metrics(data, threshold_config=None):
    if threshold_config is None:
        threshold_config = {'base': 50, 'penalty': 8, 'boost': 3}
    
    raw_total = sum(data['signs'])
    critical_count = data['flags']['critical']
    elevated_count = data['flags']['elevated']
    
    penalty = critical_count * threshold_config['penalty']
    bonus = min(elevated_count, 3) * threshold_config['boost']
    
    # Apply stability multiplier (clamped)
    stability_multiplier = max(0.5, min(1.5, data['stability'] / 50))
    
    intermediate = (raw_total - penalty + bonus) * stability_multiplier
    
    # Size adjustment
    size_mod = (data['size_factor'] - 6) * 1.2
    
    final_score = intermediate + size_mod
    
    # Diagnostic mapping
    if final_score < 400:
        diagnostic = 101
    elif final_score < 500:
        diagnostic = 207
    elif final_score < 600:
        diagnostic = 313
    else:
        diagnostic = 419
    
    # Additional decoy transformation
    encoded_diagnostics = []
    for i in range(4):
        shift = (diagnostic + i * 11) % 256
        encoded_diagnostics.append((shift ^ 0xAA) % 100)
    
    # Only last one considered
    final_code = encoded_diagnostics[-1]
    
    # Real return
    return int(final_score // 3) + final_code

thresholds = {'base': 52, 'penalty': 9, 'boost': 4}

# Key execution point
final_diagnostic = aggregate_metrics(health_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")