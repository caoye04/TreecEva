from collections import defaultdict, Counter
import itertools

# Simulated health monitoring system with multiple sensor streams
def analyze_risk_level(values):
    avg = sum(values) / len(values)
    if avg > 75:
        return 'CRITICAL'
    elif avg > 50:
        return 'WARNING'
    else:
        return 'STABLE'

# Irrelevant helper function (decoy)
def calculate_bmi(weight, height):
    return weight / (height ** 2) * 703  # Not used in main logic

# Distractor data: unrelated patient records
historical_logs = [
    {'id': 'P001', 'temp': 98.6, 'hr': 72, 'bp': '120/80'},
    {'id': 'P002', 'temp': 101.2, 'hr': 110, 'bp': '140/90'}
]

# Unused transformation map (red herring)
sensor_mapping = {
    'ECG': lambda x: x * 1.05,
    'RESP': lambda x: x * 0.95,
    'O2': lambda x: x + 2 if x < 90 else x
}

# Real processing function with embedded distractions
def process_metrics(data, limits):
    # Irrelevant initialization (distractor variables)
    temp_cache = []
    checksum = 0
    anomaly_count = 0  # Never actually used

    # Core logic begins
    aggregated = defaultdict(list)
    for entry in data:
        for key, val in entry.items():
            aggregated[key].append(val)

    # Misleading normalization block (does not affect result)
    normalized = {}
    for k, v_list in aggregated.items():
        mean_v = sum(v_list) / len(v_list)
        normalized[k] = [v / mean_v * 100 for v in v_list]  # Dead end

    # Critical path: risk evaluation using raw data
    risk_flags = []
    for metric, readings in aggregated.items():
        threshold = limits.get(metric, 100)
        outliers = list(filter(lambda x: x > threshold, readings))
        risk_flags.append(len(outliers) > 0)

    # Secondary analysis: pattern detection with itertools
    flag_patterns = list(itertools.combinations(risk_flags, 2))
    pattern_score = len(flag_patterns) if len(flag_patterns) > 0 else 0

    # Decoy calculation with string manipulation
    status_tag = "ANALYSIS_" + "_".join([k.upper()[:3] for k in aggregated.keys()])
    status_code = sum([ord(c) for c in status_tag]) % 1000  # Looks important, unused

    # Actual determination path
    if any(risk_flags) and pattern_score >= 1:
        decision_weight = 888.888
    else:
        decision_weight = 111.111

    # Final computation chain
    base_metric = len(aggregated.keys()) * 100
    adjustment = sum([len(v) for v in aggregated.values()]) * 2
    
    # Key assignment - this is the real answer
    final_diagnostic = base_metric + adjustment + int(decision_weight)

    # More red herrings
    debug_trace = []
    for i in range(3):
        debug_trace.append(f"TRACE_{i}: {i*999}")  # Dead code

    return final_diagnostic

# Primary dataset (relevant input)
health_data = [
    {'HR': 75, 'O2': 92, 'BP_SYS': 150},
    {'HR': 80, 'O2': 88, 'BP_SYS': 155},
    {'HR': 85, 'O2': 94, 'BP_SYS': 145}
]

# Thresholds that matter
thresholds = {
    'BP_SYS': 150,  # Two entries exceed (150, 155)
    'HR': 90,
    'O2': 90
}

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")