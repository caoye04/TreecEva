def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    count_consonants = sum(1 for c in sequence if c.isalpha() and c.lower() not in 'aeiou')
    total_chars = len(sequence)
    redundancy_factor = len(sequence) - len(set(sequence))

    # Irrelevant statistical distraction
    avg_char_position = sum(ord(c) for c in sequence) / len(sequence) if sequence else 0
    palindrome_check = sequence == sequence[::-1]

    return count_vowels, count_consonants, total_chars, redundancy_factor


def generate_weighted_profile(data_list):
    weighted_sum = 0
    normalization_base = 0

    for item in data_list:
        temp_score = 0
        if len(item) > 3:
            temp_score += len(item) * 1.5
        if item[-1].isdigit():
            temp_score += int(item[-1])
        if item[0].isupper():
            temp_score += 2.5

        # Distractor: unused intermediate
        reverse_entropy = sum((i + 1) * ord(c) for i, c in enumerate(reversed(item))) % 100

        weighted_sum += temp_score
        normalization_base += 1

    profile_score = weighted_sum / normalization_base if normalization_base else 0
    return profile_score

# Simulate sensor readings with noise filtering
readings = ['Alpha3', 'beta4', 'Gamma7', 'Delta1', 'Echo5']

# Extract linguistic features (some irrelevant)
linguistic_metrics = [analyze_pattern(r) for r in readings]
vowel_density = sum(m[0] for m in linguistic_metrics) / sum(m[2] for m in linguistic_metrics) if any(m[2] > 0 for m in linguistic_metrics) else 0

# Compute structural bias (partially relevant)
structural_bias = sum(m[3] for m in linguistic_metrics) * 0.8

# Generate behavioral weights (distractor-heavy)
behavioral_weights = []
duplicate_tracker = {}
for r in readings:
    hash_val = sum(ord(c) * (i + 1) for i, c in enumerate(r))
    duplicate_tracker[r] = hash_val
    if r[0].lower() in 'bcdfg':
        behavioral_weights.append(hash_val % 7)
    else:
        behavioral_weights.append((hash_val + 3) % 5)

# Main scoring logic
base_scores = [len(r) + (ord(r[0]) % 5) for r in readings]
adjusted_scores = [s * 1.1 for s in base_scores]

# Conditional modulation based on character type
modulated_scores = []
for idx, r in enumerate(readings):
    mod = 1.0
    if r[0].isupper():
        mod *= 1.2
    if r[-1].isdigit():
        digit_val = int(r[-1])
        if digit_val % 2 == 0:
            mod *= 0.9
        else:
            mod *= 1.1
    modulated_scores.append(adjusted_scores[idx] * mod)

# Secondary adjustment using weighted profile
profile_value = generate_weighted_profile(readings)

# Final fusion with modular arithmetic and thresholding
fusion_component = (int(profile_value) % 4) + 1
noise_floor = sum(1 for r in readings if 'a' in r or 'e' in r) * 0.3

# Critical execution point
final_score = sum(modulated_scores) * fusion_component + vowel_density * 10 - noise_floor

# Output target result
print(f"Result: {final_score}")