import math

def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]

def shift_phase(data, offset=2):
    return [data[(i + offset) % len(data)] for i in range(len(data))]

def generate_checksum(sequence):
    # Irrelevant checksum function (dead code path)
    return sum((i + val) * 3 % 7 for i, val in enumerate(sequence)) % 100

def evaluate_entropy(stream):
    # Misleading complexity: computes entropy but not used in final result
    freq_map = {}
    for s in stream:
        freq_map[s] = freq_map.get(s, 0) + 1
    entropy = 0
    total = len(stream)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_features(dataset):
    features = []
    for item in dataset:
        if isinstance(item, float):
            binary_rep = bin(int(abs(item) * 1000))[2:]
            parity = bin(int(abs(item) * 1000)).count('1') % 2
            features.append(parity)
    return features

def transform_sequence(values):
    # Applies bit manipulation and modular arithmetic
    shifted = [v * 1.5 for v in values]
    modded = [int(s * 100) % 97 for s in shifted]
    xored = [m ^ 15 for m in modded]  # Key transformation
    return xored

def analyze_pattern(traces):
    cumulative = 0
    for idx, val in enumerate(traces):
        if idx % 2 == 0 and val > 50:
            cumulative += val // (idx + 1)
        elif val < 30:
            cumulative -= val
        else:
            cumulative += val % 11
    return int(math.sqrt(cumulative * 4))  # Final computation

def main():
    # Simulated sensor input (real data)
    primary_input = [-2.3, 1.7, 0.8, 3.4, -0.5, 2.9, 4.1, 0.0, -1.2]

    # Irrelevant auxiliary data (distractor)
    noise_floor = [0.01, 0.02, -0.015, 0.0]
    baseline_offsets = {'a': 10, 'b': 25, 'c': -7}

    # Step 1: Preprocess real signal
    cleaned = preprocess_signal(primary_input)

    # Step 2: Phase shift for alignment (used)
    aligned = shift_phase(cleaned, offset=1)

    # Step 3: Transform into integer domain using scaling and XOR
    transformed_data = transform_sequence(aligned)

    # Irrelevant string processing (distractor with string methods)
    status_log = "System initialized: OK | Data ready: TRUE | Mode: DIAGNOSTIC"
    if status_log.startswith("System") and "DIAGNOSTIC" in status_log:
        log_parts = status_log.split('|')
        mode_flag = log_parts[-1].strip().lower()
        backup_code = ''.join([p[0] for p in log_parts]).replace(' ', '')

    # Dead function call (red herring)
    _ = evaluate_entropy(['a', 'b', 'a', 'c', 'b', 'a'])

    # Unused feature extraction
    _ = extract_features(aligned)

    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data)

    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()