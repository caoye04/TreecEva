from itertools import combinations

# Simulate sensor data calibration and weighted metric computation
def collect_diagnostics(values):
    diagnostics = []n    for i in range(len(values)):
        shifted = values[i] ^ 255  # Bitwise complement simulation
        if shifted > 100:
            diagnostics.append(shifted // 7)
    return diagnostics

def extract_patterns(text_data):
    # Irrelevant string processing - distractor
    segments = text_data.split(',')
    clean_segments = [s.strip().upper() for s in segments]
    joined = '-'.join(clean_segments)
    return joined.replace('X', '')  # No impact on final result

def validate_sequence(seq):
    # Another distractor: checks monotonicity but not used
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def process_metrics(raw_data, importance_weights):
    baseline = sum(raw_data) / len(raw_data)
    adjusted = [x * w for x, w in zip(raw_data, importance_weights)]
    
    # Generate some intermediate stats (partially relevant)
    deviations = [(x - baseline) ** 2 for x in raw_data]
    variance = sum(deviations) / len(deviations)
    stability_factor = 1.0 if variance < 500 else 0.8

    # Use itertools to compute interaction effects (real logic)
    interaction_sum = 0
    for pair in combinations(adjusted, 2):
        interaction_sum += abs(pair[0] - pair[1]) * 0.1

    # Key calculation path
    primary_total = sum(adjusted) * stability_factor
    penalty = 0
    for val in adjusted:
        if val > 300:
            penalty += (val - 300) * 0.05

    # Final score calculation
    final_score = primary_total - penalty + interaction_sum

    # Dead code branch - misleading control flow
    if len(raw_data) > 10:
        fallback = sum(raw_data) * 0.5
        final_score = max(final_score, fallback)

    return int(final_score)

# Main execution
sensor_readings = [120, 150, 200, 250, 180]
weights = [0.8, 1.2, 1.0, 1.5, 0.9]

diag_results = collect_diagnostics(sensor_readings)
text_log = "errX01, warnX02, infoX03"
processed_pattern = extract_patterns(text_log)

# This call has no side effects
validate_sequence(sensor_readings)

final_score = process_metrics(sensor_readings, weights)
print(f"Target result: {final_score}")