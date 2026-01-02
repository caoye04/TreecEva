import math

# Simulated sensor array diagnostics with data transformation and noise filtering
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-9) for x in filtered]
    return [round(x, 6) for x in normalized]


def generate_harmonic_series(base, length):
    # Distractor function: generates harmonic-like values not directly used in final result
    return [round(base / (i + 1), 6) for i in range(length)]


def shift_cipher(text, shift):
    # Irrelevant string operation - red herring
    return ''.join(chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c for c in text)


def compute_checksum(sequence):
    # Decoy computation on transformed data
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return int(checksum * 1000) % 1000


def transform_signal(data, key):
    # Bit manipulation mixed with arithmetic - relevant but partially obscured
    shifted = [(x * 1000) for x in data]
    processed = []
    for val in shifted:
        temp = int(val) ^ int(key * 100)  # XOR with scaled key
        temp = (temp << 2) | (temp >> 15)  # Bit rotation simulation
        processed.append(temp % 97)
    return processed


def evaluate_stability(indices):
    # Stability metric based on index variance - misleading intermediate
    mean_idx = sum(indices) / len(indices)
    variance = sum((x - mean_idx) ** 2 for x in indices) / len(indices)
    return variance < 0.5


def analyze_pattern(seq, limit):
    # Core logic hidden among distractions
    count = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1] and (seq[i] - seq[i-1]) % 3 == 0:
            count += 1
    # Final decision involves lambda and slicing
    validator = lambda x: sum(x[-3:]) > limit
    if validator(seq) and count >= 2:
        return count * seq[-1] + len(seq)
    else:
        return -count * 10

# Main execution flow
if __name__ == "__main__":
    # Real input data
    sensor_log = [0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05]
    
    # Irrelevant variables and operations
    encryption_key = 7
    encoded_message = shift_cipher("sensoralert", encryption_key)
    dummy_series = generate_harmonic_series(5.0, 7)
    backup_threshold = 0.45
    
    # Relevant preprocessing
    cleaned_data = preprocess_readings(sensor_log)
    scaling_factor = sum(cleaned_data) / len(cleaned_data)
    enhanced_data = [x * scaling_factor for x in cleaned_data]
    
    # Key transformation
    transformed_data = transform_signal(enhanced_data, scaling_factor)
    
    # Dead code path - never executed due to condition
    diagnostic_mode = False
    if diagnostic_mode:
        test_result = compute_checksum(transformed_data)
        print(f"Test: {test_result}")
    
    # Control flow distraction
    critical_indices = [i for i, x in enumerate(transformed_data) if x > 50]
    system_stable = evaluate_stability(critical_indices)
    
    # Actual threshold used in analysis
    threshold = 150
    
    # Key statement containing answer
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")