from itertools import combinations

def analyze_text_segments(text_blocks):
    char_count_map = {}
    total_chars = 0
    for i, block in enumerate(text_blocks):
        clean_block = block.strip().lower()
        char_count_map[i] = len(clean_block)
        total_chars += len(clean_block)
    
    # Irrelevant distraction: counting vowels (not used later)
    vowel_count = 0
    for block in text_blocks:
        for char in block.lower():
            if char in 'aeiou':
                vowel_count += 1

    # Semi-relevant transformation
    processed = []
    for idx, block in enumerate(text_blocks):
        if len(block) > 5:
            processed.append(char_count_map[idx] * (idx + 1))
    
    return processed, total_chars

def calculate_entropy(values):
    # Dead function - not used in main logic
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0
    total = len(values)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy

def calculate_final_score(data_list):
    base_score = 0
    adjustment_factor = 1.5
    
    # Use of zip and enumerate together
    for index, value in enumerate(data_list):
        base_score += value * (index + 1)
    
    # Extra logic with distractor variables
    temp_results = []
    for a, b in combinations(data_list, 2):
        temp_results.append(abs(a - b))
    
    # Secondary adjustment based on pattern match
    pattern_match = 0
    for i in range(1, len(data_list)):
        if data_list[i] > data_list[i-1]:
            pattern_match += 1
    
    # Final computation chain
    scaling_factor = len(temp_results) if temp_results else 1
    bonus = pattern_match * 2.5
    final_score = (base_score + bonus) / adjustment_factor
    
    # Redundant print for confusion
    # print(f'Debug: {scaling_factor=}, {bonus=}')
    
    return int(final_score)

# Main execution
input_texts = [
    "Hello World",
    "LLM reasoning test",
    "Code evaluation framework",
    "Complex logic required"
]

processed_data, total_length = analyze_text_segments(input_texts)

# Dummy entropy calculation (irrelevant)
dummy_entropy = 0
for val in processed_data:
    if val % 2 == 0:
        dummy_entropy += val ** 0.5

final_score = calculate_final_score(processed_data)
print(f'Result: {final_score}')