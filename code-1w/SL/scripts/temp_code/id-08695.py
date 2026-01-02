def analyze_text_frequency(text):
    frequency_map = {}
    for char in text.lower():
        if char.isalpha():
            frequency_map[char] = frequency_map.get(char, 0) + 1
    return frequency_map

sample_text = "Dynamic programming solves complex problems by breaking them into simpler subproblems."

char_freq = analyze_text_frequency(sample_text)

# Irrelevant distraction: counting non-alphabetic characters (not used later)
non_alpha_count = sum(1 for c in sample_text if not c.isalpha())

# Distractor computation: average frequency (semi-relevant but not directly used)
if char_freq:
    avg_freq = sum(char_freq.values()) / len(char_freq)
else:
    avg_freq = 0

# Extract vowels and consonants
vowels = 'aeiou'
consonant_rarity = []
vowel_density = 0
for letter, count in char_freq.items():
    if letter in vowels:
        vowel_density += count
    else:
        consonant_rarity.append(count)

# Sort and take top 3 rarest consonants (distraction)
consonant_rarity.sort()
top_rare_consonants_sum = sum(consonant_rarity[:3]) if len(consonant_rarity) >= 3 else 0

# Process data: weight vowels more heavily
weighted_vowel_score = vowel_density * 1.5 if vowel_density > 10 else vowel_density * 1.2

# Simulate multi-step transformation
processed_data = {
    'raw_length': len(sample_text),
    'unique_letters': len(char_freq),
    'weighted_vowels': weighted_vowel_score,
    'rarity_offset': top_rare_consonants_sum,
    'baseline': len(char_freq) // 2
}

# Misleading function that looks important but only used once
def adjust_for_redundancy(data):
    adjustment = 0
    if data['raw_length'] > 50:
        adjustment += 5
    if data['unique_letters'] > 15:
        adjustment += 3
    return adjustment

# Another red herring: conditional expression with string method
status_flag = 'optimized' if sample_text.strip().endswith('.') else 'standard'
bonus_factor = 2 if status_flag == 'optimized' else 1

# Core logic chain begins
intermediate_score = (processed_data['weighted_vowels'] + 
                      processed_data['unique_letters'])

scaling_factor = bonus_factor * (1 + processed_data['baseline'] / 10)

adjusted_score = intermediate_score * scaling_factor

penalty = 0
if processed_data['raw_length'] < 70:
    penalty += 4
if len([x for x in char_freq.values() if x == 1]) > 5:  # letters appearing once
    penalty -= 2  # reward low-frequency diversity

# Final calculation
final_score = int(adjusted_score - penalty + adjust_for_redundancy(processed_data))

Result: final_score