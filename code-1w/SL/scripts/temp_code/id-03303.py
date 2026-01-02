from itertools import combinations


def analyze_pattern(seq):
    # Irrelevant helper: counts uppercase (no effect on result)
    dummy_upper = sum(1 for c in seq if c.isupper())
    
    # Semi-relevant transformation
    normalized = ''.join(c.lower() for c in seq if c.isalpha())
    
    # Generate all 3-character subsequences
    subseqs = [normalized[i:i+3] for i in range(len(normalized)-2)]
    
    # Count palindromic subsequences
    palindrome_count = sum(1 for s in subseqs if s == s[::-1])
    
    return palindrome_count


def process_sequence(raw_data):
    # Preprocessing: remove digits (distractor step)
    cleaned = ''.join(c for c in raw_data if not c.isdigit())
    
    # Actual relevant transformation: focus on letter frequency
    char_freq = {}
    for c in cleaned:
        if c.isalpha():
            char_freq[c] = char_freq.get(c, 0) + 1
    
    # Compute weighted score based on frequency squared
    freq_score = sum(v**2 for v in char_freq.values())
    
    # Use itertools to generate character triplets
    triplet_combinations = list(combinations(char_freq.keys(), 3))
    complex_metric = len(triplet_combinations) * 2 if freq_score > 10 else 0
    
    # Main logic: case conversion and slicing
    reversed_core = cleaned[::-1].lower()
    mid_section = reversed_core[len(reversed_core)//4 : 3*len(reversed_core)//4]
    
    # Final counting logic
    distinct_chars = set(mid_section)
    base_count = len(distinct_chars)
    
    # Secondary adjustment based on symmetry
    is_symmetric = mid_section == mid_section[::-1]
    adjustment = 5 if is_symmetric else -3
    
    # Final computation
    final_count = base_count * freq_score + adjustment + complex_metric
    
    # Dead code branch (never executed due to prior logic)
    if len(cleaned) < 0:  # Always false
        final_count -= 100
        buffer = [0]*10
        for x in buffer:
            pass  # meaningless loop

    return final_count

# Input data with mixed content
input_str = "XaBbCc123DdEfG!hhIIjkLmNOpqrstUvWxYzAaBb"

# Call the function
final_count = process_sequence(input_str)
print(f"Target result: {final_count}")