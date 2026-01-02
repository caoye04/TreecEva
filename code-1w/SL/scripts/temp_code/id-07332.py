def analyze_pattern(sequence):
    if not sequence:
        return 0
    
    # Irrelevant transformation (distractor)
    temp_chars = [chr((ord(c) + 3) % 26 + 97) for c in 'abcde']
    unused_sum = sum([i * 2 for i in range(4)])  # Dead computation
    
    # Real logic begins: count uppercase letters
    uppercase_count = len([c for c in sequence if c.isupper()])
    
    # Misleading normalization (not used later)
    normalized = uppercase_count / len(sequence) if sequence else 0
    
    return uppercase_count


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    
    # Side calculation with no impact
    dummy_variance = sum((x - total/len(values))**2 for x in values) / len(values) if values else 0
    
    return round(entropy, 4)


def calculate_stability_index(raw_data, limit):
    # Extract substrings and process
    segments = raw_data.split('|')
    filtered = [s.strip() for s in segments if len(s.strip()) > 2]
    
    # Distractor: character frequency map (partially computed but not fully used)
    char_freq = {}
    for seg in filtered:
        for ch in seg:
            char_freq[ch] = char_freq.get(ch, 0) + 1
    
    # Use slicing to get middle portion of each segment
    mid_parts = [seg[len(seg)//3 : 2*len(seg)//3] for seg in filtered]
    
    # Count vowels in middle parts (semi-relevant)
    vowels = 'aeiou'
    vowel_count = sum(1 for part in mid_parts for c in part.lower() if c in vowels)
    
    # Actual key metric: length-based weighting
    weights = [len(seg) ** 0.5 for seg in filtered]
    weighted_total = sum(weights)
    
    # Conditional logic with red herring branch
    adjustment = 0
    if vowel_count > 5:
        adjustment = 2
    else:
        temp_arr = [1, 2, 3, 4]
        adjustment = sum(x for x in temp_arr if x % 2 == 0)  # Always 6
    
    # Final stability logic
    base_score = analyze_pattern(raw_data)
    entropy_metric = calculate_entropy([len(filtered), len(char_freq), vowel_count])
    
    # Key intermediate variable
    preliminary_index = (base_score * weighted_total) + vowel_count - adjustment
    
    # Final decision based on threshold
    if preliminary_index >= limit:
        final_output = int(preliminary_index - entropy_metric)
    else:
        fallback_data = [len(s) for s in filtered][::-1]
        final_output = sum(fallback_data[:3]) * 2  # Unused path due to logic flow
    
    return final_output

# Main execution
threshold = 18
raw_input = "AbC|XyZz|TestString|HELLO|Data"
data = raw_input + "|extra|padding"  # Augment input

# Execute target statement
final_output = calculate_stability_index(data, threshold)
print(f"Result: {final_output}")