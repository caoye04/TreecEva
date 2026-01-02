def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    for entry in raw_entries:
        if not isinstance(entry, str) or len(entry.strip()) == 0:
            continue
        stripped = entry.strip().lower()
        if 'error' in stripped:
            continue
        word_count = len(stripped.split())
        temp_sum += word_count
        if word_count > 2:
            cleaned.append(stripped)
    average_length = temp_sum / len(cleaned) if cleaned else 0
    return cleaned, average_length


def calculate_complexity_metric(items):
    metric = 0
    char_freq = {}
    for item in items:
        for char in item:
            char_freq[char] = char_freq.get(char, 0) + 1
    # Irrelevant frequency analysis
    vowels = sum(char_freq.get(v, 0) for v in 'aeiou')
    consonants = sum(char_freq.get(c, 0) for c in 'bcdfghjklmnpqrstvwxyz')
    ratio = vowels / consonants if consonants else 0
    metric = len(char_freq) * ratio
    return round(metric, 4)


def calculate_final_score(data_list):
    scores = []
    total_chars = 0
    for record in data_list:
        # Real computation path
        length_score = len(record) * 0.5
        word_array = record.split()
        unique_words = len(set(word_array))
        repetition_penalty = len(word_array) - unique_words
        adjusted_score = length_score + unique_words - repetition_penalty * 0.3
        scores.append(adjusted_score)
        
        # Distractor: track total chars but not used in final logic
        total_chars += len(record.replace(' ', ''))
    
    # Final aggregation
    base_result = sum(scores) / len(scores) if scores else 0
    
    # Extra irrelevant transformation
    outlier_scores = [s for s in scores if s > base_result * 1.5]
    adjustment_factor = 0.9 if len(outlier_scores) > 1 else 1.0
    
    # Actual answer computation
    final_value = int(base_result * 12.7) + 3
    return final_value

# Main execution
raw_data = [
    "Data point one valid",
    "  Another complete entry with more words  ",
    "error: invalid format",
    "Final working record here",
    "Short ok",
    "",
    "This has seven distinct words present"
]

processed_data, avg_len = preprocess_records(raw_data)
complexity = calculate_complexity_metric(processed_data)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")