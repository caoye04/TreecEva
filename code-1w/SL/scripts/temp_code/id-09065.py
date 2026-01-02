from collections import defaultdict, Counter
import math

# Simulated health monitoring system with multiple sensor inputs
def analyze_vital_trend(data_sequence):
    trend_scores = []
    for i in range(1, len(data_sequence)):
        diff = data_sequence[i] - data_sequence[i-1]
        if diff > 0:
            trend_scores.append(1.2)
        elif diff < 0:
            trend_scores.append(-0.8)
        else:
            trend_scores.append(0.1)
    return sum(trend_scores) if trend_scores else 0.0

def compute_stability_index(readings):
    if len(readings) < 2:
        return 0.0
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return round(math.exp(-variance), 4)

def filter_anomalies(dataset, limit=3):
    # Irrelevant filtering logic (dead path)
    counts = Counter(dataset)
    return [k for k, v in counts.items() if v >= limit]

def evaluate_risk_category(value, category_map):
    for threshold, category in sorted(category_map.items(), reverse=True):
        if value >= threshold:
            return category
    return 'unknown'

def generate_diagnostic_report(records):
    # Distractor: complex but unused report generation
    report = defaultdict(str)
    for record in records:
        status = 'stable' if record > 70 else 'caution'
        report[status] += 'x'
    return {k: len(v) for k, v in report.items()}

def process_metrics(data, config):
    # Core logic begins
    base_values = [v['reading'] for v in data if v['type'] == 'primary']
    
    # Red herring: unused transformation
    transformed = [round(math.log(abs(x) + 1) * 1.5, 2) for x in base_values]
    
    # Actual relevant metric
    avg_base = sum(base_values) / len(base_values) if base_values else 0
    
    # Intermediate calculation with distraction
    temp_flag = False
    debug_log = []
    for v in base_values:
        if v < config['critical_low']:
            debug_log.append(f'low_alert:{v}')
            temp_flag = True
    
    # Another decoy function call
    _ = analyze_vital_trend(base_values)
    
    # Key branching logic
    if avg_base < config['warning_level']:
        adjustment_factor = 0.6
    elif avg_base > config['optimal_high']:
        adjustment_factor = 1.4
    else:
        adjustment_factor = 1.0
    
    # Real computation path
    stability = compute_stability_index(base_values)
    trend_score = analyze_vital_trend(base_values)  # This one is actually used below
    
    # Composite index calculation (core)
    raw_composite = (stability * 300) + (trend_score * 50)
    adjusted_composite = raw_composite * adjustment_factor
    
    # Misleading normalization (unused)
    normalized = max(0, min(100, adjusted_composite / 10))
    
    # Final diagnostic depends on corrected scale
    final_diagnostic = int(round(adjusted_composite - 25))
    
    # Dead code branches
    if temp_flag:
        dummy = [math.sin(i) for i in range(10)]
        _ = sum(dummy)
    
    return final_diagnostic

# Setup input data
health_data = [
    {'type': 'primary', 'reading': 68},
    {'type': 'primary', 'reading': 70},
    {'type': 'primary', 'reading': 72},
    {'type': 'primary', 'reading': 69},
    {'type': 'secondary', 'reading': 85},  # ignored
    {'type': 'primary', 'reading': 71},
    {'type': 'calibration', 'reading': 0}  # ignored
]

thresholds = {
    'critical_low': 65,
    'warning_level': 68,
    'optimal_high': 75
}

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")