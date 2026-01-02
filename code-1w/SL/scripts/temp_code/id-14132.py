def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    # Distractor: Count vowels and consonants (semi-relevant)
    vowel_count = sum(1 for c in char_frequency.keys() if c in 'aeiou')
    consonant_count = sum(1 for c in char_frequency.keys() if c.isalpha() and c not in 'aeiou')

    # Red herring computation: reversed string analysis (not used later)
    reversed_analysis = input_str[::-1].title().replace(' ', '')
    dummy_metric = len(reversed_analysis) % 7

    return char_frequency, vowel_count


def compute_weighted_sum(freq_dict):
    total = 0
    weight_map = {k: ord(k) % 5 + 1 for k in freq_dict}
    for k, v in freq_dict.items():
        total += v * weight_map[k]
    
    # Extra distraction: normalize by unused factor
    if total > 10:
        normalized = total / (len(freq_dict) + 1)
        adjustment = sum(weight_map.values()) // 2
        dummy_normalized = round(normalized - adjustment, 2)  # unused
    return total

# Simulate system log entry with embedded metrics
log_entry = "UserSession_2024::[INFO] Task completed successfully. Latency=23ms"

# Extract alphanumeric payload for processing
payload = ''.join(filter(str.isalnum, log_entry))

# Secondary distractor: timestamp approximation (irrelevant)
timestamp_approx = sum(ord(c) for c in log_entry[:15]) % 1000

# Core data extraction
cleaned_payload = ''.join([c for c in payload if not c.isdigit()])

# Perform character analysis
frequencies, vowel_types = analyze_text_patterns(cleaned_payload)

# Compute intermediate score
raw_sum = compute_weighted_sum(frequencies)

# Apply conditional scaling based on vowel diversity
scaling_factor = 1.5 if vowel_types >= 3 else 1.2
adjusted_sum = raw_sum * scaling_factor

# Additional noise: simulate checksum validation (dead path)
checksum = sum(frequencies.values()) * 3
valid_checksum = (checksum % 9 == 0)
dummy_status = 'OK' if valid_checksum else 'FAIL'  # unused

# Final performance rating calculation
final_score = 0
if adjusted_sum > 50:
    final_score = int(adjusted_sum // 2)
    extra_penalty = len([v for v in frequencies.values() if v == 1])
    final_score -= extra_penalty  # minor correction
else:
    final_score = int(adjusted_sum)

# Also include some independent string manipulation (distractor block)
segment_a = log_entry.split('::')[0].upper()
segment_b = log_entry.split('[')[1].split(']')[0] if '[' in log_entry else ''
context_flag = len(segment_a + segment_b) % 4

# Output target result
print(f"Result: {final_score}")