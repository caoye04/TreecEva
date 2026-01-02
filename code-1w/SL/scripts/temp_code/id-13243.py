from collections import defaultdict


def analyze_water_samples(samples):
    sample_stats = defaultdict(int)
    total_anomalies = 0
    cumulative_offset = 0

    for region, readings in samples.items():
        high_alerts = 0
        low_alerts = 0
        temp_sum = 0

        for reading in readings:
            if reading > 95:
                high_alerts += 1
                sample_stats['critical'] += 1
            elif reading < 30:
                low_alerts += 1
                sample_stats['warning'] += 1
            temp_sum += reading

        # Irrelevant averaging (distractor)
        avg_region = temp_sum / len(readings) if readings else 0
        cumulative_offset += round(avg_region % 10)

        if high_alerts > 2:
            total_anomalies += 1

    # Dead code path (misleading)
    if cumulative_offset > 100:
        return -1

    return sample_stats['critical']


def validate_purity_levels(readings, threshold=75):
    adjusted_scores = []
    penalty_factor = 0.85
    base_multiplier = 1.2
    phantom_count = 0  # unused distractor

    for val in readings:
        if val >= threshold:
            score = val * base_multiplier
            # Simulate conditional boost
            score += 5 if val > 90 else 0
            adjusted_scores.append(score)
        else:
            # Apply decay for below-threshold values
            decayed = val * penalty_factor
            adjusted_scores.append(decayed)

    # Extra computation: normalize to 100-scale (semi-relevant)
    max_score = max(adjusted_scores) if adjusted_scores else 1
    normalized = [round(s * (100 / max_score), 2) for s in adjusted_scores]

    # Final aggregation with early termination logic
    filtration_score = 0
    for ns in normalized:
        if ns < 40:
            continue  # skip low scores
        filtration_score += ns
        if filtration_score > 200:
            break  # early stop

    return int(filtration_score)

# Main execution
purity_readings = [88, 92, 76, 81, 64, 94, 85]
sample_regions = {
    'north': [85, 87, 90, 92, 28, 31],
    'south': [76, 79, 81, 95, 96, 94, 25],
    'east': [68, 73, 77, 80],
    'west': [90, 93, 91, 89, 87]
}

# Preliminary analysis (side effect, not used later)
analyze_water_samples(sample_regions)

threshold = 78
filtration_score = validate_purity_levels(purity_readings, threshold)
print(f"Result: {filtration_score}")