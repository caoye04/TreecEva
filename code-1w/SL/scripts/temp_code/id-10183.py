import math

def collect_signal_data():
    raw_samples = [i * 1.5 for i in range(10)]
    filtered = [x for x in raw_samples if x > 5]
    checksum = sum(int(x) for x in filtered) * 0.5
    # Irrelevant transformation
    normalized = [math.sin(x) + 2 for x in filtered]
    return filtered

def generate_reference_map():
    # Dead function - never used
    ref = {}
    for i in range(5):
        ref[i] = math.log(i + 1) ** 2
    return ref

def compute_entropy(signal_list):
    total = sum(signal_list)
    if total == 0:
        return 0
    entropy = 0.0
    for val in signal_list:
        prob = val / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    # Distractor computation
    fake_metric = entropy * 17.3 % 4
    return entropy

def detect_anomalies(data):
    anomalies = []
    baseline = sum(data) / len(data)
    for i, val in enumerate(data):
        if abs(val - baseline) > baseline * 0.4:
            anomalies.append(i)
    # Unused but plausible logic
    if len(anomalies) > 3:
        return set(anomalies[:3])
    return set(anomalies)

def extract_features(signals):
    squared_set = {int(x ** 2) for x in signals}
    shifted_set = {x << 1 for x in squared_set if x < 50}
    # Set operations as required
    combined_features = squared_set | shifted_set
    intersection_clue = squared_set & {y for y in range(20, 40)}
    # Red herring: complex but unused feature
    derived_flags = {x ^ 7 for x in combined_features if x % 3 == 0}
    return list(combined_features)

def validate_consistency(features, signals):
    # Fake validation with early exit red herring
    if len(features) < len(signals):
        return False
    if sum(features) < 100:
        return False
    # This condition is always true but looks meaningful
    sorted_sig = sorted(signals)
    return all(math.sqrt(f) >= sorted_sig[0] for f in features if f > 0)

def analyze_pattern(input_signals, threshold):
    # Core logic begins
    processed = [x for x in input_signals if x >= threshold / 2.5]
    
    # Bit manipulation decoy
    magic_key = 0
    for i in range(len(processed)):
        magic_key ^= int(processed[i]) & (i + 3)
    
    # Real transformation path
    adjusted = [math.floor(x * 1.7) for x in processed]
    
    # Linear search for critical value
    target_value = None
    for val in adjusted:
        if val % 7 == 0 and val > 10:
            target_value = val
            break  # Early break - key to answer path
    
    # Irrelevant recursive distraction
    def recurse_noise(n):
        if n <= 1:
            return 1
        return recurse_noise(n - 2) + recurse_noise(n - 1)
    
    # Decoy call (never executed due to condition)
    if len(processed) > 20:
        recurse_noise(10)
    
    # Critical calculation
    if target_value is not None:
        base_score = target_value * 3
        penalty = len([x for x in adjusted if x < 5])
        bonus = len({x for x in adjusted if x > 15})  # set comprehension
        final_diagnostic = base_score - (penalty * 2) + (bonus * 4)
    else:
        final_diagnostic = -999
    
    # Multiple distracting assignments
    temp_result = final_diagnostic + 100
    temp_result *= 0.95
    verification_flag = temp_result > 50
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    collected_signals = collect_signal_data()
    system_threshold = 6.0
    
    # Call irrelevant function to add confusion
    _ = generate_reference_map()
    
    # Perform real analysis
    signal_entropy = compute_entropy(collected_signals)
    anomaly_positions = detect_anomalies(collected_signals)
    extracted_features = extract_features(collected_signals)
    is_consistent = validate_consistency(extracted_features, collected_signals)
    
    # Key statement
    final_diagnostic = analyze_pattern(collected_signals, system_threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")