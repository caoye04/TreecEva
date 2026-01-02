import math

def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 50]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    normalized = [x - baseline for x in filtered]
    return normalized

def compute_entropy(values):
    if not values:
        return 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

def detect_spikes(signal, sensitivity=0.85):
    threshold = sensitivity * max(signal, default=1)
    spikes = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            spikes.append(i)
    return spikes if len(spikes) > 0 else [0]

def transform_coordinates(indices, offset=100):
    # Irrelevant geometric mapping (distractor)
    transformed = []
    for idx in indices:
        x = (idx * 2 + offset) % 360
        y = int(math.sin(math.radians(x)) * 100)
        transformed.append((x, y))
    return transformed

def evaluate_stability(risk_factors):
    # Dead code path — never actually used in final computation
    if len(risk_factors) == 0:
        return 0.0
    weighted = 0.0
    for i, factor in enumerate(risk_factors):
        weighted += factor * (0.9 ** i)
    return weighted / len(risk_factors)

def recursive_diagnose(state, depth):
    if depth <= 0 or sum(state) < 5:
        return sum(state)
    new_state = [state[i] - i for i in range(len(state)) if i % 2 == 0]
    return recursive_diagnose(new_state, depth - 1) + len(new_state)

def analyze_metrics(system_state, thresholds):
    # Core relevant logic begins here
    clean_data = preprocess_signal(system_state)
    
    # Distractor: unused transformation
    temp_analysis = [math.tanh(x / 10) for x in system_state]
    
    # Relevant entropy calculation
    info_entropy = compute_entropy(clean_data)
    
    # Distractor: spike detection not used in final result
    spike_locations = detect_spikes(clean_data, sensitivity=0.75)
    spatial_map = transform_coordinates(spike_locations)
    
    # Conditional expression (required Python feature)
    adjustment_factor = 1.5 if info_entropy > 2.0 else 0.8
    
    # Simulated recursive diagnosis with partial relevance
    recursion_seed = [int(abs(x)) for x in clean_data[:5]]
    diagnostic_score = recursive_diagnose(recursion_seed, depth=3)
    
    # Unused risk evaluation (dead path)
    fake_risks = [info_entropy * 2, diagnostic_score / 2, len(spatial_map)]
    _ = evaluate_stability(fake_risks)
    
    # Actual core computation
    base_metric = sum(clean_data) * adjustment_factor
    penalty = 0
    for val in clean_data:
        if val > 10:
            penalty += val * 0.1
    final_diagnostic = int(base_metric - penalty + diagnostic_score)
    
    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input data with realistic domain context (sensor readings)
    sensor_readings = [23, -15, 44, 18, -7, 39, 12, -22, 51, 65, -30, 14, 8, 27]
    thresholds = {"high": 40, "low": -20, "entropy_cap": 3.5}
    
    # Irrelevant preprocessing
    scaled_readings = [x * 1.05 for x in sensor_readings]
    sorted_readings = sorted(scaled_readings, reverse=True)
    avg_val = sum(sorted_readings) / len(sorted_readings)
    deviation = math.sqrt(sum((x - avg_val) ** 2 for x in scaled_readings) / len(scaled_readings))
    
    # Key statement
    final_diagnostic = analyze_metrics(sensor_readings, thresholds)