from collections import Counter

def analyze_text_statistics(text):
    # Normalize text to lowercase for case-insensitive analysis
    normalized_text = text.lower()
    
    # Count frequency of each character
    char_counts = Counter(normalized_text)
    
    # Define vowels for filtering
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # Assign arbitrary weights for analysis (e.g., linguistic impact score)
    vowel_weight = 3
    consonant_weight = 2
    special_char_weight = 1
    
    # Irrelevant distraction: track max frequency (not used in final result)
    max_frequency = max(char_counts.values()) if char_counts else 0
    
    # Compute weighted count only for vowels
    total_weighted_count = sum(weight * count for char, count in char_counts.items() if char in vowels)
    
    # Print result as required
    print(f"Result: {total_weighted_count}")

# Input text for analysis
text_input = "Dynamic programming solves complex problems by breaking them into simpler subproblems."
analyze_text_statistics(text_input)