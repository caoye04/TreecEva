def process_text(text, filters=None):
    # Apply text transformations based on filters
    if filters is None:
        filters = []
    
    processed = text
    for filter_type in filters:
        if filter_type == 'uppercase':
            processed = processed.upper()
        elif filter_type == 'lowercase':
            processed = processed.lower()
        elif filter_type == 'reverse':
            processed = processed[::-1]
    
    # Calculate character frequencies
    char_freq = {}
    for char in processed:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    return processed, char_freq

def analyze_pattern(text):
    # Find repeating patterns in text
    patterns = {}
    text_length = len(text)
    
    for i in range(text_length):
        for j in range(i + 1, min(i + 4, text_length) + 1):
            pattern = text[i:j]
            if len(pattern) > 0:
                if pattern in patterns:
                    patterns[pattern] += 1
                else:
                    patterns[pattern] = 1
    
    # This calculation is irrelevant for the final result
    pattern_score = sum([len(p) * count for p, count in patterns.items()])
    return patterns, pattern_score

def calculate_valid_combinations(text):
    # Process the input text
    processed_text, char_frequencies = process_text(text, ['lowercase'])
    
    # Extract only letters for analysis
    letters = ''
    for char in processed_text:
        if char.isalpha():
            letters += char
    
    # This pattern analysis is a distraction
    patterns, _ = analyze_pattern(letters)
    
    # Count vowels and consonants
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    
    for char in letters:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    
    # More distractions: calculate potential anagrams
    unique_letters = set(letters)
    potential_anagrams = len(letters) * len(unique_letters)
    
    # Calculate letter positions for distraction
    letter_positions = {}
    for i, char in enumerate(letters):
        if char not in letter_positions:
            letter_positions[char] = []
        letter_positions[char].append(i)
    
    # Complex calculation that doesn't affect the result
    position_product = 1
    for positions in letter_positions.values():
        if len(positions) > 1:
            position_product *= sum(positions)
    
    # The actual calculation for the result
    valid_count = 0
    for v in range(min(vowel_count + 1, 4)):
        for c in range(min(consonant_count + 1, 5)):
            if v + c >= 3 and v >= 1 and c >= 1:
                combinations = 1
                # Calculate combinations C(vowel_count, v) * C(consonant_count, c)
                for i in range(v):
                    combinations *= (vowel_count - i) / (i + 1)
                for i in range(c):
                    combinations *= (consonant_count - i) / (i + 1)
                valid_count += int(combinations)
    
    # More distraction calculations
    distraction_factor = (vowel_count * consonant_count) // (1 if len(unique_letters) == 0 else len(unique_letters))
    meaningless_result = potential_anagrams + distraction_factor
    
    return valid_count

# Input message
message = "Hello Python World!"

# Calculate letter statistics
original_stats, _ = process_text(message)
distractor_value = len(message) * 2

# More distractions
reversed_message = message[::-1]
reverse_stats, _ = process_text(reversed_message)

# This is the key calculation
final_count = calculate_valid_combinations(message)

# Even more distractions after the key calculation
alternate_count = len(message.replace(' ', ''))
if alternate_count > 10:
    bonus_factor = alternate_count // 5
else:
    bonus_factor = alternate_count // 3

print(f"Result: {final_count}")