def analyze_text_patterns(text_block):
    char_count = len(text_block)
    word_list = text_block.split()
    word_length_map = {word: len(word) for word in word_list}
    long_words = [word for word in word_list if len(word) > 5]
    avg_word_length = sum(len(w) for w in word_list) / len(word_list) if word_list else 0
    
    # Distractor: frequency analysis (not used later)
    letter_freq = {}
    for c in text_block.lower():
        if c.isalpha():
            letter_freq[c] = letter_freq.get(c, 0) + 1
    sorted_freq = sorted(letter_freq.items(), key=lambda x: -x[1])
    
    return word_length_map, avg_word_length, long_words


def transform_data(raw_mapping, multiplier):
    scaled_values = [val * multiplier for val in raw_mapping.values()]
    threshold = 10 * multiplier
    filtered_vals = [v for v in scaled_values if v < threshold]
    
    # Distractor: reverse mapping that isn't used
    reversed_map = {v: k for k, v in raw_mapping.items() if v % 2 == 0}
    
    adjusted_total = sum(filtered_vals) + len(filtered_vals)
    return adjusted_total


def calculate_final_score(data_chunk):
    temp_result = 0
    for item in data_chunk:
        if isinstance(item, dict):
            keys = list(item.keys())
            if 'score' in keys:
                temp_result += item['score']
                if 'modifier' in keys:
                    temp_result *= item['modifier']
    
    # Semi-relevant transformation
    adjustment_factor = len(data_chunk) or 1
    temp_result = temp_result / adjustment_factor
    
    # Final computation step
    final_score = int(temp_result + 37.8)
    return final_score

# Main execution flow
input_text = "algorithm benchmark performance evaluation system integration test"

# Step 1: Text analysis
mapping, avg_len, long_words = analyze_text_patterns(input_text)

# Step 2: Data transformation (distractor usage)
dummy_multiplier = 3
intermediate_sum = transform_data(mapping, dummy_multiplier)

# Step 3: Prepare structured data for scoring
raw_entries = [
    {'score': 8, 'tag': 'A'},
    {'score': 5, 'modifier': 2, 'tag': 'B'},
    {'score': 10, 'modifier': 1, 'tag': 'C'}
]

# Step 4: Modify entries based on average word length (semi-relevant)
if avg_len > 5.0:
    raw_entries.append({'score': 4, 'tag': 'D'})

# Step 5: Process data
processed_data = []
for entry in raw_entries:
    new_entry = {k: v for k, v in entry.items()}
    if 'modifier' in new_entry:
        new_entry['score'] = new_entry['score'] ** (new_entry['modifier'])
    processed_data.append(new_entry)

# Step 6: Calculate final score
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")