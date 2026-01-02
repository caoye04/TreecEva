import itertools

# Simulated sensor data from multiple sources
def generate_sensor_readings():
    base_sequence = [0.8, 1.2, 0.9, 1.5, 1.1]
    readings = []
    for i in range(5):
        shifted = [x + i * 0.1 for x in base_sequence]
        readings.append(shifted)
    return readings

# Irrelevant transformation: frequency shifting (dead path)
def apply_frequency_shift(signal, shift_factor=1.0):
    return [val * shift_factor for val in signal]

# Unused helper: spectral decomposition (decoy function)
def decompose_spectrum(signal):
    result = []
    for i in range(len(signal)):
        component = 0
        for j in range(len(signal)):
            component += signal[j] * (i + j) % 3
        result.append(component)
    return result

# Core diagnostic logic
def compute_coherence_index(seq1, seq2):
    index = 0
    for a, b in zip(seq1, seq2):
        if abs(a - b) < 0.5:
            index += 1
    return index

# Noise level estimator (used only partially)
def estimate_noise_level(data_matrix):
    noise_score = 0
    for row in data_matrix:
        for val in row:
            if val > 1.0:
                noise_score += (val - 1.0) ** 2
    return noise_score * 100

# Key analysis function
def analyze_signal_quality(readings):
    n = len(readings)
    
    # Distractor variables
    temp_cache = {}
    debug_trace = []
    accumulator = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            coherence = compute_coherence_index(readings[i], readings[j])
            key_pair = (i, j)
            temp_cache[key_pair] = coherence
            accumulator += coherence
    
    # Real computation begins here — average coherence
    avg_coherence = accumulator / len(temp_cache) if temp_cache else 0
    
    # Secondary metric: variation stability
    stability_scores = []
    for row in readings:
        mean_val = sum(row) / len(row)
        variance = sum((x - mean_val) ** 2 for x in row) / len(row)
        stability_scores.append(1 / (1 + variance))
    
    avg_stability = sum(stability_scores) / len(stability_scores)
    
    # Tertiary: pattern regularity using itertools
    flat_data = list(itertools.chain.from_iterable(readings))
    diffs = [abs(flat_data[i+1] - flat_data[i]) for i in range(len(flat_data)-1)]
    regularity = sum(1 for d in diffs if d < 0.3) / len(diffs)
    
    # Final diagnostic score — this is the actual answer
    final_diagnostic = (avg_coherence * 2.5) + (avg_stability * 1.8) + (regularity * 1.2)
    
    # Dead code block: entropy calculation (never used)
    def calculate_entropy(values):
        from math import log
        freq_map = {}
        for v in values:
            freq_map[v] = freq_map.get(v, 0) + 1
        total = len(values)
        entropy = 0
        for count in freq_map.values():
            p = count / total
            entropy -= p * log(p, 2)
        return entropy
    
    # Unused set operations (red herring)
    unique_values = set(flat_data)
    outlier_set = {v for v in unique_values if v > 1.4}
    normal_set = {v for v in unique_values if v <= 1.4}
    overlap = outlier_set & normal_set  # Always empty
    
    # Debug logs (no effect)
    debug_trace.append(f'Coherence: {avg_coherence}')
    debug_trace.append(f'Stability: {avg_stability}')
    debug_trace.append(f'Regularity: {regularity}')
    
    # Final result output
    return final_diagnostic

# Main execution flow
sensor_data = generate_sensor_readings()

# Irrelevant pre-processing
shifted_data = apply_frequency_shift(sensor_data[0], 0.95)

# Noise estimation (computed but not used in final result)
noise_diagnosis = estimate_noise_level(sensor_data)

# Actual target computation
final_diagnostic = analyze_signal_quality(sensor_data)

print(f"Result: {final_diagnostic}")