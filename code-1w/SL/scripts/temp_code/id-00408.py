def analyze_text_pattern(text):
    if not text:
        return 0
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    special_count = len(text) - upper_count - lower_count - digit_count
    
    # Irrelevant transformation chain
    temp_buffer = [ord(c) % 10 for c in text]
    shifted = [((x + 3) * 7) % 10 for x in temp_buffer]
    hashed_sum = sum(shifted) ** 2 % 100
    
    # Unused branching based on character pattern
    if upper_count > lower_count and digit_count == 0:
        scale_factor = 1.5
    elif lower_count > upper_count:
        scale_factor = 0.8
    else:
        scale_factor = 1.0
    
    # Distractor: complex but unused score
    complexity_score = (upper_count * 2 + lower_count) / max(1, special_count + 1)
    normalized_entropy = 0.0
    for i in range(1, min(5, len(text))):
        if text[i] != text[i-1]:
            normalized_entropy += 0.2
    
    return upper_count * 10 + lower_count


def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True

# Main logic
raw_data = "AaBbCc123!@#"
processed_chars = list(raw_data.strip().lower().replace(" ", ""))
char_positions = {c: i for i, c in enumerate(processed_chars)}

# Extract frequency stats using slicing and string ops
slice_a = processed_chars[::2]
slice_b = processed_chars[1::2]
freq_map_a = {c: slice_a.count(c) for c in set(slice_a)}
freq_map_b = {c: slice_b.count(c) for c in set(slice_b)}

# Dummy sequence for Fibonacci check (dead path)
test_seq = [1, 1, 2, 3, 5, 8]
is_valid_seq = validate_sequence(test_seq)

# Real computation begins — metrics for evaluation
base_metric_1 = len([c for c in raw_data if c.isalpha()])  # Alphabetic length
base_metric_2 = analyze_text_pattern(raw_data)              # Encoded case count
base_metric_3 = sum(char_positions.values()) // max(len(char_positions), 1)  # Avg position

# Additional irrelevant intermediate
reversed_pairs = list(zip(processed_chars, processed_chars[::-1]))
enumerated_lines = list(enumerate(reversed_pairs, start=1))
checksum = sum(i * ord(pair[0][0]) for i, pair in enumerated_lines) % 50

# Weights (some are misleading)
weights = [0.4, 0.35, 0.25]  # Only first three used
extra_weights = [0.1, 0.15, 0.2]  # Unused

# Key function with distractors
metrics = [
    base_metric_1 * 2,
    (base_metric_2 + 10) // 5,
    max(1, abs(base_metric_3 - 15))
]

# Introduce bit manipulation red herring
bit_analysis = 0
for val in metrics:
    bit_analysis ^= (val << 2) | (val >> 1)
bit_analysis = bit_analysis & 0xFF  # Cap to byte

# Final performance evaluation (actual answer path)
def evaluate_performance(mets, wts):
    weighted_sum = 0.0
    for i, (m, w) in enumerate(zip(mets, wts)):
        if i % 2 == 0:
            weighted_sum += m * w * 1.1  # Bonus on even indices
        else:
            weighted_sum += m * w
    
    # Secondary adjustment based on string property
    temp_str = ''.join([k for k in char_positions.keys() if k.isalpha()])
    if temp_str.startswith('a'):
        adjustment = 5
    else:
        adjustment = -3
    
    # Final nonlinear scaling
    result = int(weighted_sum + adjustment)
    
    # Dead comparison with early return (never reached due to structure)
    if result > 1000:
        return result // 10
    
    return result

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")