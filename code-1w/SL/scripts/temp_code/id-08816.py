import math

# Simulated sensor data processing pipeline with diagnostic logic
def collect_samples():
    raw = [i * 0.5 for i in range(20)]
    offset = sum(raw) / len(raw)
    return [x + offset for x in raw]

def apply_filter(data):
    filtered = []
    for x in data:
        if x > 5.0:
            filtered.append(math.sin(x) * math.cos(x))
        else:
            filtered.append(math.tan(x) if x != 0 else 0)
    return filtered

def generate_checksum(sequence):
    # Irrelevant checksum calculation (dead-end function)
    chk = 0
    for val in sequence:
        chk = (chk + int(abs(val) * 100)) % 257
    return chk

def normalize_signal(signal):
    max_val = max(abs(min(signal)), abs(max(signal)))
    return [s / max_val if max_val != 0 else 0 for s in signal]

def encode_sequence(norm_seq):
    # Distractor: encoding not used in final result
    encoded = []
    for x in norm_seq:
        if x >= 0:
            encoded.append(hex(int(x * 255))[2:])
        else:
            encoded.append('ff')
    return encoded

def calculate_entropy(data):
    # Misleading intermediate metric
    hist = {}
    for x in data:
        bin_x = round(x, 1)
        hist[bin_x] = hist.get(bin_x, 0) + 1
    total = len(data)
    entropy = 0
    for count in hist.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def build_threshold_map(config_level=3):
    # Complex but relevant threshold structure
    base = {'low': 0.1, 'mid': 0.4, 'high': 0.8}
    multipliers = [0.9 + i*0.2 for i in range(config_level)]
    enhanced = {}
    for key in base:
        values = [base[key] * m for m in multipliers]
        enhanced[key] = sum(values) / len(values)
    return enhanced

def transform_features(filtered):
    # Feature engineering with red herrings
    features = {
        'rms': math.sqrt(sum(x**2 for x in filtered) / len(filtered)),
        'peak': max(abs(x) for x in filtered),
        'zero_crossings': sum(1 for i in range(1, len(filtered)) if filtered[i]*filtered[i-1] < 0),
        'spectral_centroid': sum(i * abs(filtered[i]) for i in range(len(filtered))) / sum(abs(x) for x in filtered) if sum(abs(x) for x in filtered) != 0 else 0
    }
    # Unused feature expansions
    dummy_features = []
    for i in range(3):
        dummy = {'level': i, 'noise_floor': math.exp(-i), 'dummy_flag': False}
        dummy_features.append(dummy)
    return features

def validate_integrity(data_block, sig_key='rms'):
    # Distraction: validation not tied to final output
    ref = {'rms': 0.6, 'tolerance': 0.15}
    feat = transform_features(data_block)
    valid = abs(feat[sig_key] - ref['rms']) <= ref['tolerance']
    return 'VALID' if valid else 'INVALID'

def recursive_smooth(arr, depth=0):
    # Superfluous recursive smoothing (not used)
    if depth >= 2 or len(arr) < 2:
        return arr
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        smoothed.append((arr[i-1] + arr[i] + arr[i+1]) / 3)
    smoothed.append(arr[-1])
    return recursive_smooth(smoothed, depth + 1)

def analyze_signal(processed, thresholds):
    # Core analysis logic
    magnitude = sum(abs(x) for x in processed)
    activity = sum(1 for x in processed if abs(x) > thresholds['mid'])
    suppression = sum(1 for x in processed if abs(x) < thresholds['low'])
    ratio = activity / (suppression + 1e-8)
    score = magnitude * ratio
    
    # Conditional expression determining final outcome
    adjustment = 1.25 if score > thresholds['high'] * 15 else 0.78
    diagnostic_value = score * adjustment
    
    # Final computation step
    final_score = int(diagnostic_value) + (50 if len(processed) % 2 == 1 else 0)
    
    # Irrelevant branching affecting unused variable
    log_entry = f"Diagnostic level {'elevated' if final_score > 100 else 'normal'}"
    metadata_flag = True
    
    return final_score

# --- Main Execution ---
data_stream = collect_samples()
cleaned = apply_filter(data_stream)
processed_data = normalize_signal(cleaned)

# Unused branches and variables (distractors)
checksum = generate_checksum(cleaned)
entropy_metric = calculate_entropy(processed_data)
encoded_data = encode_sequence(processed_data)
validation_status = validate_integrity(cleaned)
smoothed_recursive = recursive_smooth(processed_data)

threshold_map = build_threshold_map(config_level=3)

# Key statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")