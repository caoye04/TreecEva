from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def fetch_raw_samples():
    return [14, 17, 14, 23, 17, 14, 17, 23, 14, 17, 14, 23, 17, 14]

def apply_noise_filter(samples):
    filtered = []
    for x in samples:
        if x % 2 == 1:
            filtered.append(x - 1)
        else:
            filtered.append(x)
    return filtered

def compute_amplitude_envelope(signal):
    envelope = []
    for i in range(1, len(signal) - 1):
        env_val = (signal[i-1] + signal[i] + signal[i+1]) / 3
        envelope.append(int(env_val))
    return [signal[0]] + envelope + [signal[-1]]

def generate_frequency_bins(data):
    bins = defaultdict(int)
    for val in data:
        bin_key = val // 5
        bins[bin_key] += 1
    return bins

def calculate_entropy(dist):
    total = sum(dist.values())
    entropy = 0.0
    for freq in dist.values():
        p = freq / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def derive_calibration_sequence(base_values):
    # Irrelevant calibration logic - dead end
    seq = []
    for v in base_values:
        seq.append((v * 17) % 23)
    return seq[::-1]

def validate_consistency(trace):
    # Misleading validation that isn't used in final result
    if len(trace) < 10:
        return False
    checksum = sum(trace[i] * (i + 1) for i in range(len(trace)))
    return checksum % 107 == 0

def build_transition_matrix(seq):
    matrix = defaultdict(lambda: defaultdict(int))
    for i in range(len(seq) - 1):
        curr, nxt = seq[i], seq[i+1]
        matrix[curr][nxt] += 1
    return matrix

def evaluate_stability_index(transitions):
    index = 0
    for src in transitions:
        if len(transitions[src]) == 1:
            index += 1
    return index

def analyze_signal(data, thresholds):
    # Core analysis logic
    count_by_value = Counter(data)
    dominant = count_by_value.most_common(1)[0][1]
    
    # Compute weighted score based on threshold crossings
    score = 0
    for val in data:
        for t in thresholds:
            if val > t:
                score += t % 7
    
    # Actual answer derivation
    stability_proxy = len(data) - abs(dominant - len(thresholds))
    final_score = (score * dominant) - (stability_proxy ** 2)
    return final_score

def main():
    # Step 1: Fetch raw sensor readings
    raw_readings = fetch_raw_samples()
    
    # Step 2: Filter odd-numbered noise artifacts
    clean_signal = apply_noise_filter(raw_readings)
    
    # Step 3: Smooth with moving average envelope
    processed_data = compute_amplitude_envelope(clean_signal)
    
    # Step 4: Generate frequency distribution bins (distractor)
    freq_distribution = generate_frequency_bins(processed_data)
    entropy_metric = calculate_entropy(freq_distribution)
    
    # Step 5: Build unused transition graph (red herring)
    decoy_sequence = derive_calibration_sequence(processed_data)
    is_valid = validate_consistency(decoy_sequence)
    trans_matrix = build_transition_matrix(processed_data)
    stability_index = evaluate_stability_index(trans_matrix)
    
    # Step 6: Create threshold map based on data characteristics (used)
    threshold_map = []
    for i in range(3):
        threshold_map.append((processed_data[i] + processed_data[-(i+1)]) // 2)
    
    # Step 7: Perform final diagnostic analysis (KEY STATEMENT)
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()