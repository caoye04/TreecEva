from collections import defaultdict, Counter
import math

# Simulated sensor array data processing with diagnostic logic
def collect_sensor_data():
    raw_readings = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    timestamp_map = {i: t * 1.5 for i, t in enumerate(range(10))}
    mode_flag = True
    scaling_factor = 2.0
    adjusted = [x * scaling_factor for x in raw_readings]
    return adjusted

def filter_noise(data, limit=50):
    # Irrelevant filtering path (dead code)
    if len(data) > limit:
        return data[:limit]
    return data

def generate_frequency_profile(values):
    # Distractor function - not used in final computation
    freq = defaultdict(int)
    for v in values:
        freq[int(math.log(v + 1, 2))] += 1
    return freq

def compute_entropy(arr):
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def detect_anomalies(signal_list):
    anomalies = []
    baseline = sum(signal_list) / len(signal_list)
    deviation_scores = []
    for idx, val in enumerate(signal_list):
        score = abs(val - baseline) / baseline
        deviation_scores.append(score)
        if score > 0.6:
            anomalies.append(idx)
    # Decoy result
    max_deviation = max(deviation_scores)
    return anomalies

def reconstruct_sequence(indices, source_data):
    # Unused reconstruction logic (red herring)
    sequence = []
    for i in sorted(indices, reverse=True):
        if i < len(source_data):
            sequence.append(int(source_data[i] // 2))
    return sequence

def analyze_pattern(signal_stream, threshold):
    # Core logic hidden among distractions
    logs = []
    for s in signal_stream:
        if s > threshold:
            logs.append(s % 7)
    
    # Key transformation
    transformed = []
    for x in logs:
        if x != 0:
            transformed.append(x ** 2)
    
    # Critical dependency on set operations
    unique_vals = set(transformed)
    supplement_set = {1, 4, 9, 16, 25}
    intersection = unique_vals & supplement_set  # Shared squares
    
    # Final computation
    base_score = sum(intersection)
    penalty = len([v for v in signal_stream if v < threshold]) // 4
    final_score = base_score - penalty
    
    # Dead code branch - misleading
    if final_score < 0:
        final_score = abs(final_score) * 2
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect sensor signals
    collected_signals = collect_sensor_data()
    
    # Step 2: Irrelevant noise check
    filtered_signals = filter_noise(collected_signals, limit=15)
    
    # Step 3: Generate unused frequency analysis
    profile = generate_frequency_profile(filtered_signals)
    
    # Step 4: Compute decoy entropy (not used later)
    entropy_metric = compute_entropy(filtered_signals)
    
    # Step 5: Detect anomaly indices (used to mislead)
    anomalous_positions = detect_anomalies(filtered_signals)
    
    # Step 6: Reconstruct sequence from anomalies (dead end)
    reconstructed = reconstruct_sequence(anomalous_positions, filtered_signals)
    
    # Step 7: Define threshold and proceed to critical analysis
    system_threshold = 20.0
    
    # Step 8: Execute key statement
    final_diagnostic = analyze_pattern(collected_signals, system_threshold)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")