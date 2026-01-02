from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring
def acquire_raw_readings():
    return [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def apply_calibration(raw_data, factor=1.05):
    # Irrelevant calibration path with unused branches
    if len(raw_data) > 20:
        return [x * 1.1 for x in raw_data]
    elif len(raw_data) % 3 == 0:
        return [x * 1.08 for x in raw_data]
    else:
        return [x * factor for x in raw_data]

def filter_outliers(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    threshold = 1.5 * std_dev
    # Misleading: computes bounds but uses fixed threshold instead
    upper = mean + threshold
    lower = mean - threshold
    return [x for x in data if 5 < x < 25]  # Hardcoded range bypasses computed stats

def generate_frequency_map(values):
    # Complex distractor: builds map not directly used in final result
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
        if v % 2 == 0:
            freq['even'] += 1
        else:
            freq['odd'] += 1
    return freq

def extract_peaks(signal):
    # Unused function - dead code path
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def compute_entropy(data):
    # Decoy computation with no impact on final answer
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def transform_signal(readings):
    # Key transformation with embedded distractions
    squared = [x**2 for x in readings]
    shifted = [x >> 1 for x in squared]  # Bitwise distraction
    masked = [x & 0xFF for x in shifted]  # More bit noise
    # Actual relevant operation buried here:
    adjusted = [x // 10 for x in masked]  # Integer division critical to result
    return adjusted

def phase_modulate(sequence):
    # Red herring function with complex logic but no real use
    modulated = []
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            modulated.append(val + (i * 2))
        else:
            modulated.append(val - i)
    return modulated

def analyze_readings(processed):
    # Core analysis with one key variable
    base_score = sum(processed)
    penalty = 0
    
    # Distracting conditional block
    if any(x > 100 for x in processed):
        penalty += 10
    elif len(processed) > 20:
        penalty += 5
    else:
        penalty = 2  # Fixed penalty actually applied
    
    # Another decoy counter
    distribution = Counter(processed)
    mode_count = distribution.most_common(1)
    
    # Critical calculation hidden among noise
    aggregate = base_score - penalty
    
    # Multiple assignments to obscure flow
    temp_result = aggregate * 3
    normalized = temp_result // 2
    final_diagnostic = normalized ^ 42  # Final XOR twist
    
    # Dead assignment
    final_diagnostic = final_diagnostic + 0  # No-op
    
    return final_diagnostic

# Main execution sequence
def main_pipeline():
    # Step 1: Acquire data
    raw_sensor_data = acquire_raw_readings()  # [3,5,7,11,13,17,19,23,29,31]
    
    # Step 2: Apply irrelevant calibration
    calibrated = apply_calibration(raw_sensor_data, 1.05)
    
    # Step 3: Filter outliers (actually trims to [5,7,11,13,17,19])
    filtered = filter_outliers(calibrated)
    
    # Step 4: Generate useless frequency map
    freq_map = generate_frequency_map(filtered)
    
    # Step 5: Compute decoy entropy
    entropy_value = compute_entropy(filtered)
    
    # Step 6: Transform signal (key step)
    processed_signals = transform_signal(filtered)  # Becomes [2,4,12,16,28,36]
    
    # Step 7: Phase modulation (dead path)
    modulated_output = phase_modulate(processed_signals)
    
    # Step 8: Analyze readings (final computation)
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main_pipeline()