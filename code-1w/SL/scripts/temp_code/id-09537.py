def analyze_text_composition():
    text = 'algorithmic reasoning enhances computational thinking'
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # Extract unique characters from text
    unique_chars = set(text.replace(' ', ''))
    
    # Identify vowels present in text
    unique_vowels = unique_chars.intersection(vowels)
    
    # Define core letters based on frequency heuristic (arbitrary subset)
    core_letters = {'a', 'e', 'i', 'n', 't', 'h', 's'}
    
    # Calculate intersection of vowels that are also in core set
    common_elements = unique_vowels.intersection(core_letters)
    
    # Distraction: count total consonants (not used in final result)
    total_consonants_in_text = len(unique_chars.intersection(consonants))
    
    # Correction factor based on length parity
    if len(text) % 2 == 0:
        correction_factor = 3
    else:
        correction_factor = 4
    
    # Key computation step
    result = len(unique_vowels.intersection(core_letters)) * correction_factor
    
    # Print final result
    print(f"Result: {result}")

analyze_text_composition()