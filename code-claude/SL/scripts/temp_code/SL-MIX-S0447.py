def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word.lower() if char in vowels)

def is_palindrome(word):
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]

# Text processing function
def process_text(text):
    words = text.split()
    processed = [w.strip('.,!?;:()[]{}"\'\'') for w in words]
    return [word for word in processed if word]

# Calculate word value based on position and characteristics
def calculate_word_value(words):
    position_values = {i+1: (i*2) for i in range(len(words))}
    alternative_values = {i+1: (i*3) for i in range(len(words))}
    
    palindrome_bonus = lambda w: 15 if is_palindrome(w) else 0
    length_factor = lambda w: len(w) // 2
    
    total = 0
    for i, word in enumerate(words, 1):
        # This calculation doesn't affect the result but adds complexity
        temp_value = alternative_values[i] if i % 3 == 0 else position_values[i]
        
        # Actual calculation that matters
        char_value = sum(ord(c) % 10 for c in word if c.isalpha())
        vowel_count = count_vowels(word)
        word_value = char_value + (vowel_count * 5) + palindrome_bonus(word)
        
        # More distraction calculations
        adjusted = word_value * length_factor(word)
        if i % 2 == 0:
            adjusted += 3
        
        total += word_value
    
    return total

# Main program
text = "radar level deed stats kayak"
processed_text = process_text(text)

# Extra processing that doesn't affect the final result
duplicate_check = {}
for word in processed_text:
    duplicate_check[word] = duplicate_check.get(word, 0) + 1

# Filter words based on some criteria
filter_condition = lambda w: len(w) >= 4
filtered_words = [word for word in processed_text if filter_condition(word)]

# Calculate final score
word_score = calculate_word_value(filtered_words)

# Extra calculation that doesn't affect the answer
adjusted_score = word_score + len(text) - len(text)

print(f"Result: {word_score}")