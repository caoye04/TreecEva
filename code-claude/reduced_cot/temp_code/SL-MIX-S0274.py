def calculate_prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

def calculate_word_value(text, key):
    # Calculate base value from character positions
    base_value = 0
    vowel_count = 0
    consonant_sum = 0
    special_chars = 0
    
    # Track character frequencies for distraction
    char_freq = {}
    for c in text.lower():
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    
    # Process each character with its position
    for i, c in enumerate(text.lower()):
        if c.isalpha():
            # Position value (1-based index)
            pos_value = i + 1
            
            # Check if vowel or consonant
            if c in 'aeiou':
                vowel_count += 1
                # Vowels contribute differently
                base_value += (ord(c) - 96) * 2
            else:
                consonant_sum += (ord(c) - 96)
                base_value += (ord(c) - 96)
        elif c.isdigit():
            # Digits contribute their numerical value
            base_value += int(c) * 3
        else:
            special_chars += 1
    
    # Calculate distractor values that won't be used
    most_common = max(char_freq.values()) if char_freq else 0
    least_common = min(char_freq.values()) if char_freq else 0
    distinct_chars = len(char_freq)
    
    # Apply cipher key transformation
    transformed_value = 0
    for digit in str(key):
        transformed_value += int(digit)
    
    # Calculate final score using relevant factors
    result = (base_value * transformed_value) // 2
    
    # Apply conditional adjustments
    if vowel_count > 5:
        result += vowel_count * 2
    else:
        result += vowel_count
        
    if consonant_sum > 50:
        result = result // 2 + 10
    
    # Calculate some irrelevant values for distraction
    prime_factors = calculate_prime_factors(base_value)
    prime_sum = sum(prime_factors)
    
    # More distraction calculations that don't affect the result
    complexity_score = distinct_chars * most_common - least_common
    pattern_value = sum([ord(c) for c in text if c.isupper()])
    
    return result

# Main program with test cases
def analyze_message_patterns(messages):
    pattern_scores = []
    for msg in messages:
        # Calculate character distribution
        char_counts = {}
        for c in msg:
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1
                
        # Find most common character
        most_common = max(char_counts.items(), key=lambda x: x[1]) if char_counts else ('', 0)
        pattern_scores.append((most_common[0], most_common[1]))
    return pattern_scores

# Test data
messages = [
    "Hello World",
    "Python Programming",
    "Cryptography is fun!"
]

# This function is never used but serves as a distraction
def calculate_entropy(text):
    length = len(text)
    if length == 0:
        return 0
    
    # Calculate character frequencies
    freq = {}
    for c in text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    
    # Calculate entropy
    entropy = 0
    for count in freq.values():
        probability = count / length
        entropy -= probability * (probability ** 0.5)
    
    return entropy * 100

# More distracting data and calculations
cipher_systems = {
    'caesar': {'complexity': 3, 'security': 1},
    'vigenere': {'complexity': 7, 'security': 5},
    'rsa': {'complexity': 10, 'security': 9}
}

# Process messages with pattern analysis (distraction)
pattern_results = analyze_message_patterns(messages)
pattern_count = sum(count for _, count in pattern_results)

# The actual task
encoded_message = "Code Challenge"
cipher_key = 42

# Calculate the score - this is what we're being asked about
final_score = calculate_word_value(encoded_message, cipher_key)

# More distraction - these lines don't affect final_score
bonus_points = len([c for c in encoded_message if c.isupper()])
penalty = sum([ord(c) for c in encoded_message if c in '!@#$%^&*()'])

print(f"Result: {final_score}")
