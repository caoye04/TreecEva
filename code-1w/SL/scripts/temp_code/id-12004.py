import math

# Simulated sensor data from environmental monitoring stations
def generate_raw_readings():
    return [14.2, 18.5, 22.1, 19.3, 25.0, 17.8, 20.4, 23.7, 16.9, 21.5]

def filter_outliers(data, threshold=1.8):
    mean = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean) / mean < threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def shift_cipher_encode(text, key=3):
    # Distractor function - not related to main logic
    encoded = ''.join(chr((ord(c) - 97 + key) % 26 + 97) if c.isalpha() else c for c in text.lower())
    return encoded

def detect_peak_clusters(magnitude_series):
    peaks = []
    for i in range(1, len(magnitude_series) - 1):
        if magnitude_series[i] > magnitude_series[i-1] and magnitude_series[i] > magnitude_series[i+1]:
            peaks.append(i)
    return peaks if peaks else [0]

def calculate_phase_shift(amplitude, frequency):
    # Irrelevant computation chain
    phase = (amplitude * frequency) % (2 * math.pi)
    shifted = math.sin(phase) + math.cos(phase * 0.5)
    return round(shifted, 3)

def evaluate_consistency_pattern(sequence):
    consistency_flags = []
    for idx, val in enumerate(sequence[:-1]):
        consistency_flags.append(1 if abs(val - sequence[idx+1]) < 5 else 0)
    return sum(consistency_flags)

def derive_weighted_hierarchy(raw_importance):
    ranked = sorted(enumerate(raw_importance), key=lambda x: x[1], reverse=True)
    weights = [math.exp(-i * 0.2) for i in range(len(ranked))]
    hierarchy_score = sum(weight * raw_importance[idx] for (idx, _), weight in zip(ranked, weights))
    return hierarchy_score

def assess_variance_threshold(dataset, baseline=20):
    variance = sum((x - sum(dataset)/len(dataset))**2 for x in dataset) / len(dataset)
    exceeds = [x for x in dataset if x > baseline + variance**0.5]
    penalty = len(exceeds) * 1.5
    return variance - penalty

def analyze_system_state(metrics_bundle):
    entropy_component = compute_entropy(metrics_bundle['normalized_levels'])
    peak_influence = len(metrics_bundle['peak_positions']) * 10
    consistency_bonus = evaluate_consistency_pattern(metrics_bundle['normalized_levels'])
    hierarchy_factor = derive_weighted_hierarchy(metrics_bundle['normalized_levels'])
    raw_equilibrium = entropy_component + peak_influence + consistency_bonus
    adjustment = assess_variance_threshold(metrics_bundle['normalized_levels'])
    final_score = raw_equilibrium - adjustment + (hierarchy_factor * 0.01)
    return int(round(final_score))

# Main execution flow
if __name__ == "__main__":
    # Step 1: Acquire initial environmental readings
    sensor_output = generate_raw_readings()
    
    # Step 2: Process and normalize data (key preprocessing)
    cleaned_data = filter_outliers(sensor_output)
    
    # Step 3: Detect significant fluctuation peaks (used later)
    critical_peaks = detect_peak_clusters(cleaned_data)
    
    # Irrelevant side computation - simulates signal processing but unused
    dummy_signal = [calculate_phase_shift(x, 2.5) for x in cleaned_data]
    
    # Step 4: Encrypt log metadata (red herring - no impact on result)
    log_id = "envlog_2023"
    encrypted_key = shift_cipher_encode(log_id, 7)
    
    # Step 5: Prepare metric bundle for analysis
    metrics = {
        'raw_readings': sensor_output,
        'normalized_levels': cleaned_data,
        'peak_positions': critical_peaks,
        'timestamp_sequence': list(range(len(cleaned_data)))
    }
    
    # Step 6: Analyze system state - this is where equilibrium_score is computed
    equilibrium_score = analyze_system_state(metrics)
    
    # Step 7: Perform irrelevant sorting operation (dead code path)
    sorted_copy = sorted(cleaned_data, reverse=True)
    alternate_sum = sum(sorted_copy[i] for i in range(0, len(sorted_copy), 2))
    
    # Step 8: Generate decoy report using unused functions
    dummy_entropy = compute_entropy([10, 20, 30])
    hidden_adjustment = calculate_phase_shift(5.5, 1.1)
    
    # Output the target result
    print(f"Result: {equilibrium_score}")