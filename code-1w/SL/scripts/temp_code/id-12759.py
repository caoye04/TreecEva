def analyze_text_quality(text):
    if not text:
        return 0
    uppercase_count = sum(1 for c in text if c.isupper())
    lowercase_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    special_char_count = len(text) - uppercase_count - lowercase_count - digit_count
    
    # Distractor: irrelevant normalization
    normalized_upper = uppercase_count / max(len(text), 1) * 100
    normalized_lower = lowercase_count / max(len(text), 1) * 100
    
    score = (uppercase_count * 1.5 + lowercase_count * 1.0 + digit_count * 2.0)
    penalty = 0.5 * special_char_count
    return score - penalty


def filter_sensitive_terms(words):
    # Dead code path - never actually used in final computation
    banned = ['error', 'fail', 'bug']
    clean_list = [w for w in words if w.lower() not in banned]
    return clean_list


def calculate_final_score(data, threshold):
    base_values = [len(item) for item in data]
    adjusted = [val * 1.1 for val in base_values if val > threshold]
    
    # Intermediate distractor variables
    temp_sum = sum(adjusted)
    temp_avg = temp_sum / len(adjusted) if adjusted else 0
    adjustment_factor = temp_avg * 0.1 if temp_avg > 5 else 0.05
    
    processed_texts = [item.upper().strip() for item in data]
    
    # Real work begins here
    total_weighted = 0
    for txt in processed_texts:
        quality = analyze_text_quality(txt)
        if 'SECRET' in txt:
            quality *= 1.8
        elif 'PUBLIC' in txt:
            quality *= 0.7
        total_weighted += quality
    
    # Final calculation with meaningful logic
    count_bonus = len([d for d in data if len(d) >= threshold]) * 3
    stability_modifier = len(set(data))  # bonus for diversity
    
    # Irrelevant debug print (has no effect)
    debug_info = {"items": len(data), "unique": stability_modifier}
    
    final_score = int(total_weighted + count_bonus + stability_modifier - adjustment_factor)
    return final_score

# Main execution
raw_data = ["PublicDoc", "SECRET7", "NormalEntry", "SECURE123", "public_note"]
data = [s.replace("o", "0").replace("e", "3") for s in raw_data]  # minor obfuscation
threshold = 7
final_score = calculate_final_score(data, threshold)
print(f"Result: {final_score}")