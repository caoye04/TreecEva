from collections import defaultdict, Counter

# Simulated sensor data aggregation for a health monitoring system
def collect_telemetry():
    raw_readings = [
        (1, 'HR', 72), (2, 'BP', 120), (3, 'O2', 98),
        (1, 'HR', 75), (2, 'BP', 118), (4, 'TEMP', 36.8),
        (5, 'HR', 80), (6, 'O2', 96), (7, 'BP', 125)
    ]
    
    aggregated = defaultdict(list)
    for device_id, metric, value in raw_readings:
        aggregated[metric].append(value)
    
    # Irrelevant transformation - distractor
    stats_summary = {k: (sum(v)/len(v), min(v), max(v)) for k, v in aggregated.items()}
    
    # This is actually used
    normalized = {k: sum(v) // len(v) for k, v in aggregated.items()}
    return normalized

# Decoy function - never called
def analyze_risk_factors(data):
    risk_score = 0
    for val in data.values():
        if val > 100:
            risk_score += 3
        elif val > 70:
            risk_score += 1
    return risk_score * 0.5

# Another decoy - looks important but unused
class DiagnosticEngine:
    def __init__(self):
        self.thresholds = defaultdict(lambda: 1.0)
    
    def calibrate(self, data):
        return {k: v * 1.1 for k, v in data.items()}

# Bit manipulation red herring
def encode_status_code(code):
    encoded = 0
    for i, c in enumerate(str(code)):
        encoded |= (int(c) << i) ^ (i * 3)
    return encoded + 1000  # Never integrated into main logic

# Real processing begins here
def build_threshold_map(metrics):
    # Complex but partially irrelevant logic
    base = {'HR': 75, 'BP': 120, 'O2': 95, 'TEMP': 37.0}
    adjustments = Counter(['HR', 'HR', 'BP', 'O2'])
    
    # Only this line matters
    result = {k: base[k] + (adjustments[k] * 0.5) for k in base}
    
    # Dead code branch
    if len(adjustments) > 10:
        result['OVERLOAD'] = 999
    
    return result

# Core logic with early returns and conditional expressions
def evaluate_stability(value, thresh, metric):
    if metric == 'O2':
        return 1 if value >= thresh else -2
    elif metric == 'HR':
        deviation = abs(value - thresh)
        return 2 if deviation <= 5 else (0 if deviation <= 10 else -1)
    else:
        return 1 if abs(value - thresh) < 3 else 0

# Main processing pipeline
def process_metrics(data, thresholds):
    score_map = defaultdict(int)
    priority_flags = set()
    
    for metric, value in data.items():
        if metric not in thresholds:
            continue
        
        stability = evaluate_stability(value, thresholds[metric], metric)
        score_map[metric] = stability
        
        # Early termination red herring
        if stability < 0:
            priority_flags.add(metric)
            break  # This break is misleading - makes you think it stops early, but only affects flag
    
    # Critical computation - depends on full loop
    base_diagnostic = sum(score_map.values()) * 10
    
    # Multiple distractor operations
    temp_adjustment = 0
    for i in range(3):
        temp_adjustment ^= (i + base_diagnostic) & 7
    
    # Decoy conditional that doesn't affect outcome
    if 'HR' in priority_flags and 'O2' in priority_flags:
        temp_adjustment += 100
    
    # Final result built from actual logic
    final_diagnostic = base_diagnostic + temp_adjustment * 0  # Neutralized distractor
    
    # This print is required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Data collection
    health_data = collect_telemetry()
    
    # Irrelevant preprocessing
    filtered_data = {k: v for k, v in health_data.items() if k in ['HR', 'BP', 'O2']}
    scaled_data = {k: v * 1.01 for k, v in filtered_data.items()}  # Unused
    
    # Threshold setup
    threshold_map = build_threshold_map(filtered_data)
    
    # Key execution point
    final_diagnostic = process_metrics(health_data, threshold_map)