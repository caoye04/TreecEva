from collections import defaultdict
from itertools import cycle

# Simulated sensor readings and calibration data
def get_sensor_data():
    return [14, 17, 23, 14, 23, 19, 17, 23, 14]

def calibrate_readings(raw):
    counts = defaultdict(int)
    for val in raw:
        counts[val] += 1
    # Misleading transformation
    adjusted = [v * (k ** 0.5) for k, v in counts.items()]
    return sum(adjusted)

def analyze_pattern(seq):
    # Irrelevant pattern analysis with decoy logic
    transitions = 0
    for i in range(len(seq) - 1):
        if seq[i] != seq[i + 1]:
            transitions += 1
    trend_score = 0
    for a, b in zip(seq, seq[1:]):
        trend_score += (b - a) ** 2
    return transitions > 5, trend_score < 30

def compute_entropy(values):
    # Dead code path — never used in final calculation
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def extract_modes(data):
    # Real but indirectly used function
    seen = set()
    modes = []
    for item in data:
        if item in seen and item not in modes:
            modes.append(item)
    return sorted(modes)

def shift_sequence(seq, key):
    # Distractor: complex-looking but unused transformation
    rotated = []
    for i, val in enumerate(seq):
        shifted = val ^ (key * i) % 13
        rotated.append(shifted & 0xF)
    return rotated

def filter_outliers(arr):
    # Seemingly relevant but actually irrelevant filtering
    mean_val = sum(arr) / len(arr)
    dev = [(x - mean_val) ** 2 for x in arr]
    std_dev = (sum(dev) / len(dev)) ** 0.5
    return [x for x in arr if abs(x - mean_val) <= 2 * std_dev]

def adjust_flux(base, flags):
    temp = base
    if flags[0]:
        temp += 11
    if flags[1]:
        temp *= 2
    if flags[2]:
        temp -= (temp // 4)
    return int(temp)

def main():
    # Entry point with multiple distractions
    raw_input = get_sensor_data()
    
    # Irrelevant entropy computation (red herring)
    entropy_metric = compute_entropy(raw_input)
    
    # Meaningful calibration step
    base_flux = calibrate_readings(raw_input)
    
    # Generate misleading intermediate values
    is_complex, is_stable = analyze_pattern(raw_input)
    filtered_data = filter_outliers(raw_input)
    rotated_data = shift_sequence(filtered_data, key=7)
    
    # Extract actual control flags based on repetition pattern
    repeated_values = extract_modes(raw_input)
    mode_flags = [
        len(repeated_values) >= 2,
        17 in repeated_values,
        14 in repeated_values
    ]
    
    # Critical execution point
    final_flux = adjust_flux(base_flux, mode_flags)
    
    # Print required result
    print(f"Result: {final_flux}")

if __name__ == "__main__":
    main()