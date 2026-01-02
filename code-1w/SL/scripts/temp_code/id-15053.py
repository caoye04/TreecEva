from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor data stream with noise and redundant readings
def generate_noisy_readings():
    base_signal = [1, 0, 1, 1, 0, 1, 0, 0]
    noise_mask = [0, 1, 1, 0, 1, 0, 1, 1]
    return [int((s + n) % 2) for s, n in zip(base_signal, noise_mask)]

# Irrelevant helper: used nowhere but looks important
def decrypt_sequence(seq):
    return [x ^ 1 for x in seq[::-1]]

# Data transformation pipeline
def apply_filter(data):
    filtered = []
    for i in range(len(data)):
        window = data[max(0, i-2):i+1]
        avg = sum(window) / len(window)
        filtered.append(1 if avg >= 0.5 else 0)
    return filtered

# Complex pattern analyzer with red herrings
def detect_anomalies(sequence):
    stats = defaultdict(int)
    for bit in sequence:
        stats['total'] += 1
        if bit == 1:
            stats['ones'] += 1
        else:
            stats['zeros'] += 1
    
    # Distractor logic: computes unused metrics
    stats['ratio'] = stats['ones'] / stats['total'] if stats['total'] else 0
    stats['entropy'] = 0.0
    if stats['ones'] and stats['zeros']:
        p1 = stats['ones'] / stats['total']
        p0 = stats['zeros'] / stats['total']
        import math
        stats['entropy'] = -p1 * math.log2(p1) - p0 * math.log2(p0)
    
    # This result is ignored later — deliberate misdirection
    return stats

# Core analysis function (actually used)
def analyze_pattern(seq, thresh):
    count = 0
    for a, b, c in zip(seq, seq[1:], seq[2:]):
        if a == 1 and b == 0 and c == 1:
            count += 1
    return count > thresh

# Secondary transformation — only some output matters
def transform_sequence(raw):
    doubled = [x * 2 for x in raw]
    shifted = [doubled[-1]] + doubled[:-1]
    return [x ^ 1 for x in shifted]  # Flip bits

# Unused checksum generator — looks critical
def compute_cyclic_checksum(data):
    chk = 0
    for i, val in enumerate(data):
        chk = (chk + val * (i + 1)) % 257
    return chk

# Main execution flow
if __name__ == "__main__":
    # Step 1: Acquire raw sensor data
    raw_diagnostics = generate_noisy_readings()  # [1, 1, 0, 1, 1, 1, 1, 1]
    
    # Step 2: Apply temporal filter to smooth signal
    filtered_diagnostics = apply_filter(raw_diagnostics)
    
    # Step 3: Transform sequence using bit manipulation
    transformed_data = transform_sequence(filtered_diagnostics)
    
    # Step 4: Detect anomalies (result stored but not used)
    anomaly_report = detect_anomalies(transformed_data)
    
    # Step 5: Decrypt attempt (unused, red herring)
    decrypted_attempt = decrypt_sequence(transformed_data)
    
    # Step 6: Compute irrelevant checksum
    dummy_checksum = compute_cyclic_checksum(decrypted_attempt)
    
    # Step 7: Prepare counter-based frequency analysis (unused)
    freq_analysis = Counter(transformed_data)
    
    # Step 8: Define decision threshold based on flawed heuristic
    dynamic_thresh = 1 if freq_analysis[1] > 3 else 0
    
    # Step 9: Perform final diagnostic pattern match (ACTUALLY USED)
    final_diagnostic = analyze_pattern(transformed_data, dynamic_thresh)
    
    # Print result as required
    print(f"Result: {int(final_diagnostic)}")