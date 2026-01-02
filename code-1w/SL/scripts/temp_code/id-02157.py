def analyze_component_health(reading, baseline, weights):
    return sum((r - b) * w for r, b, w in zip(reading, baseline, weights))

# Simulate sensor array data
sensor_readings = [
    [0.85, 1.02, 0.93, 2.15],
    [0.87, 0.99, 0.91, 2.10],
    [0.84, 1.05, 0.95, 2.20],
    [0.88, 0.97, 0.89, 2.05]
]

baseline_calibration = [0.80, 1.00, 0.90, 2.00]
feature_weights = [2.0, 1.5, 3.0, 0.5]

# Irrelevant auxiliary computation (distractor)
decoy_aggregates = []
for i in range(len(sensor_readings)):
    temp_sum = 0
    for val in sensor_readings[i]:
        temp_sum += val ** 0.5
    decoy_aggregates.append(temp_sum * 0.1)  # Unused result

# Hidden intermediate: health scores per reading
diagnostic_scores = []
for idx, reading in enumerate(sensor_readings):
    score = analyze_component_health(reading, baseline_calibration, feature_weights)
    diagnostic_scores.append(round(score, 3))

# Data transformation using dictionary and lambda (required feature)
score_map = {i: val for i, val in enumerate(diagnostic_scores)}
adjustment_factor = lambda x: 0.95 if x > 0.4 else (1.05 if x < 0.2 else 1.0)
adjusted_scores = {k: adjustment_factor(v) * v for k, v in score_map.items()}

# Conditional override simulation (red herring path)
if any(v > 0.6 for v in adjusted_scores.values()):
    for k in adjusted_scores:
        adjusted_scores[k] *= 0.98  # Minor adjustment, not final

# Log entry generation with metadata (mix of relevant and irrelevant)
log_entries = []
for i, raw_score in enumerate(diagnostic_scores):
    log_entries.append({
        'timestamp': f'2023-11-05T10:{i:02d}:00',
        'node_id': f'N-{1000 + i}',
        'raw_diagnostic': raw_score,
        'priority': 'high' if raw_score > 0.35 else 'normal',
        'redundant_flag': False
    })

# System thresholds with unused alternatives (distractor)
system_thresholds = {
    'critical': 0.55,
    'warning': 0.35,
    'info': 0.15,
    'legacy_mode': False,
    'deprecated_limit': 0.75  # Not used
}

# Secondary unused function (dead code path)
def legacy_evaluate(seq):
    total = 0
    for x in seq:
        total += x * 0.7 + 0.3
    return total / len(seq) if seq else 0

# Core processing function combining multiple concepts
def process_metrics(entries, thresholds):
    critical_count = 0
    aggregate = 0.0
    recent_high = []

    # Enumerate with filtering (required feature)
    for i, entry in enumerate(entries):
        val = entry['raw_diagnostic']
        if val > thresholds['warning']:
            critical_count += 1
            aggregate += val
        if i >= 1 and val > 0.4:
            recent_high.append(val)
    
    # Compute average of qualifying diagnostics
    avg_critical = aggregate / critical_count if critical_count > 0 else 0.0
    
    # Apply decay based on recency pattern (complex logic)
    if len(recent_high) >= 2:
        trend = recent_high[-1] - recent_high[-2]
        adjustment = 1.1 if trend > 0 else 0.95
        avg_critical *= adjustment
    
    # Final clamping operation
    final_value = max(avg_critical, 0.25)
    
    # Dead code branches (misleading paths)
    if final_value > 1.0:
        final_value = 0.99
    elif final_value < 0.1:
        final_value = 0.1
        
    return round(final_value, 6)

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")