from collections import Counter

def analyze_text_patterns(input_str):
    words = input_str.lower().split()
    word_count = Counter(words)
    unique_words = set(word for word in words if len(word) > 2)
    
    # Compute frequency score for longer words
    freq_score = sum(count for word, count in word_count.items() if len(word) >= 4)
    
    # Irrelevant distraction: counting vowels (not used in final result)
    vowel_count = sum(1 for c in input_str if c.lower() in 'aeiou')
    
    return freq_score

def calculate_final_score():
    text = "explore advanced patterns in code reasoning with complex logic chains"
    base_score = analyze_text_patterns(text)
    
    adjustment = 1 if 'reasoning' in text else -1
    multiplier = 2 if len(text.split()) > 5 else 1
    
    # Conditional expression used as per requirement
    result = base_score * multiplier + (10 if text.startswith('explore') else 0)
    
    # Distractor variable - not directly related
    temp_data = [len(word) for word in text.split() if word.endswith('s')]
    
    return result

# Execution point
result = calculate_final_score()
print(f"Result: {result}")