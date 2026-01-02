def process_sequence(stream):
    count_vowels = 0
    total_chars = 0
    temp_sum = 0
    
    # Misleading pre-processing: counts digits but never used
    digit_count = sum(1 for c in stream if c.isdigit())
    unused_intermediate = digit_count * 2 + 5

    for char in stream:
        if char.lower() in 'aeiou':
            count_vowels += 1
        total_chars += 1
        
        # Red herring computation with no impact
        if char.isupper():
            temp_sum += ord(char) % 7

    # Conditional expression (required language feature)
    adjustment = 10 if count_vowels > 3 else 5
    
    # Real logic: vowel density adjusted by rule
    density_score = count_vowels / total_chars if total_chars > 0 else 0
    weighted_value = density_score * 100
    
    # Another distraction: character product modulo, computed but unused
    phantom_product = 1
    for c in stream[:min(4, len(stream))]:
        phantom_product *= (ord(c) % 10) or 1
    dead_end_result = phantom_product % 97

    # Key calculation
    base_tally = int(weighted_value) + adjustment
    
    # Secondary logic chain: analyze repetition pattern
    seen = {}
    repeat_bonus = 0
    for c in stream:
        seen[c] = seen.get(c, 0) + 1
        if seen[c] == 2 and c.isalpha():
            repeat_bonus += 1

    # Final result built from multiple valid steps
    final_tally = base_tally + repeat_bonus
    
    # Output required format
    return final_tally

# Input data
data_stream = "SignalFlow2024!"

# Execution point
final_tally = process_sequence(data_stream)
print(f"Result: {final_tally}")