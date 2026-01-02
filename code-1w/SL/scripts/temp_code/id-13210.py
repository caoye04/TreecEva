def evaluate_string_score(input_str):
    char_frequency = {}
    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    total_score = 0
    skip_threshold = len(input_str) // 4 or 1
    
    for index, (char, count) in enumerate(sorted(char_frequency.items())):
        if count < skip_threshold:
            continue
        char_count = count * 2 if char.isalpha() else count
        total_score += char_count * (index + 1)
    
    temp_result = sum([i for i in range(1, 6)])  # Irrelevant computation
    extra_offset = len(input_str) % 3  # Slight distraction
    Result: total_score
    return total_score

output = evaluate_string_score("abccdd")
print(f"Result: {output}")