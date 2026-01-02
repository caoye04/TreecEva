import math

def generate_noise(length, seed=42):
    # Irrelevant function: generates noise but not used in critical path
    result = []
    val = seed
    for i in range(length):
        val = (val * 937 + 17) % 101
        result.append(val / 100)
    return result

def filter_signal(raw_data):
    # Applies a simple moving average filter (red herring: looks important)
    window = 3
    filtered = []
    for i in range(len(raw_data)):
        if i < window - 1:
            filtered.append(raw_data[i])
        else:
            avg = sum(raw_data[i - window + 1:i + 1]) / window
            filtered.append(avg)
    return filtered

def compute_entropy(data):
    # Computes Shannon entropy (distractor: not used in final result)
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_features(signal):
    # Extracts various statistical features (some irrelevant)
    n = len(signal)
    mean_val = sum(signal) / n
    variance = sum((x - mean_val) ** 2 for x in signal) / n
    peak_to_peak = max(signal) - min(signal)
    
    # Distractor variables
    normalized_energy = sum(x**2 for x in signal) / n
    zero_crossings = sum(1 for i in range(1, n) if signal[i] * signal[i-1] < 0)
    
    # Only 'mean_val' and 'peak_to_peak' are actually used later
    return {'mean': mean_val, 'pp': peak_to_peak, 'var': variance}

def process_phase_shift(frequencies):
    # Complex-looking but unused function
    shifted = []
    for f in frequencies:
        shift = math.sin(f * math.pi / 180)
        shifted.append(f + shift)
    return shifted

def simulate_calibration(baseline):
    # Dead code path - never called
    calibrated = [b * 1.05 + 2 for b in baseline]
    return calibrated

def analyze_readings(features_list):
    cumulative_score = 0
    adjustment_factor = 0.87
    
    # List comprehension with filtering (required Python feature)
    significant = [f for f in features_list if f['mean'] > 50 and f['pp'] > 20]
    
    # Another list comprehension (second usage)
    scores = [int(f['mean'] // 10) * int(f['pp'] % 7) for f in significant]
    
    temp_result = 0
    for s in scores:
        if temp_result > 100:  
            break  # Early break (rarely triggered)
        temp_result += s * 2
    
    # Core logic hidden among distractions
    base = sum(scores) if scores else 1
    modifier = len(features_list) - len(significant)
    
    intermediate = base + (modifier ** 2)
    final_value = int(intermediate * adjustment_factor)
    
    # Decoy computation that looks important
    outlier_ratio = len([s for s in scores if s > 50]) / len(scores) if scores else 0
    confidence = math.exp(-abs(modifier)) if modifier != 0 else 1.0
    
    # Final answer depends only on specific chain
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Real data source
    raw_signals = [
        [12, 58, 65, 70, 54],
        [15, 62, 77, 80, 61],
        [10, 45, 50, 48, 60],
        [20, 88, 92, 85, 90],
        [18, 76, 79, 82, 88]
    ]
    
    # Unused variables (distractors)
    noise_profile = generate_noise(50)
    calibration_reference = [100, 200, 150]
    frequency_bands = [50, 60, 100, 120]
    
    processed_signals = []
    for sig in raw_signals:
        filtered = filter_signal(sig)
        features = extract_features(filtered)
        processed_signals.append(features)
    
    # This call contains the key statement
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print required output
    print(f"Result: {final_diagnostic}")