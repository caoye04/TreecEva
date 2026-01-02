def analyze_readings(values):
    cumulative = 0
    for i, val in enumerate(values):
        if i % 2 == 0:
            cumulative += val ** 0.5
        else:
            cumulative -= val // 3
    return cumulative

# Irrelevant sensor simulation (red herring)
def simulate_noise(length):
    return [i * 0.9 + (i % 4) for i in range(length)]

# Unused transformation path
def transform_sequence(seq):
    return [x * 1.5 for x in seq if x > 5]

# Decoy function that looks important but isn't used in main logic
def compute_fusion_score(data):
    total = 0
    for d in data:
        total += d * d - d
    return total / len(data) if data else 0

# Real processing chain
def filter_outliers(arr, limit):
    return [x for x in arr if abs(x - sum(arr)/len(arr)) < limit]

def aggregate_windows(data, size=3):
    aggregated = []
    for i in range(0, len(data) - size + 1):
        window = data[i:i+size]
        aggregated.append(round(sum(window) / size, 2))
    return aggregated

def evaluate_stability(metrics):
    if not metrics:
        return 0
    avg = sum(metrics) / len(metrics)
    variance = sum((m - avg) ** 2 for m in metrics) / len(metrics)
    return round(avg - variance * 0.5, 2)

def process_metrics(raw_data, config):
    # Step 1: Preprocess with filtering
    clean_data = filter_outliers(raw_data, config['variance_cap'])
    
    # Step 2: Create rolling averages
    trends = aggregate_windows(clean_data, size=2)
    
    # Step 3: Analyze trend stability
    stability = evaluate_stability(trends)
    
    # Step 4: Secondary analysis on original indices
    index_sum = 0
    for idx, val in enumerate(raw_data):
        if val > config['baseline'] and idx % 2 == 1:
            index_sum += val // (idx + 1)
    
    # Step 5: Cross-correlation with dummy pattern (distractor)
    dummy_pattern = [1, 0, -1] * (len(clean_data)//3 + 1)
    correlation = sum(clean_data[i] * dummy_pattern[i] for i in range(len(clean_data)))

    # Step 6: Conditional override based on obscure rule (not triggered)
    trigger_condition = len([x for x in clean_data if x > config['baseline']]) > 5 and stability < 0
    temp_adjustment = stability * 1.5 if trigger_condition else stability * 0.8
    
    # Step 7: Combine multiple factors
    score_a = analyze_readings(clean_data)
    score_b = index_sum * 1.2
    
    # Step 8: Final diagnostic calculation (this is the real answer path)
    final_diagnostic = int(abs(score_a + score_b - temp_adjustment) % 10000)
    
    # Dead code branch (never executed)
    if False:
        fallback = compute_fusion_score(raw_data)
        final_diagnostic = max(final_diagnostic, int(fallback))
    
    return final_diagnostic

# Simulated health monitoring data (fictional sensor readings)
health_data = [25, 16, 9, 64, 49, 36, 81, 100, 121, 144]

# Threshold configuration with misleading keys
thresholds = {
    'baseline': 30,
    'variance_cap': 40,
    'emergency': 150,
    'debug_mode': False
}

# Unused data transformations (distractors)
noise_floor = simulate_noise(len(health_data))
distorted_signal = transform_sequence(health_data)

# Main execution point
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")