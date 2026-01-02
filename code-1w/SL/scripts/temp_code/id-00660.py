from collections import defaultdict, Counter

# Simulated sensor node readings with diagnostic tags
def analyze_readings(readings):
    diagnostics = defaultdict(list)
    anomalies = []
    base_rating = 0
    temp_buffer = []
    checksum = 0

    for idx, (val, status) in enumerate(readings):
        if val < 0:
            diagnostics['negative'].append(idx)
            anomalies.append(val)
        elif status == 'ERR':
            diagnostics['error_status'].append(idx)
        elif val > 1000:
            temp_buffer.append(val)
        else:
            if val % 7 == 0:
                checksum += val % 13
            base_rating += (val % 11)

    # Irrelevant aggregation - red herring
    error_summary = {k: len(v) for k, v in diagnostics.items()}
    buffer_stats = sum(temp_buffer) if temp_buffer else 0

    # Core logic disguised among distractions
    raw_candidates = [v for v, s in readings if s != 'CRIT' and v >= 0]
    candidate_freq = Counter(raw_candidates)
    candidates = [v for v in raw_candidates if candidate_freq[v] <= 2]

    # Decoy calculation
    peak_density = max(Counter([x // 100 for x in raw_candidates]).values()) if raw_candidates else 1

    # Misleading intermediate
    stability_index = (sum(abs(a - b) for a, b in zip(raw_candidates, raw_candidates[1:])) 
                      if len(raw_candidates) > 1 else 0)

    # Critical statement - target of evaluation
    anomaly_count = len([x for x in anomalies if x < -50])
    filtration_score = len(candidates) - anomaly_count + base_rating

    # Dead code path - never executed but looks relevant
    if False:
        fallback_score = buffer_stats - len(diagnostics['error_status'])
        filtration_score = fallback_score * 2

    # Output required result
    print(f"Result: {filtration_score}")
    return filtration_score

# Input data - deterministic sensor logs
sensor_data = [
    (105, 'OK'), (210, 'OK'), (-30, 'OK'), (42, 'ERR'), (77, 'OK'),
    (105, 'OK'), (140, 'OK'), (210, 'OK'), (-120, 'OK'), (999, 'OK'),
    (7, 'CRIT'), (14, 'OK'), (21, 'OK'), (1001, 'OK'), (49, 'OK')
]

result = analyze_readings(sensor_data)