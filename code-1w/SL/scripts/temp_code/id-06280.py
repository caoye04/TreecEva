def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq

# Irrelevant helper function (distractor)
def compute_entropy(frequency_dict):
    import math
    total = sum(frequency_dict.values())
    entropy = 0
    for count in frequency_dict.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Semi-relevant preprocessing step
def extract_vowel_count(frequency_dict):
    vowels = 'aeiou'
    return sum(frequency_dict.get(v, 0) for v in vowels)

# Core logic with state tracking and dictionary usage
def validate_sequence(numbers):
    if len(numbers) < 3:
        return False
    for i in range(2, len(numbers)):
        if numbers[i] != numbers[i-1] + numbers[i-2]:
            return False
    return True

# Recursive helper to count valid subsequences (simple recursion)
def count_valid_subsequences(arr, index=0, current=[]):
    if index == len(arr):
        return 1 if validate_sequence(current) and len(current) >= 3 else 0
    # Include current element
    include = count_valid_subsequences(arr, index + 1, current + [arr[index]])
    # Exclude current element
    exclude = count_valid_subsequences(arr, index + 1, current)
    return include + exclude

# Main scoring logic
def calculate_final_score(log_data):
    raw_text = log_data['raw_input']
    num_sequence = log_data['sequence']
    
    # Step 1: Analyze character frequency (dictionary op)
    char_freq = analyze_frequency(raw_text)
    
    # Step 2: Compute vowel count (semi-relevant)
    vowel_count = extract_vowel_count(char_freq)
    
    # Step 3: Calculate entropy (distraction - not used later)
    entropy_value = compute_entropy(char_freq)  # Dead end
    
    # Step 4: Count valid Fibonacci-like subsequences
    sequence_count = count_valid_subsequences(num_sequence)
    
    # Step 5: Apply weighting based on length patterns
    length_bonus = 0
    for k, v in char_freq.items():
        if v > 2:
            length_bonus += 1
    
    # Step 6: Final score computation
    base_score = vowel_count * 10
    adjustment = sequence_count * 7
    final_adjusted = base_score + adjustment + length_bonus
    
    # Misleading complex expression that simplifies deterministically
    temp_debug = (base_score * adjustment) // (vowel_count + 1) if vowel_count else 0
    temp_debug = (temp_debug % 97)  # Unused variable
    
    # Critical assignment
    final_score = final_adjusted - 5
    return final_score

# Input data construction
input_text = "DataAnalysisWithComplexPatternsAndFrequentCharacters"
data_log = {
    'raw_input': input_text,
    'sequence': [1, 1, 2, 3, 5, 8],  # Fibonacci - all subsequences valid?
    'timestamp': 1712345678,
    'version': '2.1.0'
}

# Execution point
final_score = calculate_final_score(data_log)
print(f"Target result: {final_score}")