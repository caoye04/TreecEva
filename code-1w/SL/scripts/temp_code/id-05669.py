from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def fetch_raw_readings():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def apply_noise_filter(data):
    # Real transformation: removes duplicates while preserving order
    seen = set()
    filtered = []
    for x in data:
        if x not in seen:
            filtered.append(x)
            seen.add(x)
    return filtered

def compute_entropy(arr):
    # Irrelevant distractor function (not used in final path)
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_synthetic_sequence(n):
    # Dead-end computation: generates Fibonacci-like sequence
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq  # Never used in critical path

def transform_signal(readings):
    # Applies squaring then mod 7
    return [x ** 2 % 7 for x in readings]

def detect_anomalies(signal):
    # Misleading analysis: counts transitions above threshold
    count = 0
    for i in range(1, len(signal)):
        if abs(signal[i] - signal[i-1]) > 3:
            count += 1
    return count  # Computed but unused

def build_lookup_table(keys):
    # Constructs mapping from key to index (used later)
    table = defaultdict(lambda: -1)
    for idx, k in enumerate(keys):
        table[k] = idx
    return table

def evaluate_consistency(pattern):
    # Checks if pattern alternates parity
    for i in range(1, len(pattern)):
        if (pattern[i] % 2) == (pattern[i-1] % 2):
            return False
    return True

def reconstruct_timeline(events, lookup):
    # Complex but irrelevant restructuring
    timeline = []
    for e in events:
        if e in lookup:
            timeline.append((lookup[e], e))
    timeline.sort(key=lambda x: x[0])
    return [x[1] for x in timeline]  # Unused result

def analyze_pattern(data, reference):
    # Core logic hidden among distractions
    shift = sum(reference) % len(data)
    rotated = data[shift:] + data[:shift]
    score = 0
    for a, b in zip(rotated, reference):
        score += (a * b) % 4
    return score + len([x for x in rotated if x in reference])

def main():
    # Step 1: Fetch raw data
    raw_data = fetch_raw_readings()  # [3,1,4,1,5,9,2,6,5,3,5]
    
    # Step 2: Filter noise
    clean_data = apply_noise_filter(raw_data)  # [3,1,4,5,9,2,6]
    
    # Step 3: Transform signal
    transformed_data = transform_signal(clean_data)  # [2,1,2,4,4,4,1]
    
    # Step 4: Detect anomalies (distractor)
    anomaly_count = detect_anomalies(transformed_data)  # 2, unused
    
    # Step 5: Compute entropy (irrelevant)
    entropy_value = compute_entropy(transformed_data)  # ~2.128, unused
    
    # Step 6: Generate synthetic sequence (dead end)
    fake_sequence = generate_synthetic_sequence(10)  # [1,1,2,...], unused
    
    # Step 7: Build lookup (partially used)
    key_sequence = [1, 2, 4]
    lookup_map = build_lookup_table(key_sequence)  # {1:0, 2:1, 4:2}
    
    # Step 8: Evaluate consistency (distractor call)
    is_alternating = evaluate_consistency(key_sequence)  # False
    
    # Step 9: Reconstruct timeline (useless)
    dummy_events = [4, 1, 2]
    timeline_result = reconstruct_timeline(dummy_events, lookup_map)  # [1,2,4], unused
    
    # Step 10: CRITICAL STATEMENT
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()