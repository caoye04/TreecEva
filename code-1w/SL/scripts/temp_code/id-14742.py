import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_signal, noise_level, samples):
    return [base_signal * math.sin(i) + (i % noise_level) for i in range(samples)]

def filter_outliers(data, limit):
    # Irrelevant filtering function (dead code path)
    return [x for x in data if abs(x) < limit]

def compute_moving_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed

def encrypt_key(sequence):  # Distractor function – looks important but unused
    key = 0
    for idx, val in enumerate(sequence):
        key ^= int(val) & idx
    return key

def transform_signal(raw, factor):
    # Apply non-linear transformation
    adjusted = [math.tanh(x * factor) for x in raw]
    # Slice to keep only mid-segment (critical step)
    trimmed = adjusted[len(adjusted)//4 : len(adjusted)//2]
    normalized = [round(x, 6) for x in trimmed]
    return normalized

def evaluate_stability(metrics):
    # Misleading evaluation – never called
    score = 0
    for m in metrics:
        if m > 0.5:
            score += 1
    return score

def analyze_pattern(data, cutoff):
    # Core logic: count how many values exceed cutoff after bit analysis
    counts = []
    for val in data:
        # Convert float to integer representation for bitwise ops
        as_int = int(abs(val) * 10000) & 0xFF  # Mask to 8 bits
        bit_count = bin(as_int).count('1')
        counts.append(bit_count)
    
    # Determine pattern match based on odd counts
    pattern_match = 0
    running_sum = 0
    temp_buffer = []
    
    for c in counts:
        running_sum += c
        temp_buffer.append(c * 2)  # Red herring buffer
        if c % 2 == 1:  # Only odd bit counts contribute
            pattern_match += 1
    
    # Secondary condition: must have even sum modulo pattern_match
    if pattern_match > 0 and (running_sum % pattern_match) % 2 == 0:
        adjustment = len(temp_buffer) // pattern_match
        return running_sum + adjustment
    else:
        return running_sum - pattern_match

# Main execution sequence
if __name__ == "__main__":
    # Initialization parameters
    signal_strength = 2.7
    noise_floor = 5
    sample_count = 16
    threshold = 0.45

    # Step 1: Collect raw sensor readings
    raw_readings = collect_samples(signal_strength, noise_floor, sample_count)

    # Step 2: Apply moving average smoothing (distraction - not used later)
    smoothed_readings = compute_moving_average(raw_readings, 3)

    # Step 3: Transform signal for analysis
    transformed_data = transform_signal(raw_readings, factor=1.8)

    # Irrelevant variables and decoy operations
    checksum = sum(int(abs(x)*100) for x in smoothed_readings) % 256
    metadata_log = {'version': '2.1', 'mode': 'diagnostic'}
    debug_trace = [math.cos(x) for x in raw_readings[:5]]

    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Output result
    print(f"Result: {final_diagnostic}")