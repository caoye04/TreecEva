import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(data_stream):
    scaled = [x * 1.5 for x in data_stream]
    offset = [x + 10 for x in scaled]  # Distractor: not used later
    filtered = [x for x in offset if x > 15]
    return filtered

# Irrelevant transformation path (dead end)
def legacy_normalize(arr):
    mean_val = sum(arr) / len(arr)
    return [round((x - mean_val) / mean_val, 3) for x in arr]

# Core transformation function used in logic chain
def apply_window(signal, window_size=3):
    result = []
    for i in range(len(signal) - window_size + 1):
        window_avg = sum(signal[i:i+window_size]) / window_size
        result.append(round(window_avg, 4))
    return result

# Decoy function that looks important but isn't called
def calculate_entropy(sequence):
    from math import log
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count/total) * log(count/total, 2) for count in freq_map.values())
    return round(entropy, 4)

# Bit manipulation red herring
def encode_flags(mode, debug=False):
    base = mode << 4
    if debug:
        base |= 1
    return base ^ 255  # Complex but unused

# Main pattern analyzer (critical path)
def analyze_pattern(seq):
    # Count transitions between even and odd
    transitions = 0
    for i in range(len(seq) - 1):
        if (seq[i] % 2) != (seq[i+1] % 2):
            transitions += 1
    
    # Apply recursive reduction on transition count
    def reduce_value(n):
        if n <= 1:
            return n
        return n + reduce_value(n // 2)
    
    reduced = reduce_value(transitions)
    
    # Use lambda to obscure simple mapping
    significance = lambda x: x * 17 if x % 2 else x * 12
    return significance(reduced)

# Secondary decoy analysis
threshold_log = []
def monitor_stability(input_seq):
    avg = sum(input_seq) / len(input_seq)
    stable = all(abs(x - avg) < 0.5 for x in input_seq)
    threshold_log.append(stable)  # Side effect distraction
    return stable

# Generate initial signal using itertools
def generate_basis():
    # Create repeating pattern: 1,2,3,1,2,3,...
    cycle = itertools.cycle([1, 2, 3])
    return [next(cycle) for _ in range(10)]

# Entry point
if __name__ == '__main__':
    raw_signal = generate_basis()  # [1,2,3,1,2,3,1,2,3,1]
    
    # Process through valid pipeline
    processed = preprocess_sensor_readings(raw_signal)  # scaling and filtering
    windowed = apply_window(processed, 3)  # moving average
    
    # Convert to integers to create discrete transitions
    transformed_data = [int(x) for x in windowed]  # becomes [19, 19, 19, 19, 19, 19, 19]
    
    # Dead code branches (distractors)
    normalized = legacy_normalize(processed)
    flags = encode_flags(5, debug=True)
    stability = monitor_stability(windowed)
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")