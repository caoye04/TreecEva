from itertools import combinations

# Simulate sensor fusion system with weighted reliability scoring
def analyze_sensor_data(raw_readings):
    base_scores = {}
    temp_adjustments = []
    
    for sensor_id, readings in raw_readings.items():
        avg = sum(readings) / len(readings)
        variance = sum((x - avg) ** 2 for x in readings) / len(readings)
        reliability = 1 / (1 + variance)  # Higher reliability for lower variance
        base_scores[sensor_id] = avg * reliability

        # Irrelevant temperature drift simulation (distractor)
        if 'T' in sensor_id:
            for i in range(len(readings)):
                temp_adjustments.append(readings[i] * 0.98 ** i)

    return base_scores

# Weighted aggregation with redundancy filtering
def filter_redundant_inputs(scores):
    sorted_sensors = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    selected = [sorted_sensors[0]]
    
    # Simulate interference via unnecessary combination analysis
    all_pairs = list(combinations(sorted_sensors, 2))
    pair_impact = {}
    for pair in all_pairs:
        s1, s2 = pair[0][1], pair[1][1]
        pair_impact[(pair[0][0], pair[1][0])] = (s1 + s2) / (1 + abs(s1 - s2))

    # Only select non-redundant sensors (threshold-based)
    for item in sorted_sensors[1:]:
        last_selected_score = selected[-1][1]
        current_score = item[1]
        if abs(last_selected_score - current_score) > 0.5 or current_score > 3 * last_selected_score:
            selected.append(item)
    
    return dict(selected)

# Final scoring with decay factors and normalization
def calculate_overall_score(validated_results, importance_weights):
    composite = 0
    weight_sum = 0
    
    # Real computation path
    for sensor, score in validated_results.items():
        base_weight = importance_weights.get(sensor, 1.0)
        decay_factor = 0.95 ** len(sensor)  # Penalize longer IDs
        adjusted_score = score * base_weight * decay_factor
        composite += adjusted_score
        weight_sum += base_weight * decay_factor
    
    # Dead code branch - never executed (distractor)
    if False:
        backup = 0
        for val in validated_results.values():
            backup += val ** 0.5
        composite = max(composite, backup)
    
    # Auxiliary irrelevant calculation (bitwise red herring)
    magic_offset = 0
    for w in importance_weights.values():
        magic_offset ^= int(w * 10) & 7  # Bitwise XOR on scaled weights
    
    normalized = composite / weight_sum if weight_sum else 0
    final_with_offset = normalized + (magic_offset * 0.01)  # Minor influence, but measurable
    
    return round(final_with_offset, 4)

# Main execution flow
if __name__ == "__main__":
    # Input data from environmental monitoring array
    sensor_readings = {
        "S1": [2.1, 1.9, 2.0, 2.2],
        "S2": [5.3, 5.1, 5.4, 5.2],
        "T1": [3.0, 3.1, 2.9],
        "PWR": [10.0, 10.0, 10.1]
    }
    
    weights = {
        "S1": 1.2,
        "S2": 1.8,
        "T1": 0.9,
        "PWR": 0.1
    }
    
    # Step 1: Analyze raw data into reliability-weighted scores
    preliminary = analyze_sensor_data(sensor_readings)
    
    # Step 2: Remove redundant or correlated inputs
    filtered_results = filter_redundant_inputs(preliminary)
    
    # Step 3: Calculate final fused score
    final_score = calculate_overall_score(filtered_results, weights)
    
    # Output target variable
    print(f"Result: {final_score}")