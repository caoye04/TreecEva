def analyze_signal(samples, threshold=128):
    signal_peaks = []
    noise_floor = 0
    for sample in samples:
        if sample > threshold:
            signal_peaks.append(sample & 0xFF)
        else:
            noise_floor += (sample ^ 0x5A) % 3
    return signal_peaks

samples_data = [203, 87, 135, 44, 176, 92, 200, 110]
signal_output = analyze_signal(samples_data)

# Extract dominant bit pattern across high-amplitude samples
dominant_bits = 0
for val in signal_output:
    dominant_bits ^= val  # Accumulate XOR to find bit bias

# Simulate diagnostic checksums
diagnostic_codes = {1: 'A', 3: 'B', 5: 'C'}
encoded_checksum = 0
for k in diagnostic_codes:
    encoded_checksum += k * ord(diagnostic_codes[k])

# Generate feedback set with overlapping characteristics
raw_feedback = [x % 64 for x in samples_data if x < 150]
feedback_set = set(raw_feedback)
backup_set = set([x + 10 for x in raw_feedback if x % 2 == 0])  # Unused distractor

# Weighted influence factors (some irrelevant)
influence_map = {}
for i, v in enumerate(signal_output):
    influence_map[i] = (v ** 2) / (i + 1) if i % 2 == 0 else v * 0.5

# Core evaluation logic depending on dominant_bits and feedback_set
def evaluate_performance(bits, fb_set):
    base_score = bits % 100
    bonus = 0
    penalty = len(fb_set.intersection({x for x in range(10, 30, 3)}))
    
    # Irrelevant loop - computes but doesn't impact final score
    temp_sum = 0
    for _ in range(3):
        temp_sum += sum([bits >> i & 1 for i in range(8)])  # Count active bits, thrice
    
    # Actual bonus logic
    if len(fb_set) > 5:
        bonus = 15
    if (bits & 0b110011) == 0b100010:
        bonus += 10
    
    # Final score computation
    final_score = base_score + bonus - penalty
    return int(final_score)

# Key statement
final_score = evaluate_performance(dominant_bits, feedback_set)
print(f"Result: {final_score}")