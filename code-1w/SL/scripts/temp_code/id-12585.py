def analyze_frequency(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

# Irrelevant helper function (dead code path)
def validate_input(value):
    if not isinstance(value, str):
        raise ValueError("Input must be string")
    return True

# Misleading preprocessing step
temp_buffer = [0] * 26
for i in range(26):
    temp_buffer[i] = i * i + 3*i - 1  # Unused computation

# Real data processing
raw_data = "abccba defg ggfed xyzzy"
data_parts = raw_data.split(' ')
filtered_parts = [part for part in data_parts if len(part) >= 3]

# Simulate noisy signal filtering
signal_strength = sum(len(part) for part in filtered_parts) / len(filtered_parts) if filtered_parts else 0
threshold = int(signal_strength) if signal_strength > 4 else 4

# Core logic with conditional expression
compression_factor = 2 if len(filtered_parts) > 3 else 1.5

# Main metric processor
def process_metrics(parts, limit):
    total_chars = sum(len(part) for part in parts)
    unique_chars = len(set(''.join(parts)))
    
    # Secondary distraction: frequency analysis not fully used
    freq_map = analyze_frequency(''.join(parts))
    max_freq = max(freq_map.values()) if freq_map else 1
    adjustment = 0
    for k, v in freq_map.items():
        if v == max_freq and k in 'aeiou':
            adjustment += 2
    
    # Actual calculation chain
    base_score = total_chars * unique_chars
    penalty = 0
    for part in parts:
        if len(part) < limit:
            penalty += 3
    
    # Conditional expression usage (required feature)
    bonus = 10 if any(part == part[::-1] for part in parts) else 5
    
    # Final formula with distractor variables present but not dominant
    intermediate = (base_score - penalty * 4) + (adjustment * bonus) // compression_factor
    final_score = int(intermediate // 1.5)  # Key assignment point
    return final_score

# Execute main logic
final_score = process_metrics(data_parts, threshold)
print(f"Result: {final_score}")