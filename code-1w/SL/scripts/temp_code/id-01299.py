def analyze_character_frequency(text_block):
    char_count = {}
    for char in text_block:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1

    frequency_values = list(char_count.values())
    median_freq = sorted(frequency_values)[len(frequency_values) // 2]

    threshold = median_freq * 2
    high_freq_letters = {k for k, v in char_count.items() if v > threshold}

    processed_data = [ord(k) - ord('a') + v for k, v in char_count.items()]
    valid_set = set(range(1, 27))
    filtered_sum = sum(filter(lambda x: x in valid_set, processed_data))
    
    temp_var_ignore = [x for x in range(len(text_block)) if x % 100 == 0]  # Irrelevant tracking
    return filtered_sum

result = analyze_character_frequency("Hello from advanced code reasoning evaluation")
print(f"Result: {result}")