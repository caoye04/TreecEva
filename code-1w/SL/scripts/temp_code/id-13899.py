def analyze_character_counts(text_blocks):
    char_count_map = {}
    for block in text_blocks:
        count = len(block.replace(' ', ''))
        char_count_map[block] = count

    counts = list(char_count_map.values())
    shifted_counts = [c + 2 for c in counts]
    doubled_counts = [c * 2 for c in counts]  # distractor

    processed_data = [sc for sc in shifted_counts if sc > 10]
    sorted_data = sorted(processed_data, reverse=True)  # distractor

    filtered_sum = sum([x for x in processed_data if x % 3 == 0])
    return filtered_sum

input_blocks = ["hello world", "python code", "ai reasoning test", "complex logic"]
temp_result = analyze_character_counts(input_blocks)
Result: {temp_result}