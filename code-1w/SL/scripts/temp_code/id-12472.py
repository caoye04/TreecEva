def analyze_patient_data(raw_samples, thresholds):
    # Irrelevant preprocessing (distractor)
    normalized = [round(x * 0.89, 2) for x in raw_samples if x > 10]
    offset_correction = sum([i * 0.01 for i in range(len(normalized))])

    # Core data sets
    biomarkers = set(raw_samples)
    critical_levels = set(thresholds)
    elevated = biomarkers & critical_levels
    mild_elevation = biomarkers - critical_levels

    # Misleading accumulation path (dead-end logic)
    temp_score = 0
    for val in mild_elevation:
        if val % 7 == 0:
            temp_score += val // 7
    temp_score *= 1.5  # Unused downstream

    # Primary analysis path
    severity_weights = {}
    for idx, val in enumerate(raw_samples):
        if val > thresholds[idx % len(thresholds)]:
            severity_weights[idx] = val ** 0.5
        else:
            severity_weights[idx] = val * 0.1

    base_aggregate = sum(severity_weights.values())
    adjustment_factor = len(elevated) * 1.75
    aggregate_health_score = base_aggregate - adjustment_factor

    # Red herring: complex string logic with no impact
    sample_labels = ['S' + str(i).zfill(3) for i in range(len(raw_samples))]
    label_concat = ''.join(sample_labels)
    split_parts = label_concat.split('S')
    valid_ids = [p for p in split_parts if p.isdigit() and int(p) < 200]
    checksum = sum(int(v) for v in valid_ids) / 100.0 if valid_ids else 0.0

    # Decoy function call (no side effects)
    def compute_stress_index(data):
        return sum(d ** 0.3 for d in data) / len(data)
    stress_proxy = compute_stress_index(raw_samples) * 0.01  # Not used

    # Key state variables
    remaining_biomarkers = biomarkers.symmetric_difference(critical_levels)
    clearance_rate = 0.92
    decay_adjustment = 1.0
    for _ in range(len(remaining_biomarkers)):
        decay_adjustment *= clearance_rate

    # Critical assignment (target execution point)
    final_diagnostic = aggregate_health_score + len(remaining_biomarkers)

    # Output required result
    print(f"Result: {final_diagnostic}")

# Input data (deterministic)
patient_samples = [45, 68, 72, 88, 61, 90, 55]
detection_limits = [70, 50, 80, 60, 95]

# Execute
analyze_patient_data(patient_samples, detection_limits)