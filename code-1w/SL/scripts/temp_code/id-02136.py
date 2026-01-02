import math

# Simulated sensor fusion system for environmental monitoring
def collect_data():
    raw_entries = [
        'temp:23.5,hum:45,co2:415',
        'temp:24.1,hum:47,co2:423',
        'temp:22.8,hum:50,co2:409',
        'temp:25.3,hum:44,co2:431'
    ]
    return raw_entries

# Irrelevant parsing function (decoy)
def parse_legacy_format(entry):
    parts = entry.split('|')
    if len(parts) == 3:
        return {"legacy": True}
    else:
        return {"legacy": False}

# Real data parser
def parse_modern_entry(entry):
    pairs = entry.split(',')
    result = {}
    for pair in pairs:
        k, v = pair.split(':')
        result[k] = float(v)
    return result

# Signal conditioning with multiple distractors
def filter_noise(readings, threshold=1.5):
    filtered = []
    noise_log = []  # Dead variable - never used again
    total_suppressed = 0.0

    for reading in readings:
        temp_diff = abs(reading['temp'] - 24.0)
        if temp_diff > threshold:
            suppression_factor = math.exp(-temp_diff)
            total_suppressed += suppression_factor
            continue
        filtered.append(reading)
    
    # Decoy computation (irrelevant)
    if total_suppressed > 0:
        adjustment_curve = []
        for i in range(5):
            adjustment_curve.append(math.sin(total_suppressed * i))

    return filtered

# Data transformation with set operations
def extract_unique_signatures(signals):
    signatures = set()
    duplicates_ignored = set()  # Unused tracking
    for s in signals:
        sig = (round(s['temp']), round(s['hum']))
        if sig in signatures:
            duplicates_ignored.add(sig)
        else:
            signatures.add(sig)
    return signatures

# Tuple-based calibration mapping
def generate_calibration_map(signatures):
    calibrations = {}
    base_shift = 0.87
    for sig in signatures:
        temp_class = 'high' if sig[0] > 24 else 'normal'
        hum_class = 'high' if sig[1] > 46 else 'optimal'
        key_tuple = (temp_class, hum_class, 'Q1')
        calibrations[key_tuple] = base_shift * (sig[0] + sig[1]) / 2
        base_shift *= 0.98  # Decaying irrelevant factor
    return calibrations

# Main processing pipeline
processed_signals = []
def process_chain():
    global processed_signals
    entries = collect_data()
    parsed_data = []
    
    # Parsing loop with red herring
    for entry in entries:
        if "legacy" in entry:  # Never true
            parsed_data.append(parse_legacy_format(entry))
        else:
            parsed_data.append(parse_modern_entry(entry))
    
    cleaned = filter_noise(parsed_data)
    
    # Secondary filtering (distractor)
    valid_co2 = []
    for c in cleaned:
        if 'co2' in c and c['co2'] > 400:
            valid_co2.append(c['co2'])
    avg_co2 = sum(valid_co2) / len(valid_co2) if valid_co2 else 400
    co2_offset = avg_co2 - 400  # Minor adjustment, not critical
    
    # Apply offset to temp as artificial correlation (misleading)
    for c in cleaned:
        c['temp'] += co2_offset * 0.01
        c['adjusted'] = True
    
    processed_signals = cleaned

# Recursive depth analysis (overcomplicated)
def calculate_depth_score(data, index=0, acc=None):
    if acc is None:
        acc = []
    if index >= len(data):
        return sum(acc) / len(acc) if acc else 0
    
    val = data[index]['temp'] * data[index]['hum']
    acc.append(math.log(val) if val > 0 else 0)
    
    # Dead recursive branch (never taken)
    if index == -1:
        backup = [v['co2'] for v in data]
        return max(backup) - min(backup)
    
    return calculate_depth_score(data, index + 1, acc)

# Core diagnostic logic
baseline_cache = {}  # Unused caching mechanism

def analyze_readings(signals):
    if not signals:
        return 0
    
    # Extract features
    temps = [s['temp'] for s in signals]
    hums = [s['hum'] for s in signals]
    co2_levels = [s['co2'] for s in signals]
    
    # Set operation on string representations (required feature)
    temp_strings = {f"T{t:.1f}" for t in temps}
    hum_strings = {f"H{h:.1f}" for h in hums}
    overlap_codes = temp_strings & hum_strings  # Intersection - always empty, but present
    
    # Primary calculation
    temp_mean = sum(temps) / len(temps)
    hum_mean = sum(hums) / len(hums)
    co2_mean = sum(co2_levels) / len(co2_levels)
    
    # Composite index with weighted factors
    stability_score = 0
    for i in range(len(signals)):
        t_dev = abs(temps[i] - temp_mean)
        h_dev = abs(hums[i] - hum_mean)
        stability_score += math.sqrt(t_dev**2 + h_dev**2)
    
    normalized_stability = stability_score / len(signals)
    
    # Final diagnostic formula
    diagnostic_value = (
        (temp_mean * 1.2) +
        (hum_mean * 0.8) +
        (co2_mean * 0.05) -
        (normalized_stability * 3.5)
    )
    
    # Store intermediate values (some irrelevant)
    diagnostics_log = {
        'readings_count': len(signals),
        'primary_index': diagnostic_value,
        'stability_metric': normalized_stability,
        'overlap_count': len(overlap_codes),  # Always 0
        'version': '2.1'
    }
    
    # Final transformation using string method (required feature)
    version_str = diagnostics_log['version']
    if version_str.replace('.', '').isdigit():
        scale_factor = float(version_str) * 0.1
        diagnostic_value *= (1 + scale_factor)
    
    return int(diagnostic_value)

# Execution flow with decoy branches
process_chain()

# Unused alternative path (dead code)
if __name__ != "__main__":
    fallback_data = [{'temp': 20, 'hum': 50, 'co2': 400}]
    final_diagnostic = analyze_readings(fallback_data)
else:
    final_diagnostic = analyze_readings(processed_signals)

# Additional distraction: unused aggregation
aggregated_key_metrics = []
for sig in processed_signals:
    code_name = f"M{int(sig['temp'])}{int(sig['hum'])}"
    if code_name.startswith('M'):
        code_name = code_name.replace('M', 'X')
    aggregated_key_metrics.append(code_name)

# Output result
print(f"Result: {final_diagnostic}")