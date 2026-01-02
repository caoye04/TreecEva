from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly-weighted scoring
def main():
    raw_readings = [102, 95, 108, 99, 101, 94, 110, 103, 98, 107, 100, 96]
    thresholds = {'low': 97, 'high': 105}
    anomalies = []
    processed_data = []

    # Step 1: Filter and classify readings with distraction logic
    temp_accumulator = 0
    debug_log = []
    for i, val in enumerate(raw_readings):
        if val < thresholds['low'] or val > thresholds['high']:
            anomalies.append((i, val))
            weight = 1.5 if val > thresholds['high'] else 0.5
        else:
            weight = 1.0
        
        # Distractor: complex but unused transformation
        transformed = (val ** 0.5) * (i + 1) if i % 3 == 0 else val - (i % 5)
        debug_log.append(transformed)

        # Relevant: accumulate baseline sum
        temp_accumulator += val
        processed_data.append({'index': i, 'value': val, 'weight': weight})

    # Step 2: Compute frequency stats (semi-relevant)
    value_counts = Counter([r['value'] for r in processed_data])
    mode_value = value_counts.most_common(1)[0][1]  # just used to add complexity

    # Step 3: Group by weight categories using defaultdict (relevant)
    grouped_by_weight = defaultdict(list)
    for entry in processed_data:
        grouped_by_weight[entry['weight']].append(entry['value'])

    avg_low = sum(grouped_by_weight.get(0.5, [0])) / len(grouped_by_weight.get(0.5, [1]))
    avg_normal = sum(grouped_by_weight.get(1.0, [0])) / len(grouped_by_weight.get(1.0, [1]))
    avg_high = sum(grouped_by_weight.get(1.5, [0])) / len(grouped_by_weight.get(1.5, [1]))

    # Distractor: unused statistical spread
    ranges = {}
    for w, vals in grouped_by_weight.items():
        ranges[w] = max(vals) - min(vals) if vals else 0

    # Step 4: Apply correction factor based on anomaly count
    anomaly_count = len(anomalies)
    correction_factor = 0.9 if anomaly_count > 3 else 1.0
    base_metric = temp_accumulator / len(raw_readings)

    # Distractor: dead code path (never executed due to fixed condition)
    fallback_used = False
    if base_metric < 0:  # Impossible condition
        adjusted_avg = sum(raw_readings) / 2
        fallback_used = True
    else:
        adjusted_avg = base_metric * correction_factor

    # Step 5: Prepare inputs for final computation
    weights = {'baseline': adjusted_avg, 'penalty': 0.8, 'boost': 1.2}

    def compute_final_score(data, w):
        total_weighted = 0
        total_influence = 0
        for d in data:
            impact = d['value'] * w['boost'] if d['weight'] > 1.0 else d['value'] * w['penalty'] if d['weight'] < 1.0 else d['value']
            total_weighted += impact
            total_influence += d['weight']
        return int((total_weighted / total_influence) * w['baseline']) // 10

    final_score = compute_final_score(processed_data, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()