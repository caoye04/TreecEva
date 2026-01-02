from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [
        (101, 45.2, 'temp'), (102, 38.7, 'temp'), (103, 45.2, 'temp'),
        (201, 120, 'pressure'), (202, 115, 'pressure'), (203, 120, 'pressure'),
        (301, 7.8, 'ph'), (302, 8.2, 'ph'), (303, 7.8, 'ph')
    ]

    # Irrelevant aggregation - red herring
    device_stats = defaultdict(lambda: {'count': 0, 'total': 0.0})
    for dev_id, value, sensor_type in raw_readings:
        device_stats[dev_id]['count'] += 1
        device_stats[dev_id]['total'] += value

    # Misleading intermediate calculation
    avg_per_device = {dev: info['total'] / info['count'] for dev, info in device_stats.items()}
    overall_avg = sum(avg_per_device.values()) / len(avg_per_device)

    # Real processing begins: filter anomalies by type
    readings_by_type = defaultdict(list)
    for _, value, sensor_type in raw_readings:
        readings_by_type[sensor_type].append(value)

    # Decoy statistical analysis
    mode_values = {}
    for s_type, values in readings_by_type.items():
        count = Counter(values)
        mode_values[s_type] = max(count, key=count.get)

    # Threshold logic - actual relevant path
    base_thresholds = {'temp': 40.0, 'pressure': 110, 'ph': 7.5}
    fluctuation_scores = {}
    for s_type, values in readings_by_type.items():
        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)
        std_dev = math.sqrt(variance)
        fluctuation_scores[s_type] = std_dev

    # Complex threshold adjustment with irrelevant components
    adjustment_log = []
    adjusted_thresholds = {}
    for s_type in ['temp', 'pressure', 'ph']:
        raw_thresh = base_thresholds[s_type]
        score = fluctuation_scores[s_type]
        if s_type == 'temp':
            adj = raw_thresh + (score * 1.5)
        elif s_type == 'pressure':
            adj = raw_thresh + (score * 0.8)
        else:
            adj = raw_thresh + (score * 1.2)
        adjusted_thresholds[s_type] = adj
        adjustment_log.append(f'{s_type}:{adj:.3f}')

    # Dead code path - never executed
    def legacy_compatibility(data):
        return [x * 1.05 for x in data if isinstance(x, (int, float))]

    metadata_index = {'version': '2.1', 'schema': 'sensor-v3', 'active': False}
    if metadata_index['active']:
        backup_thresholds = adjusted_thresholds.copy()
        for k in backup_thresholds:
            backup_thresholds[k] *= 0.95

    # Actual filtering logic
    critical_events = []
    for reading in raw_readings:
        _, value, s_type = reading
        thresh = adjusted_thresholds[s_type]
        if value > thresh:
            deviation = value - thresh
            if deviation > 0:
                critical_events.append((value, thresh, deviation, s_type))

    filtered_data = [(v, t, d, st) for v, t, d, st in critical_events if d > 0.1]

    # Secondary decoy: unused complex structure
    summary_matrix = [
        [len(readings_by_type[t]), round(fluctuation_scores[t], 2)] 
        for t in sorted(readings_by_type.keys())
    ]

    # Final processing function - key relevant logic
    def process_readings(events, thresholds):
        if not events:
            return -1
        total_excess = 0.0
        type_contributions = defaultdict(float)
        for value, threshold, deviation, stype in events:
            contribution = deviation * 1.8 if stype == 'temp' else deviation * 1.4
            if stype == 'pressure':
                contribution *= 1.1
            type_contributions[stype] += contribution
            total_excess += contribution
        
        # Additional distraction inside function
        sorted_contribs = sorted(type_contributions.items(), key=lambda x: x[1], reverse=True)
        ranking_hint = [k for k, _ in sorted_contribs]
        
        final_score = int(round(total_excess * 2.3))
        sanity_check = sum(type_contributions.values())
        if abs(sanity_check - total_excess) > 1e-5:
            return -999
        return final_score

    threshold_map = adjusted_thresholds  # Relevant assignment
    
    # Unused but plausible-looking diagnostics
    outlier_report = []
    for t in readings_by_type:
        vals = readings_by_type[t]
        q1, q3 = sorted(vals)[1], sorted(vals)[-2]
        iqr = q3 - q1
        lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
        outliers = [v for v in vals if v < lower or v > upper]
        if outliers:
            outlier_report.append((t, len(outliers)))
    
    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")