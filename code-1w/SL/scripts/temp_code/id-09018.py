def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence.lower() if c in 'aeiou')
    char_frequency = {c: sequence.count(c) for c in set(sequence)}
    total_pairs = sum(1 for i in range(len(sequence)-1) if sequence[i] == sequence[i+1])
    return count_vowels, char_frequency, total_pairs

def validate_sequence(seq):
    if not seq.isalpha():
        return False
    if len(seq) < 5:
        return False
    if seq != seq[::-1]:  # Must be a palindrome
        return False
    return True

def compute_entropy(s):
    import math
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0
    length = len(s)
    for f in freq.values():
        p = f / length
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def calculate_final_score(entry, threshold):
    entry_clean = entry.strip().replace(' ', '').lower()
    
    # Irrelevant preprocessing (distractor)
    reversed_chunks = [entry_clean[i:i+3][::-1] for i in range(0, len(entry_clean), 3)]
    chunk_sum = sum(len(c) for c in reversed_chunks)
    
    if not validate_sequence(entry_clean):
        return -1
    
    # Core logic begins
    vowel_count, _, repeated_adjacent = analyze_pattern(entry_clean)
    entropy_value = compute_entropy(entry_clean)
    
    # Misleading intermediate calculations
    temp_weight = 0
    if len(entry_clean) > threshold:
        temp_weight += 2.5
    if vowel_count >= 3:
        temp_weight += 1.8
    
    # Actual score computation
    raw_score = vowel_count * 7
    if repeated_adjacent > 0:
        raw_score += 15
    if entropy_value > 2.0:
        raw_score += 10
    
    adjustment = len(entry_clean) // 2
    final_score = raw_score + adjustment
    
    # Dead code path (distractor)
    if chunk_sum > 100:
        final_score -= temp_weight  # Never reached
    
    return int(final_score)

# Main execution
user_input = "abccba"
base_threshold = 5

# Extraneous data setup
sample_data = ["abc", "xyz", "racecar", "hello"]
data_analysis = [validate_sequence(s) for s in sample_data]
unused_metric = sum(1 for d in data_analysis if d)

intermediate_result = user_input.upper() + "_PROCESSED"
dummy_list = [compute_entropy(x*3) for x in ['a', 'b', 'c']]

# Key statement
final_score = calculate_final_score(user_input, base_threshold)
print(f"Result: {final_score}")