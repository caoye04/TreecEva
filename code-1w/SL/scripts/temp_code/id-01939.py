def calculate_final_score(data, weight_map):
    normalized = []
    total_length = sum(len(s) for s in data)
    
    for entry in data:
        clean_entry = entry.strip().lower()
        vowel_count = sum(1 for char in clean_entry if char in 'aeiou')
        consonant_count = len(clean_entry) - vowel_count
        score = (vowel_count * weight_map['vowels']) + (consonant_count * weight_map['consonants'])
        normalized.append(score)
    
    aggregate = sum(normalized)
    adjustment = len(data) * weight_map.get('length_bonus', 0)
    return int(aggregate + adjustment)

# Irrelevant utility function (mild distraction)
def reverse_strings_in_list(lst):
    return [s[::-1] for s in lst]

# Main execution
raw_data = ['Hello World', 'Python Code', 'AI Reasoning', 'Data Analysis']
weights = {
    'vowels': 1.5,
    'consonants': 0.8,
    'length_bonus': 2
}

intermediate_result = reverse_strings_in_list(raw_data)
final_score = calculate_final_score(raw_data, weights)
print(f"Target result: {final_score}")