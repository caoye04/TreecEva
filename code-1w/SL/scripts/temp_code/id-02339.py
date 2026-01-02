def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1
    
    # Distractor: Compute average frequency (not used later)
    frequencies = list(char_frequency.values())
    avg_freq = sum(frequencies) / len(frequencies) if frequencies else 0
    
    # Extract unique vowels using set operations
    vowels = set('aeiou')
    found_vowels = set(char_frequency.keys()) & vowels
    vowel_count = len(found_vowels)
    
    # Misleading intermediate calculation
    redundancy_score = 0
    for freq in frequencies:
        if freq > 2:
            redundancy_score += 1

    return vowel_count, len(input_str), redundancy_score


def transform_dataset(raw_values):
    # Apply filtering and transformation
    filtered = [x for x in raw_values if x % 3 == 0]
    shifted_values = [x >> 2 for x in filtered]  # Bitwise distraction
    
    # Dummy combinatorics that doesn't affect final result
    pair_count = 0
    for i in range(len(shifted_values)):
        for j in range(i + 1, len(shifted_values)):
            if shifted_values[i] + shifted_values[j] < 50:
                pair_count += 1
    
    processed = [val ** 2 for val in shifted_values if val > 5]
    return processed if processed else [0]


def calculate_final_score(data):
    base = sum(data)
    adjustment = len(data) * 1.5
    
    # Red herring with string method on numeric context
    str_base = str(base)
    digit_sum = sum(int(d) for d in str_base if d.isdigit())
    
    # Final logic depends only on base and adjustment
    score = base - adjustment + digit_sum
    return int(score)

# Main execution
raw_text = "Dynamic Programming Optimizes Recursive Solutions Efficiently"
data_stream = [18, 27, 36, 45, 54, 63, 72, 81, 90]

# Step 1: Analyze text (produces side results)
letter_info = analyze_text_patterns(raw_text)

# Irrelevant state tracking
state_log = []
for i in range(3):
    state_log.append(f"Stage {i}: Active")

# Step 2: Process numerical data
processed_data = transform_dataset(data_stream)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")