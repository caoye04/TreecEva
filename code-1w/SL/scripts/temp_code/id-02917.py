def analyze_text_properties(text):
    char_count = len(text)
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    space_count = text.count(' ')
    
    # Irrelevant intermediate calculations (distractors)
    temp_ratio = (upper_count + 1) / (lower_count + 1)
    noise_value = (char_count * 0.15) % 7
    dummy_flag = noise_value > 3.5
    
    stats = {
        'total': char_count,
        'uppercase': upper_count,
        'lowercase': lower_count,
        'digits': digit_count,
        'spaces': space_count
    }
    
    return stats


def transform_case_distribution(data):
    ratio = data['uppercase'] / (data['lowercase'] + 1)
    adjusted = ratio * 100
    
    # Dead code path (not used later)
    if adjusted < 10:
        category = 'low'
    elif adjusted < 50:
        category = 'medium'
    else:
        category = 'high'
    
    normalized = min(adjusted, 80)
    return normalized


def calculate_efficiency(data_dict):
    base_score = data_dict['total'] * 0.5
    penalty = 0
    
    if data_dict['digits'] == 0:
        penalty += 15
    
    bonus = 10 if data_dict['spaces'] > 0 and data_dict['uppercase'] > 0 else 0
    
    # Conditional expression usage (required feature)
    adjustment = 5 if data_dict['lowercase'] > data_dict['uppercase'] else -2
    
    final_score = base_score - penalty + bonus + adjustment
    return int(final_score)

# Main execution
input_text = "LLM Evaluation Framework V2.1"

# Step 1: Extract character-level statistics
raw_analysis = analyze_text_properties(input_text)

# Step 2: Compute derived metrics (some not used)
distribution_metric = transform_case_distribution(raw_analysis)
synthetic_index = (raw_analysis['total'] + raw_analysis['digits']) * 1.75

# Step 3: Calculate final efficiency score (target variable)
efficiency_score = calculate_efficiency(raw_analysis)

# Output result
print(f"Result: {efficiency_score}")