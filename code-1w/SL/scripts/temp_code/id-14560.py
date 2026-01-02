from collections import defaultdict, Counter

# Simulated sensor network data with noise and redundant metrics
def collect_diagnostics():
    raw_readings = [
        (1, 'temp', 98.6), (2, 'temp', 102.1), (3, 'temp', 97.3),
        (4, 'pressure', 118), (5, 'pressure', 122), (6, 'pressure', 119),
        (7, 'temp', 103.4), (8, 'temp', 96.8), (9, 'temp', 101.9),
        (10, 'humidity', 45), (11, 'humidity', 52), (12, 'humidity', 47)
    ]

    # Irrelevant aggregation - red herring
    stat_summary = defaultdict(lambda: {'count': 0, 'sum': 0})
    for sid, stype, val in raw_readings:
        stat_summary[stype]['count'] += 1
        stat_summary[stype]['sum'] += val

    # Decoy transformation - unused later
    normalized = {k: v['sum'] / v['count'] for k, v in stat_summary.items()}
    adjusted_scores = [abs(x[2] - 100) for x in raw_readings if x[1] == 'temp']

    # Actual processing path begins here
    temp_only = [(sid, val) for sid, stype, val in raw_readings if stype == 'temp']
    outlier_bounds = (97.0, 102.0)
    filtered_data = [val for sid, val in temp_only if not (val < outlier_bounds[0] or val > outlier_bounds[1])]

    # Misleading bitwise manipulation - looks important but unused
    flags = 0
    for val in filtered_data:
        flags ^= int(val) & 7
    flags = (flags << 3) | (flags >> 1)

    # Complex default dictionary setup with nested logic
    threshold_map = defaultdict(lambda: {'warn_low': 0, 'warn_high': 0, 'action': None})
    threshold_map['temp']['warn_low'] = 97.5
    threshold_map['temp']['warn_high'] = 101.5
    threshold_map['temp']['action'] = 'monitor'

    # Dead code path - unreachable due to prior filtering
    def legacy_correction(data):
        return [x * 0.98 + 1.5 for x in data]  # Not used

    # Key distracting computation - creates illusion of importance
    entropy_proxy = 0.0
    counts = Counter(int(v * 10) % 5 for v in filtered_data)
    total = sum(counts.values())
    for c in counts.values():
        p = c / total
        entropy_proxy -= p * __import__('math').log(p)

    # Real signal extraction via list comprehension and slicing
    recent_samples = filtered_data[-3:]  # Focus on latest three
    drift_estimate = sum(recent_samples[i+1] - recent_samples[i] for i in range(len(recent_samples)-1))

    # Final processing function (defined inline to obscure flow)
    def process_readings(data, thresholds):
        base = sum(data) / len(data)
        deviation = base - 99.6
        if base < thresholds['temp']['warn_low']:
            level = -1
        elif base > thresholds['temp']['warn_high']:
            level = 1
        else:
            level = 0
        return int((deviation * 100) + level * 10)

    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture result
collect_diagnostics()