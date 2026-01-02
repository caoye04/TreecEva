def analyze_pattern(data, limit):
    char_frequency = {}
    for char in data:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    filtered_chars = []
    temp_sum = 0
    for key in char_frequency:
        if char_frequency[key] >= limit:
            filtered_chars.append(key)
            temp_sum += ord(key) - ord('a') + 1
    
    result_count = len(filtered_chars) * temp_sum
    
    # Irrelevant distraction: unused variable
    debug_info = "Analysis complete"
    
    return result_count

# Input data
text_data = "Programming languages are powerful tools for problem solving"
threshold = 3

result_count = analyze_pattern(text_data, threshold)
print(f"Result: {result_count}")