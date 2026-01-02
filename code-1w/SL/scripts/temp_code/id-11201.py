def analyze_text_composition(text):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0

    temp_sum = 0  # distractor: used in irrelevant computation
    for i, char in enumerate(text):
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
            temp_sum += int(char)  # red herring
        else:
            special_char_count += 1

    # Irrelevant transformation
    adjusted_temp = temp_sum * 2 if temp_sum > 5 else temp_sum + 3
    dummy_ratio = consonant_count / (vowel_count + 1)  # not used later

    return {
        'vowels': vowel_count,
        'consonants': consonant_count,
        'digits': digit_count,
        'specials': special_char_count,
        'length': len(text)
    }


def calculate_complexity_index(meta):
    base = meta['vowels'] + meta['consonants']
    penalty = meta['specials'] * 2
    bonus = meta['digits'] // 2
    return base - penalty + bonus


def calculate_final_score(data):
    comp_index = calculate_complexity_index(data)
    length_factor = data['length'] % 7
    score = comp_index * 3 + length_factor

    # Distractor block: dead logic with no effect
    if score < 0:
        score = abs(score)
    elif score == 0:
        score = 10
    # This branch never executes due to input constraints
    if data['vowels'] > 100:
        score += 50

    return score

# Main execution
raw_input = "Hello World! 2023..."  # realistic sample text
processed_data = analyze_text_composition(raw_input)

# Redundant analysis path
secondary_analysis = analyze_text_composition(raw_input.upper())
consistency_check = processed_data['length'] == secondary_analysis['length']

# Dummy counters for interference
char_cycle_total = 0
for c in raw_input:
    char_cycle_total += ord(c) % 5

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")