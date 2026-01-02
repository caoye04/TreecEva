import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant computation: counts transitions but not used later
    transitions = 0
    for t in range(1, len(trend)):
        if trend[t] != trend[t-1]:
            transitions += 1

    # Real logic: sum of positive trends
    positive_trend_sum = sum(1 for t in trend if t == 1)
    return positive_trend_sum


def clean_string_data(raw_str):
    # Dummy cleaning that's overcomplicated
    stripped = raw_str.strip()
    lowercased = stripped.lower()
    no_punct = ''.join(ch for ch in lowercased if ch.isalnum() or ch.isspace())
    tokenized = no_punct.split()
    filtered_words = [word for word in tokenized if len(word) > 2]
    joined = ' '.join(filtered_words)
    char_count = len(joined.replace(' ', ''))  # Not used
    return joined


def preprocess_dataset(data_list, config_map):
    temp_result = []
    scaling_factor = config_map.get('scale', 1)
    offset = config_map.get('offset', 0)
    
    for item in data_list:
        if isinstance(item, int):
            temp_result.append(item * scaling_factor + offset)
        elif isinstance(item, str):
            cleaned = clean_string_data(item)
            length_indicator = len(cleaned) % 5  # Distractor
            temp_result.append(length_indicator)
    
    # Inject synthetic values for complexity
    synthetic_data = [x for x in range(len(temp_result)) if x % 3 == 0]
    merged = list(itertools.chain.from_iterable(zip(temp_result, synthetic_data + [0]*len(temp_result))))[:len(temp_result)]
    
    # Final transformation
    processed = [x + 1 for i, x in enumerate(merged) if i % 2 == 0]
    return processed


def calculate_final_score(data):
    base = sum(data)
    
    # Red herring: complex conditional not affecting result
    adjustments = 0
    if len(data) > 5:
        adjustments += 2
    if sum(1 for x in data if x > 0) == len(data):
        adjustments -= 1  # Never reached due to zero below

    # Introduce irrelevant sequence analysis
    fake_sequence = [1, 3, 2, 5, 4, 6]
    pattern_value = analyze_pattern(fake_sequence)  # Returns 3, unused

    # Actual key operation
    data.append(0)  # This affects average
    avg = sum(data) / len(data)
    penalty = 0
    if avg < 4:
        penalty = 5
    
    final = base - penalty
    return final

# Main execution
raw_input_data = [10, "Test!!!", 5, "hello world", 8, "abc"]
config = {"scale": 1, "offset": -2}

intermediate_data = preprocess_dataset(raw_input_data, config)
# Insert irrelevant string processing
header = "Data Report Q3"
cleaned_header = clean_string_data(header)
description_length = len(cleaned_header)  # Dead variable

processed_data = [x * 2 for x in intermediate_data]  # Further modify

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")