def analyze_text_data():
    data_items = ['apple', 'PEAR', 'kiwi', 'ORANGE', 'fig', 'BANANA']
    processed_data = [item.upper() if len(item) > 3 else item.lower() for item in data_items]
    
    # Distractor computations that don't affect final_count
    temp_lengths = [len(item) for item in processed_data]
    total_chars = sum(len(item) for item in data_items)
    average_length = total_chars / len(data_items) if data_items else 0
    
    vowel_counts = []
    for item in processed_data:
        vowels = sum(1 for char in item if char.lower() in 'aeiou')
        vowel_counts.append(vowels)
    
    # Relevant computation chain
    filtered_items = [item for item in processed_data if item.startswith('A') or item.startswith('O')]
    intermediate_count = len(filtered_items)
    
    # Another distractor that seems relevant
    character_sum = sum(ord(char) for item in processed_data for char in item[:2])
    
    final_count = intermediate_count * 2 + len([item for item in processed_data if 'I' in item])
    
    print(f"Target result: {final_count}")
    return final_count

analyze_text_data()