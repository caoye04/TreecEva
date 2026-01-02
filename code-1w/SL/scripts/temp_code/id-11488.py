def preprocess_signal(raw_samples, gain):
    amplified = [int(x * gain) for x in raw_samples]
    filtered = [x for x in amplified if x > 10 or x < -10]
    normalized = [x / max(max(filtered), -min(filtered)) for x in filtered] if filtered else [0]
    return normalized


def detect_peaks(signal, sensitivity=0.5):
    peak_indices = []
    for i in range(1, len(signal) - 1):
        if signal[i] > sensitivity and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peak_indices.append(i)
    return peak_indices if peak_indices else [0]


def compute_entropy(values):
    from collections import Counter
    counts = Counter([round(v, 1) for v in values])
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simulated approximation
    return round(entropy, 6)


def shift_cipher(text, shift):
    # Distractor function: used nowhere in main logic
    return ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.isalpha() else c for c in text.lower())


def evaluate_stability(metric):
    # Irrelevant auxiliary function
    if metric < 0:
        return "Unstable"
    elif metric < 0.5:
        return "Marginal"
    else:
        return "Stable"


def analyze_signal(data, limit):
    magnitude = sum(abs(x) for x in data)
    avg_magnitude = magnitude / len(data) if data else 0
    
    # Conditional expression usage (required feature)
    adjustment = 2.5 if avg_magnitude > limit else 1.2
    
    score = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            score += val ** 2
        elif i % 4 == 0:
            score -= abs(val)
        else:
            score += int(val * adjustment) & 7  # Bitwise AND as noise
    
    # Complex nested condition with red herring variables
    diagnostic_weight = 0
    temp_flag = False
    if len(data) > 5:
        if avg_magnitude > 1.0:
            if compute_entropy(data) > -1.0:
                temp_flag = True
                diagnostic_weight = 1.8
            else:
                diagnostic_weight = 0.4
        else:
            diagnostic_weight = 0.1
    else:
        diagnostic_weight = 0.05
    
    # Dead code path - never executed due to structure
    redundant_buffer = []
    for _ in range(3):
        redundant_buffer.extend([0] * 5)
    if temp_flag and False:  # Never true
        cleanup = [x for x in redundant_buffer if x != 0]
        diagnostic_weight *= 0.9
    
    final_score = score * diagnostic_weight
    
    # Key computation hidden among distractions
    outlier_count = sum(1 for x in data if abs(x) > 2.0)
    correction_factor = 1 + (outlier_count / len(data)) if data else 1
    final_diagnostic = int(final_score * correction_factor)
    
    return final_diagnostic

# Main execution flow
raw_data_stream = [0.1, 1.3, -2.1, 0.9, 3.2, -1.4, 0.8, 2.5]
gain_factor = 2.0
processed_data = preprocess_signal(raw_data_stream, gain_factor)

# Unused intermediate results (distractors)
peak_locations = detect_peaks(processed_data, sensitivity=0.8)
signal_entropy = compute_entropy(processed_data)
stability_status = evaluate_stability(signal_entropy)
encoded_tag = shift_cipher("diagnostic", 7)

threshold = 1.5
final_diagnostic = analyze_signal(processed_data, threshold)

Result: {final_diagnostic}