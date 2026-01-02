def analyze_text_quality(text):
    words = text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Distractor: irrelevant sentiment analysis
    positive_words = ['good', 'great', 'excellent', 'amazing']
    sentiment_score = sum(1 for word in words if word.lower() in positive_words)
    
    complexity_metric = avg_length * len(words)  # Not used later
    return avg_length


def preprocess_entry(entry_str):
    # Use string methods meaningfully
    cleaned = entry_str.strip().lower().replace(';', ',')
    parts = cleaned.split(',')
    parsed_values = []
    
    for part in parts:
        stripped = part.strip()
        if stripped.isdigit():
            parsed_values.append(int(stripped))
        elif '.' in stripped:
            try:
                parsed_values.append(float(stripped))
            except ValueError:
                continue
    
    # Dead code path (never accessed due to logic above)
    if 'error' in cleaned:
        raise ValueError("Invalid format")
    
    return parsed_values


def calculate_statistics(numbers):
    if not numbers:
        return 0, 0, 0
    
    sorted_nums = sorted(numbers)
    total = sum(sorted_nums)
    count = len(sorted_nums)
    mean_val = total / count
    
    # Middle computation with no impact
    squared_deviations = [(x - mean_val)**2 for x in numbers]
    variance_estimate = sum(squared_deviations) / count if count > 1 else 0
    
    # Return only what's needed
    return total, mean_val, count


def calculate_final_score(data_list):
    flat_data = []
    for item in data_list:
        if isinstance(item, list):
            flat_data.extend(item)
        else:
            flat_data.append(item)
    
    # Filter out non-numeric
    numeric_data = [x for x in flat_data if isinstance(x, (int, float)) and x >= 0]
    
    # Primary logic chain
    total_sum, mean_val, n = calculate_statistics(numeric_data)
    
    adjustment_factor = 1.0
    if n > 5:
        adjustment_factor = 1.1
    elif n > 3:
        adjustment_factor = 1.05
    
    base_score = total_sum * mean_val
    adjusted_score = base_score * adjustment_factor
    
    # Red herring: unused transformation
    inverted_vals = [1/(x+1) for x in numeric_data]  
    entropy_proxy = -sum(v * v for v in inverted_vals) if inverted_vals else 0
    
    return int(adjusted_score)

# Simulated input data
raw_entries = [
    "10; 20; 30",
    "45, 12.5, 8",
    "100, 60, 25",
    "invalid; data; 0"
]

processed_data = []
for entry in raw_entries:
    parsed = preprocess_entry(entry)
    processed_data.append(parsed)

# Irrelevant text analysis (distractor)
text_sample = "This is a great example of excellent writing with amazing clarity."
quality_metric = analyze_text_quality(text_sample)

# Core execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")