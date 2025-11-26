def count_unique_characters(text):
    character_set = set()
    total_length = len(text)
    word_count = len(text.split())
    
    for char in text:
        if char.isalpha():
            character_set.add(char.lower())
    
    unique_count = len(character_set)
    print(f"Result: {unique_count}")
    return unique_count

# Main execution
sample_text = "Programming is fascinating"
result = count_unique_characters(sample_text)