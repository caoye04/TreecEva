import math

# Simulated sensor data and calibration constants (some are decoys)
def load_sensor_data():
    raw_values = [0.78, 1.21, 0.94, 2.05, 1.88, 0.43, 1.12]
    calibration_offset = 0.107  # unused red herring
    scaling_factor = 1.05         # unused red herring
    return raw_values

# Irrelevant auxiliary function – dead code path
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Misleading preprocessing with unused branches
def preprocess(signal, mode='active'):
    filtered = []
    temp_log = []
    
    for val in signal:
        if val < 0.5:
            continue  # skip low noise
        elif val > 1.5:
            adjusted = val * 0.9
        else:
            adjusted = val * 1.1
        
        # Redundant transformation
        transformed = round(adjusted ** 2, 3)
        temp_log.append(transformed)  # logged but not used later
        
        filtered.append(adjusted)
    
    # Distractor: complex but unused list comprehension
    normalized = [x / sum(filtered) for x in filtered if x > 1.0]  # never used
    
    return filtered

# Core logic buried among distractions
def extract_features(dataset):
    magnitude = sum(x**2 for x in dataset)
    peak = max(dataset)
    count_above_threshold = len([x for x in dataset if x > 1.0])
    
    # Real feature used downstream
    return {
        'rms': math.sqrt(magnitude / len(dataset)),
        'peaks': count_above_threshold,
        'stability': 1 if peak < 2.0 else 0
    }

# Decoy analysis function that looks important but is never called
def legacy_diagnostic(seq):
    a, b, c = seq[0], seq[2], seq[-1]
    return (a + b) * c - sum(seq) // len(seq)

# Lambda-based dynamic filter – actually used
adaptive_threshold = lambda readings, base: [r for r in readings if r > base]

# Main analysis with nested logic and multiple concepts
def analyze_signal(data):
    # Step 1: Apply dynamic threshold using lambda
    relevant = adaptive_threshold(data, 0.85)
    
    # Step 2: Extract meaningful features
    features = extract_features(relevant)
    
    # Step 3: Simulate hardware feedback loop (distractor variables)
    feedback_cycle = 0
    signal_lock = False
    while feedback_cycle < 3:
        if features['stability']:
            signal_lock = True
        feedback_cycle += 1
    # signal_lock is never used beyond here
    
    # Step 4: Calculate diagnostic score (actual answer path)
    weight_rms = 128.0
    weight_peaks = 17.5
    adjustment = 0.0
    
    # Bit manipulation to obfuscate simple arithmetic
    adjustment += (int(weight_rms) & 15)  # 128 & 15 = 0
    adjustment += (int(weight_peaks * 2) >> 2)  # 35 >> 2 = 8
    
    # Critical calculation hidden in distraction
    raw_score = features['rms'] * weight_rms + features['peaks'] * weight_peaks + adjustment
    
    # Final mapping through conditional chain
    if features['stability'] == 0:
        final_value = int(raw_score - 12.3)
    else:
        decay = 0.98 ** len(data)  # minor effect
        final_value = int(raw_score * decay)
    
    return final_value

# --- Execution Sequence ---
if __name__ == "__main__":
    # Load raw sensor input
    sensor_stream = load_sensor_data()
    
    # Preprocess with irrelevant side effects
    processed_data = preprocess(sensor_stream)
    
    # Perform entropy analysis (unused result)
    entropy_metric = compute_entropy(processed_data)  # red herring
    
    # Key statement: analyze the preprocessed signal
    final_diagnostic = analyze_signal(processed_data)
    
    # Output target result
    print(f"Result: {final_diagnostic}")