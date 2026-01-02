from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulate sensor data stream with embedded patterns
def generate_noisy_signal(length=200, seed=13):
    signal = []
    for i in range(length):
        base = (i % 17) * 0.5
        noise = (i % 9) * 0.1
        spike = 2.5 if i % 43 == 0 else 0
        signal.append(base + noise + spike)
    return signal

def apply_window_filter(data, window_size=5):
    filtered = []
    for i in range(len(data)):
        start = max(0, i - window_size // 2)
        end = min(len(data), i + window_size // 2 + 1)
        window_avg = sum(data[start:end]) / (end - start)
        filtered.append(round(window_avg, 3))
    return filtered

def extract_frequency_peaks(signal, threshold=1.8):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i % 25)  # Normalize position
    return list(set(peaks))  # Remove duplicates

def compute_checksum(sequence):
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= (val * (idx + 1))  # Bitwise mix with position
    return checksum & 0xFFFF  # Limit to 16 bits

def transform_to_diagnostics(raw_series):
    # Irrelevant transformation branch (dead logic path)
    temp_buffer = [x * 1.05 for x in raw_series if x > 1.0]
    temp_stats = defaultdict(float)
    for x in temp_buffer:
        temp_stats['sum'] += x
        temp_stats['count'] += 1
    if temp_stats['count'] > 0:
        temp_stats['mean'] = temp_stats['sum'] / temp_stats['count']
    
    # Actual relevant transformation
    scaled = [int(x * 10) % 100 for x in raw_series]
    count_freq = Counter(scaled)
    frequent_values = [k for k, v in count_freq.items() if v >= 2]
    sorted_frequent = sorted(frequent_values)
    
    # Decoy computation with misleading intermediate result
    decoy_result = sum([v * v for v in count_freq.values()]) // 10
    dummy_mask = [1 if i in {2, 3, 5, 7, 11} else 0 for i in range(15)]
    masked_output = [decoy_result & mask for mask in dummy_mask]
    
    return sorted_frequent

def generate_control_sequence(seed_vals, length=10):
    seq = []
    a, b = seed_vals
    for _ in range(length):
        next_val = (a + b) % 100
        seq.append(next_val)
        a, b = b, next_val
    return seq

def analyze_pattern(pattern_list, control):
    # Complex conditional analysis with red herring branches
    if len(pattern_list) < 5:
        return -sum(pattern_list) * 100
    
    match_score = 0
    for p in pattern_list:
        if p in control:
            match_score += p * 3
        elif p % 7 == 0:
            match_score += p * 2
        else:
            match_score -= p // 4
    
    # Distractor: elaborate but unused structure
    analysis_log = defaultdict(list)
    for i, c in enumerate(control):
        analysis_log['control_trace'].append((i, c, c % 3))
        if c % 4 == 0:
            analysis_log['quadrants'].append(i)
    
    # Secondary irrelevant aggregation
    phantom_sum = sum([i * j for i, j in zip(control, control[1:])])
    buffer_check = ''.join(map(str, control[:4]))
    
    # Final logic that actually matters
    adjustment_factor = len(pattern_list) - len(control)
    final_score = match_score + (adjustment_factor * 7)
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Step 1: Generate base signal
    raw_sensor_data = generate_noisy_signal(length=200, seed=13)
    
    # Step 2: Apply smoothing filter
    filtered_data = apply_window_filter(raw_sensor_data, window_size=5)
    
    # Step 3: Extract peak positions (not directly used but looks important)
    significant_peaks = extract_frequency_peaks(filtered_data, threshold=1.8)
    peak_checksum = compute_checksum(significant_peaks)
    
    # Step 4: Transform data into diagnostic format
    transformed_data = transform_to_diagnostics(filtered_data)
    
    # Step 5: Generate control sequence using Fibonacci-like generator
    control_sequence = generate_control_sequence(seed_vals=(11, 18), length=10)
    
    # Step 6: Perform final analysis (key statement)
    final_diagnostic = analyze_pattern(transformed_data, control_sequence)
    
    # Output result
    print(f"Result: {final_diagnostic}")