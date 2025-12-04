def process_data(samples):
    total_chars = sum(len(sample) for sample in samples)
    vowel_count = sum(1 for sample in samples for char in sample if char.lower() in 'aeiou')
    consonant_count = sum(1 for sample in samples for char in sample if char.lower() in 'bcdfghjklmnpqrstvwxyz')
    
    # Distractor calculations
    irrelevant_sum = total_chars * 3 + vowel_count // 2
    misleading_factor = consonant_count % 7 if consonant_count > 20 else 5
    
    # Main logic with conditional expressions
    char_ratio = (vowel_count * 2) // (consonant_count + 1) if consonant_count > 0 else vowel_count
    adjustment = 15 if total_chars > 50 else -8
    
    # Dead code path (never executed)
    if misleading_factor < 0:
        unused_value = irrelevant_sum * 2
    
    # Final calculation
    result = (char_ratio * 3) + adjustment
    return result

text_samples = ['Python programming', 'Data analysis', 'Machine learning', 'Algorithm design']

# Distractor variables and operations
preliminary_count = len(''.join(text_samples))
misleading_total = preliminary_count * 2 - 10
unused_list = [x * 2 for x in range(10)]

final_tally = process_data(text_samples)
print(f"Result: {final_tally}")