from collections import defaultdict
import math

# Simulated sensor data processing with diagnostic analysis
def generate_pattern_sequence(raw_input):
    sequence = []
    for i in range(len(raw_input)):
        if raw_input[i] % 3 == 0:
            sequence.append((raw_input[i] ** 2) % 17)
    return sequence

# Irrelevant helper: converts numbers to string patterns (dead path)
def number_to_code(n):
    mapping = 'abcdefghij'
    return ''.join([mapping[int(d) % 10] for d in str(n)])

# Decoy function: looks important but unused in critical path
def compute_entropy(data):
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

# Data normalization (used but partially obfuscated by distractors)
def normalize_values(arr, factor=1.0):
    if factor == 0:
        return [0] * len(arr)
    return [round(x / factor, 6) for x in arr]

# Core signal analysis with red herring computations
def analyze_signal(buffer, thresholds):
    temp_result = 0
    history = []
    decoy_sum = 0  # Distractor accumulator

    for i, val in enumerate(buffer):
        # Real logic branch
        if i % 2 == 0 and val > thresholds.get('high', 10):
            temp_result += val * 2
        elif val > thresholds.get('mid', 5):
            temp_result += val // 3
        
        # Dead computation: builds a list but never used
        shift_val = (val << 2) ^ 5
        decoy_sum += shift_val % 9
        history.append(shift_val * 0.1)

        # Early termination red herring
        if temp_result > 1000:
            break  # This never triggers due to data range

    # Real result transformation
    final_score = abs(temp_result - 42) * 3
    
    # Another decoy: complex string manipulation off history
    label = ''.join([str(int(h * 10)) for h in history if h > 0.5])
    if len(label) > 5:
        label = label[::-1][:5]
    
    # Final diagnostic depends only on core numeric logic
    final_diagnostic = final_score + 11
    return final_diagnostic

# --- Main execution with distractions ---
if __name__ == "__main__":
    # Real input data
    sensor_readings = [12, 7, 15, 3, 9, 18, 6, 11, 14, 8, 10]
    
    # Irrelevant pre-processing chain
    processed_strings = [number_to_code(x) for x in sensor_readings]
    reversed_codes = [s[::-1] for s in processed_strings if len(s) > 1]
    
    # Real pattern generation
    pattern_buffer = generate_pattern_sequence(sensor_readings)
    
    # Distractor data structures
    stats_summary = {
        'max': max(sensor_readings),
        'min': min(sensor_readings),
        'range': max(sensor_readings) - min(sensor_readings),
        'mode_guess': 12  # incorrect guess
    }
    
    # Real threshold map
    threshold_map = defaultdict(int)
    threshold_map['high'] = 13
    threshold_map['mid'] = 6
    threshold_map['low'] = 2
    
    # Normalization that's not used in final calculation
    normalized_buffer = normalize_values(pattern_buffer, factor=5.5)
    entropy_value = compute_entropy(pattern_buffer)  # Computed but irrelevant
    
    # Key statement
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")