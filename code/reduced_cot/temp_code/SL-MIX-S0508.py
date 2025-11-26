def process_data(data_string):
    character_map = {}
    total_chars = len(data_string)
    
    for char in data_string:
        character_map[char] = character_map.get(char, 0) + 1
    
    # Filter characters that appear more than once
    filtered_chars = {k: v for k, v in character_map.items() if v > 1}
    final_count = sum(filtered_chars.values())
    
    # Some additional processing that doesn't affect the result
    temp_list = list(data_string)
    temp_list.reverse()
    reversed_string = ''.join(temp_list)
    
    return final_count

data_sample = "programming_assessment"
result = process_data(data_sample)
print(f"Result: {result}")