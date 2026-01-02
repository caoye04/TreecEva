def analyze_sensor(x, baseline):
    return (x ^ baseline) + (x & 7)


def validate_readings(readings):
    valid = []
    for r in readings:
        if r < 0 or r > 1023:
            continue
        valid.append(r * 2)
    return valid


def extract_features(data_stream):
    features = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            features.append(val ** 0.5)
        elif i % 3 == 1:
            features.append(val // 4)
        else:
            features.append(abs(val - 512))
    return [round(f, 2) for f in features]


def compute_checksum(seq):
    checksum = 0
    for i, s in enumerate(seq):
        checksum += s ^ (i + 1)
    return checksum % 1000


def aggregate_metrics(turbine_data, thresholds):
    processed = []
    temp_log = []
    total_shift = 0

    # Irrelevant pre-processing (distractor)
    max_val = max([max(d) for d in turbine_data])
    norm_factor = max_val / 100.0 if max_val else 1
    normalized = [[int(x / norm_factor) for x in row] for row in turbine_data]

    for idx, row in enumerate(turbine_data):
        filtered = validate_readings(row)
        enhanced = [analyze_sensor(x, thresholds[idx % len(thresholds)]) for x in filtered]
        
        # Real transformation affecting result
        shift_op = (enhanced[0] & 15) ^ (enhanced[-1] >> 2) if len(enhanced) > 1 else enhanced[0]
        total_shift += shift_op
        
        temp_log.extend(enhanced)

    # Key feature extraction (affects answer)
    feature_vector = extract_features(temp_log)
    sum_features = sum(f for f in feature_vector if isinstance(f, float))

    # Decoy aggregation (misleading path)
    fake_agg = []
    for a, b in zip(temp_log, reversed(temp_log)):
        fake_agg.append((a + b) % 256)
    fake_result = compute_checksum(fake_agg)

    # Red herring: unused complex calculation
    decoy_matrix = [[i*j for j in range(3)] for i in range(len(turbine_data))]
    decoy_sum = sum(sum(row) for row in decoy_matrix)

    # Actual final computation
    raw_diagnostic = int(sum_features) + (total_shift % 100)
    calibration = sum(thresholds) // len(thresholds)
    final_diagnostic = raw_diagnostic - calibration

    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    turbine_data = [
        [512, 100, 800, -5, 200],
        [300, 700, 1024, 400],
        [600, 900, 150, 888]
    ]
    thresholds = [100, 200, 300]
    final_diagnostic = aggregate_metrics(turbine_data, thresholds)