def analyze_text_complexity(text):
    char_count = len(text)
    vowel_list = [c for c in text.lower() if c in 'aeiou']
    consonant_count = len([c for c in text.lower() if c.isalpha() and c not in 'aeiou'])
    space_count = text.count(' ')
    
    # Distractor: irrelevant statistical computation
    avg_char_position = sum(ord(c) for c in text) / char_count if char_count else 0
    
    complexity_score = len(vowel_list) * 2 + consonant_count - space_count
    return complexity_score


def filter_noisy_entries(data_map):
    filtered = {}
    threshold = 5
    for key, value in data_map.items():
        if len(key) > threshold and value > 0:
            filtered[key] = value * 2
    # Distractor: dead code path (never executed due to logic)
    if False:
        filtered['dummy'] = -999
    return filtered


def sort_and_transform(values):
    sorted_vals = sorted(values, reverse=True)
    # Semi-relevant transformation
    adjusted = [v + 1 for v in sorted_vals]
    return adjusted


def calculate_final_score(entries):
    base_total = 0
    multiplier = 1
    temp_result = []
    
    for val in entries:
        if val > 10:
            base_total += val
        elif val > 5:
            base_total += val // 2
        else:
            multiplier += 1
    
    # Distractor: unused helper calculation
    outlier_count = len([x for x in entries if x < 0])
    temp_result.append(outlier_count)
    
    final_value = base_total * multiplier
    return final_value

# Main execution flow
raw_input = "ArtificialIntelligence"
data_points = {'alpha': 12, 'beta': 8, 'gamma': -3, 'delta': 15}

complexity_metric = analyze_text_complexity(raw_input)
processed_data = list(filter_noisy_entries(data_points).values())
processed_data.append(complexity_metric)

sorted_data = sort_and_transform(processed_data)
final_score = calculate_final_score(sorted_data)

# Print result for evaluation
print(f"Result: {final_score}")