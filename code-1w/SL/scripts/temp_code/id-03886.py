import itertools

def analyze_metrics(data, threshold=50):
    # Irrelevant metric tracking
    temp_log = []
    filtered_values = []
    cumulative_shift = 0

    for i, record in enumerate(data):
        base_value = sum(record) / len(record)
        if base_value > threshold:
            adjusted = base_value * 0.9 + 10
        else:
            adjusted = base_value * 1.1

        # Distractor: logging unused diagnostics
        temp_log.append(f"Step {i}: {adjusted:.2f}")

        # Only every third valid entry is actually used
        if i % 3 == 0:
            filtered_values.append(adjusted)

        # Red herring computation
        cumulative_shift += abs(base_value - adjusted)

    # Semi-relevant transformation
    processed = [x for x in filtered_values if x > 40]
    return processed


def calculate_performance(results):
    # Misleading normalization step
    normalized_offsets = [max(row) - min(row) for row in results]
    avg_offset = sum(normalized_offsets) / len(normalized_offsets) if normalized_offsets else 0

    # Core logic hidden among distractions
    primary_scores = []    
    secondary_tally = 0

    for idx, segment in enumerate(results):
        if len(segment) < 4:
            continue
        
        # Real logic: compute weighted harmonic interaction
        a, b, c = segment[0], segment[2], segment[-1]
        if c != 0 and (a + b) > 0:
            interaction = (2 * a * b) / (a + b)  # harmonic mean component
            scaled = interaction * (c / 100)
            primary_scores.append(scaled)
        
        # Dead code path (never executed due to data structure)
        if idx > 100:
            fallback = sum(segment) / 1000
            secondary_tally += fallback

    # Actual answer derivation
    raw_performance = sum(primary_scores)
    
    # Distractor: unused complexity
    all_pairs = list(itertools.combinations(primary_scores, 2))
    coherence_score = 0
    for p1, p2 in all_pairs:
        if p2 != 0:
            coherence_score += p1 / p2

    # Final score depends only on raw_performance and fixed adjustment
    final_score = int(raw_performance + 7.5)  # truncates to integer

    return final_score

# Simulated benchmark data (deterministic)
data_segments = [
    [15, 20, 25, 30, 40],
    [10, 12, 14, 16],
    [25, 35, 45, 55, 65, 75],
    [8, 18, 28, 38, 48],
    [5, 9, 13, 17, 21, 25, 29]
]

# Trigger analysis (produces intermediate result)
interim_findings = analyze_metrics(data_segments, threshold=20)

# Key statement that determines the answer
calibration_set = [[30, 40, 50, 60], [10, 15, 25, 35, 45]]
final_score = calculate_performance(calibration_set)

print(f"Result: {final_score}")