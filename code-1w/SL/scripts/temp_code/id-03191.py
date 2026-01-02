import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_signals = [i * 0.5 + (i % 7) for i in range(15)]
    return raw_signals

def filter_outliers(data, limit=10):
    # Irrelevant filtering branch (not used in final computation)
    return [x for x in data if x < limit]

def compute_moving_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def generate_combinations(values):
    # Distractor: generates pairs but not used in critical path
    return list(itertools.combinations(values, 2))

def enhance_resolution(data):
    # Applies transformation but some results are ignored
    enhanced = []
    for x in data:
        if x > 5:
            enhanced.append(x * 1.2)
        else:
            enhanced.append(x * 0.9)
    return enhanced

def apply_calibration(signal, factor=0.98, offset=0.1):
    # Red herring calibration function (used on unused branch)
    return [factor * x + offset for x in signal]

def detect_anomalies(stream):
    # Dead code path — never called
    count = 0
    for val in stream:
        if abs(val - sum(stream)/len(stream)) > 2:
            count += 1
    return count

def normalize_dataset(batch):
    min_val, max_val = min(batch), max(batch)
    return [(x - min_val) / (max_val - min_val) * 100 for x in batch]

def transform_readings(readings):
    # Key transformation: maps raw to intermediate domain
    transformed = []
    for r in readings:
        if r < 4:
            transformed.append(r ** 2)
        elif r < 8:
            transformed.append(r * 2.5)
        else:
            transformed.append(r + 10)
    return transformed

def evaluate_stability(metrics):
    # Decoy function computing stability index (not part of answer)
    diffs = [abs(metrics[i] - metrics[i-1]) for i in range(1, len(metrics))]
    return sum(diffs) / len(diffs)

def group_by_phase(data):
    # Splits data into phases (distractor structure)
    phase_a = data[:6]
    phase_b = data[6:10]
    phase_c = data[10:]
    return {'A': phase_a, 'B': phase_b, 'C': phase_c}

def analyze_pattern(dataset, config):
    # Core logic hidden among distractions
    total_impulse = 0
    for idx, val in enumerate(dataset):
        if idx % 2 == 0 and val > config['threshold_primary']:
            total_impulse += int(val)
        elif idx % 3 == 0 and val > config['threshold_secondary']:
            total_impulse -= int(val * 0.5)
    modulation_factor = config['base_modulator'] * 1.75
    return int(total_impulse * modulation_factor)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect initial samples
    sensor_log = collect_samples()  # [0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, ...]

    # Step 2: Apply non-critical filtering (result unused)
    cleaned_log = filter_outliers(sensor_log, limit=12)

    # Step 3: Enhance resolution (used later)
    refined_signal = enhance_resolution(sensor_log)

    # Step 4: Generate moving average (dead end)
    trend_line = compute_moving_average(refined_signal, window=3)

    # Step 5: Normalize data for hypothetical comparison
    normalized_trend = normalize_dataset(trend_line)

    # Step 6: Transform original readings through key mapping
    transformed_data = transform_readings(sensor_log)  # Critical path

    # Step 7: Create irrelevant combinations
    paired_metrics = generate_combinations(transformed_data[:8])

    # Step 8: Define threshold configuration (critical)
    thresholds = {
        'threshold_primary': 6.0,
        'threshold_secondary': 4.0,
        'base_modulator': 2.0,
        'gain': 1.05
    }

    # Step 9: Evaluate stability on wrong data (distraction)
    stability_score = evaluate_stability(normalized_trend)

    # Step 10: Group data into phases (unused structure)
    phase_groups = group_by_phase(transformed_data)

    # Step 11: Analyze pattern using correct inputs
    final_diagnostic = analyze_pattern(transformed_data, thresholds)

    # Output result
    print(f"Result: {final_diagnostic}")