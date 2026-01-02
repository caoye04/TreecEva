import math

def preprocess_segment(segment):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in segment]

def calculate_entropy(data):
    # Misleading statistical distraction
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def shift_window(sequence, offset):
    # Unused circular shift operation (distractor)
    return sequence[offset:] + sequence[:offset]

def evaluate_health_status(metrics):
    # Decoy health evaluation with red herring logic
    baseline = 75.0
    adjustment = 0
    for val in metrics:
        if val > baseline:
            adjustment += 1.5
        else:
            adjustment -= 0.8
    return adjustment  # Not used in main logic

def filter_anomalies(log_entries):
    # Irrelevant log filtering based on string patterns
    keywords = ['ERROR', 'WARNING']
    return [entry for entry in log_entries if any(k in entry for k in keywords)]

def analyze_signal(data, limit):
    magnitude = sum(x ** 2 for x in data) ** 0.5
    normalized = [x / magnitude for x in data]
    
    # Apply windowing (relevant but masked by distractions)
    window = [0.5 - 0.5 * math.cos(2 * math.pi * i / len(data)) for i in range(len(data))]
    weighted = [normalized[i] * window[i] for i in range(len(data))]
    
    # Compute spectral centroid approximation
    power_spectrum = [abs(x) ** 2 for x in weighted]
    centroid_num = sum(i * power_spectrum[i] for i in range(len(power_spectrum)))
    centroid_den = sum(power_spectrum)
    spectral_centroid = centroid_num / centroid_den if centroid_den != 0 else 0
    
    # Key conditional branch affecting final result
    if spectral_centroid > limit:
        scale_factor = 2.3
    else:
        scale_factor = 1.7
    
    # Final transformation using slicing and string-based key (hybrid)
    hex_key = ''.join([hex(int(abs(w * 100)))[-1] for w in weighted[-5:]])  # Last 5 weights -> hex digits
    checksum = sum(ord(c) - ord('a') for c in hex_key if c.isalpha()) + sum(int(c) for c in hex_key if c.isdigit())
    
    intermediate = scale_factor * (spectral_centroid + checksum / 10.0)
    
    # Destructuring distraction (tuple unpacking with irrelevant vars)
    (*_, a, b), [*ignored, c] = weighted[:3], power_spectrum[::2]
    dummy_score = a * c + b
    
    # Final computation
    result = int(intermediate * 1000) % 97  # Normalize to manageable integer
    return result

# Main execution with multiple distractions
raw_signal = [12.3, -8.7, 15.2, 3.9, -11.4, 7.6, 13.1, -9.8, 6.2, 10.5]
log_messages = ['INFO: startup', 'WARNING: low buffer', 'DEBUG: calibrating', 'ERROR: timeout']
diagnostic_codes = {'A': 10, 'B': 20, 'C': 30}

# Real processing begins here
filtered_data = [x for x in raw_signal if abs(x) > 9.0]  # Filter by amplitude

threshold = 4.8

# Unused transformations (red herrings)
cleaned_logs = filter_anomalies(log_messages)
entropy = calculate_entropy(raw_signal)
rotated = shift_window(raw_signal, 3)
eval_result = evaluate_health_status([10, 20, 30])

# Critical statement
final_diagnostic = analyze_signal(filtered_data, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")