import math

# Simulated system telemetry data
def collect_telemetry():
    raw_signals = [0.88, 0.72, 0.91, 0.65, 0.83]
    processed = list(map(lambda x: round(x * 128), raw_signals))
    return {"levels": processed, "version": "v2.3", "calibration": 1.0}

def evaluate_stability(index, history):
    if index < len(history) - 1:
        return history[index] > history[index + 1]
    return False

# Irrelevant auxiliary function (decoy)
def compute_compatibility_score(config_a, config_b):
    score = 0
    for i in range(min(len(config_a), len(config_b))):
        score += (config_a[i] + config_b[i]) % 7
    return score * 1.5

# Core analysis logic
def analyze_health_vector(data):
    magnitude = sum(x ** 2 for x in data["levels"])
    norm = math.sqrt(magnitude)
    adjusted_norm = norm / len(data["levels"])
    
    # Distractor computation (not used in final result)
    temp_analysis = {
        "peak": max(data["levels"]),
        "entropy": sum(-x/norm * math.log2(x/norm) for x in data["levels"] if x > 0),
        "outliers": [x for x in data["levels"] if x > 100]
    }
    
    # Actual signal extraction
    signal_strength = adjusted_norm
    if signal_strength > 90:
        signal_strength -= 10
    return signal_strength

# System log processor (partial red herring)
def parse_system_log(log_entries):
    error_count = 0
    warnings = set()
    timeline = []
    
    for entry in log_entries:
        timestamp = entry.get('ts', 0)
        level = entry.get('level', 'info')
        msg = entry.get('msg', '')
        
        if level == 'error':
            error_count += 1
            timeline.append(timestamp)
        elif level == 'warn':
            warnings.add(msg[:15])
    
    # Dead code path (never executed due to logic above)
    if len(warnings) > 100:
        critical_flag = True
    else:
        critical_flag = False
    
    # Only this value is actually used downstream
    return {'errors': error_count, 'sequence_length': len(timeline)}

# Main diagnostic engine
def analyze_system_state(metrics, log_data):
    # Step 1: Extract health metric
    base_score = analyze_health_vector(metrics)
    
    # Step 2: Fetch log-derived indicators
    log_profile = parse_system_log(log_data)
    
    # Step 3: Apply correction based on error frequency
    adjustment_factor = 1.0
    if log_profile['errors'] > 5:
        adjustment_factor = 0.85
    elif log_profile['errors'] == 0:
        adjustment_factor = 1.1
    
    # Step 4: Incorporate time-series pattern
    trend_modifier = 1.0
    if 'sequence_length' in log_profile and log_profile['sequence_length'] % 2 == 1:
        trend_modifier = 0.95
    
    # Step 5: Apply multipliers
    intermediate = base_score * adjustment_factor * trend_modifier
    
    # Step 6: Threshold clipping
    if intermediate < 70:
        intermediate = 70
    elif intermediate > 105:
        intermediate = 105
    
    # Step 7: Final non-linear transformation
    final_value = int(intermediate ** 1.05)
    
    # Irrelevant post-processing (distractor)
    diagnostics = {
        "raw_base": base_score,
        "adjusted": intermediate,
        "version_check": metrics.get("version", "unknown"),
        "consistency_ratio": intermediate / final_value if final_value != 0 else 0
    }
    
    # Only this variable matters
    final_diagnostic = final_value + 5
    
    # Unused branching (red herring)
    if diagnostics["consistency_ratio"] > 0.99:
        final_diagnostic *= 2  # Never reached
    
    return final_diagnostic

# Generate inputs
health_metrics = collect_telemetry()
system_log = [
    {"ts": 100, "level": "info", "msg": "system boot"},
    {"ts": 105, "level": "warn", "msg": "minor drift detected"},
    {"ts": 110, "level": "error", "msg": "sensor timeout"},
    {"ts": 115, "level": "error", "msg": "sync failure"},
    {"ts": 120, "level": "error", "msg": "retry limit exceeded"},
    {"ts": 125, "level": "warn", "msg": "corrective action"},
    {"ts": 130, "level": "error", "msg": "data corruption"},
    {"ts": 135, "level": "error", "msg": "checksum mismatch"},
    {"ts": 140, "level": "error", "msg": "channel reset"}
]

# Execute main logic
final_diagnostic = analyze_system_state(health_metrics, system_log)
print(f"Target result: {final_diagnostic}")