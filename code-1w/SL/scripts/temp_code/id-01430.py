def transform_sequence(seq, key):
    shifted = [seq[(i + key) % len(seq)] for i in range(len(seq))]
    return [x ^ key for x in shifted]


def evaluate_pattern(arr):
    trend = [arr[i] < arr[i+1] for i in range(len(arr)-1)]
    return sum(trend)

# Irrelevant helper that computes palindrome score (dead logic)
def compute_palindrome_score(s):
    rev = ''.join(reversed(s))
    return sum(1 for a, b in zip(s, rev) if a == b)

# Decoy function processing text – looks important but unused in final path
def analyze_text_structure(text):
    lines = text.strip().split('\n')
    word_count = sum(len(line.split()) for line in lines)
    avg_word_len = sum(len(word) for word in text.split()) / word_count if word_count else 0
    upper_ratio = len([c for c in text if c.isupper()]) / len(text) if text else 0
    return {'lines': len(lines), 'words': word_count, 'avg_word_len': round(avg_word_len, 2), 'caps_ratio': round(upper_ratio, 3)}

# Real data processing chain begins
raw_input = '73194628'
numeric_seq = [int(c) for c in raw_input]

# Apply transformation with key derived from string operations
dynamic_key_str = 'XyZ9pQr1'
key_digits = ''.join(filter(str.isdigit, dynamic_key_str))
transformation_key = sum(int(d) * (i + 1) for i, d in enumerate(key_digits)) % 7  # Use only mod 7

scrambled = transform_sequence(numeric_seq, transformation_key)

evaluation_proxy = evaluate_pattern(scrambled)  # Red herring: used later in distraction

# Begin actual relevant computation: weight assignment via lambda and slicing
base_weights = list(map(lambda x: (x ** 1.5) // 1, scrambled))  # Nonlinear scaling
adjusted_weights = base_weights[2:] + base_weights[:2]  # Rotate using slicing

# Simulate sensor drift correction (only some values matter)
corrected = []
for idx, w in enumerate(adjusted_weights):
    if idx % 2 == 0:
        corrected.append(w * 0.9)
    else:
        corrected.append(w * 1.1)

decay_factor = 0.95
for i in range(len(corrected)):
    corrected[i] *= (decay_factor ** i)

# Encoded data comes from case conversion and manipulation
intermediate_str = ''.join(chr(97 + (d % 26)) for d in scrambled)  # map to a-z
mixed_case_str = ''.join(c.upper() if i % 3 == 0 else c.lower() for i, c in enumerate(intermediate_str))

# Slicing-based extraction: every 2nd char starting at index 1
sliced_chars = mixed_case_str[1::2]
encoded_data = [ord(c.lower()) - 96 for c in sliced_chars]  # a=1, b=2, etc.

# Final processing depends on weighted sum masked by decoy logic
hidden_multiplier = len(dynamic_key_str) % 4 + 2  # yields 2

# Core result calculation
weight_sum = sum(corrected)
normalized_weights = [w / weight_sum for w in corrected[:len(encoded_data)]]  # align lengths

# The real answer computation
weighted_value = sum(a * w for a, w in zip(encoded_data, normalized_weights))

# Distractor block: uses evaluation_proxy in dead branch
if evaluation_proxy > 10:
    final_score = weighted_value * 2
else:
    temp_result = compute_palindrome_score(mixed_case_str)
    final_score = int(weighted_value * hidden_multiplier) + temp_result  # temp_result is small, but distracts

# Another red herring: tuple unpacking with irrelevant stats
(_, _, _, extra_flag) = (len(raw_input), sum(scrambled), max(corrected), evaluation_proxy > 3)

# Final override based on string method condition (which is always true)
flag_check = mixed_case_str.startswith('Y') or any(c.isdigit() for c in mixed_case_str)
if not flag_check:
    final_score -= 50

# ACTUAL key statement — this determines the correct answer
final_score = process_results(encoded_data, weights) if 'weights' in locals() else int(weighted_value)

# But wait — we haven't defined `process_results` yet!
# Let's define it now (was missing earlier — typical distraction)
process_results = lambda data, w: sum(d * (i+1) for i, d in enumerate(data)) // len(data) if data else 0

# Recompute final_score with correct function
weights = [1.0] * len(encoded_data)  # uniform weighting for final step
final_score = process_results(encoded_data, weights)

print(f"Target result: {final_score}")