from collections import Counter, defaultdict

def analyze_text_frequencies(text):
    # Process text and count character frequencies
    char_counts = Counter(text.lower())
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {c for c in 'bcdfghjklmnpqrstvwxyz'}
    
    vowel_count = sum(char_counts[v] for v in vowels)
    consonant_count = sum(char_counts[c] for c in consonants)
    
    # This ratio is not used in the final calculation
    ratio = vowel_count / max(1, consonant_count)
    return char_counts, vowel_count, consonant_count

def calculate_sequence_metrics(numbers):
    # Calculate various metrics on the sequence
    if not numbers:
        return 0, 0, 0
    
    # These calculations are misleading and not used in final result
    avg = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers) // 2]
    product = 1
    for num in numbers[:3]:  # Only first 3 numbers affect product
        product *= num
    
    # Only this value is used later
    weighted_sum = sum(i * val for i, val in enumerate(numbers, 1))
    return avg, median, weighted_sum

def process_data(raw_data):
    # Process the raw data through various transformations
    word_lengths = [len(word) for word in raw_data.split()]
    
    # Create a mapping that tracks position-based values
    position_map = defaultdict(int)
    for i, length in enumerate(word_lengths):
        # Only even positions contribute to the final calculation
        if i % 2 == 0:
            position_map[i] = length
    
    # Extract numerical values from the text
    numerical_values = []
    for char in raw_data:
        if char.isdigit():
            numerical_values.append(int(char))
    
    # Apply bitwise operations - these are distractors
    bit_values = []
    for i in range(len(numerical_values) - 1):
        bit_values.append(numerical_values[i] ^ numerical_values[i+1])
    
    # Calculate string-based metrics
    char_counts, vowels, consonants = analyze_text_frequencies(raw_data)
    
    # Only the sum of word_lengths and numerical_values are relevant
    return {
        'word_lengths': word_lengths,
        'position_map': position_map,
        'numerical_values': numerical_values,
        'bit_values': bit_values,
        'char_frequencies': char_counts,
        'vowel_count': vowels,
        'consonant_count': consonants
    }

def calculate_weighted_score(data, weights):
    # This function calculates the final weighted score
    # Several calculations are performed but only some contribute to result
    
    # Distractor calculations
    frequency_score = sum(data['char_frequencies'].values()) * weights.get('frequency', 0)
    vowel_ratio = data['vowel_count'] / max(1, data['consonant_count'])
    linguistic_score = data['vowel_count'] * weights.get('vowels', 0) - data['consonant_count'] * 0.5
    
    # Relevant calculations
    length_score = sum(data['word_lengths']) * weights.get('length', 0)
    
    # More distractors
    bit_score = sum(data['bit_values']) * weights.get('bits', 0) if data['bit_values'] else 0
    
    # Calculate metrics on numerical values (only weighted_sum is used)
    avg, median, weighted_sum = calculate_sequence_metrics(data['numerical_values'])
    numerical_score = weighted_sum * weights.get('numerical', 0)
    
    # Position score uses only even positions (from position_map)
    position_score = sum(data['position_map'].values()) * weights.get('position', 0)
    
    # Combine scores - but only some components are actually used
    combined_score = length_score + numerical_score + position_score
    
    # Apply a final transformation
    if combined_score > 100:
        combined_score = combined_score % 100 + 50
    elif combined_score < 0:
        combined_score = abs(combined_score) % 30
    
    return round(combined_score, 2)

# Main execution
raw_text = "Python 3.9 introduces several new features such as Union Operators in dict."

# Process the text data
processed_data = process_data(raw_text)

# Define weights for different components
weights = {
    'frequency': 0.1,  # Distractor - not used in final calculation
    'vowels': 0.2,      # Distractor - not used in final calculation
    'length': 1.5,      # Used in final calculation
    'bits': 0.3,        # Distractor - not used in final calculation
    'numerical': 2.0,   # Used in final calculation
    'position': 0.75    # Used in final calculation
}

# Calculate the final score
final_score = calculate_weighted_score(processed_data, weights)
print(f"Result: {final_score}")