def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    for char in sequence:
        if char in 'aeiou':
            count_vowels += 1
        temp_sum += ord(char)
    return count_vowels


def process_records(records):
    total_length = sum(len(record) for record in records)
    avg_length = total_length / len(records) if records else 0
    filtered = [r for r in records if len(r) > avg_length]
    excess_chars = ''.join(filtered)
    return excess_chars.upper().strip()


def calculate_final_score(data):
    # Primary computation path
    valid_entries = [x for x in data if isinstance(x, str) and x.isalpha()]
    reversed_data = [s[::-1] for s in valid_entries]
    
    # Distractor: vowel analysis with no impact on final result
    vowel_counts = [analyze_pattern(s) for s in valid_entries]
    mean_vowel_density = sum(vowel_counts) / len(vowel_counts) if vowel_counts else 0
    
    # Real logic begins: find palindromic strings after reversal
    palindrome_flags = [orig == rev for orig, rev in zip(valid_entries, reversed_data)]
    palindrome_bonus = 7 if any(palindrome_flags) else 0
    
    # Compute base score using string lengths
    length_contributions = [len(s) for s in valid_entries]
    base_score = sum(length_contributions)
    
    # Apply conditional multiplier based on set uniqueness
    unique_chars = set(''.join(valid_entries).lower())
    distinct_consonants = unique_chars - {'a', 'e', 'i', 'o', 'u'}
    multiplier = 1.5 if len(distinct_consonants) >= 5 else 1.0
    
    # Irrelevant intermediate calculation (dead-end)
    ascii_mapping = {c: ord(c) % 26 for c in unique_chars}
    shift_value = sum(ascii_mapping.values()) // len(ascii_mapping) if ascii_mapping else 0
    
    # Final composition
    adjusted_score = base_score * multiplier
    final_score = int(adjusted_score + palindrome_bonus)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
input_data = [
    "hello", "world", "level", "deified", "test",
    "abc123", 123, None, "", "python",
    "radar", "stats"
]

# Execute main function
calculate_final_score(input_data)