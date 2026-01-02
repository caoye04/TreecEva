import itertools

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    return filtered

def generate_reference(size):
    # Dead code path - never used
    return [i % 3 for i in range(size)]

def shift_sequence(seq, offset):
    # Unused helper function (red herring)
    return seq[offset:] + seq[:offset]

def calculate_entropy(data):
    # Misleading computation: looks important but isn't on critical path
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

def encode_triplet(t):
    # Core logic: maps tuple to numeric hash
    a, b, c = t
    return (a * 100) + (b * 10) + c

def transform_readings(readings):
    # Adds noise but then removes it (decoy logic)
    amplified = [r * 2 for r in readings]
    clipped = [min(r, 9) for r in amplified]
    restored = [r // 2 for r in clipped]  # Back to near-original
    return restored

def build_patterns(values):
    # Critical: creates sliding triplets
    triplets = []
    for i in range(len(values) - 2):
        triplets.append((values[i], values[i+1], values[i+2]))
    return triplets

def analyze_pattern(triplets):
    # Key transformation: encodes each triplet and sums
    codes = [encode_triplet(t) for t in triplets]
    return sum(codes)

def main():
    # Initial sensor data (simulated)
    sensor_log = [1, 2, 3, 4, 5, 6]
    
    # Distractor: unused derived data
    reversed_log = sensor_log[::-1]
    scaled_log = [x * 10 for x in sensor_log]
    
    # Real pipeline begins
    cleaned = preprocess_signal(sensor_log)
    adjusted = [int(x) for x in cleaned]  # Back to integers
    enhanced = transform_readings(adjusted)
    
    # Create all possible ordered triplets using windowing
    data_stream = enhanced
    
    # Use itertools to generate permutations (mostly irrelevant)
    decoy_combinations = list(itertools.permutations(enhanced, 3))
    decoy_count = len(decoy_combinations)
    
    # But actual pattern uses simple sliding window
    valid_triplets = build_patterns(data_stream)
    
    # Secondary distractor: case conversion on dummy string
    mode_flag = 'ACTIVE'
    mode_lower = mode_flag.lower()
    status_code = len(mode_lower) if mode_lower == 'active' else -1
    
    # Final analysis (key assignment)
    final_diagnostic = analyze_pattern(valid_triplets)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()