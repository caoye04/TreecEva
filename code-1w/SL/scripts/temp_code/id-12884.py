from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] == sequence[j]:
                count += 1
    return count

def compute_entropy(data):
    # Irrelevant entropy calculation (not used in final logic)
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = sum((count / total) * log2(total / count) for count in freq.values())
    return round(entropy, 4)

def calculate_final_score(items, threshold):
    # Main logic starts here
    item_lengths = [len(item) for item in items]
    total_length = sum(item_lengths)
    
    # Track character frequency (semi-relevant)
    char_freq = {}
    for item in items:
        for char in item:
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Generate all 2-letter combinations from first word (distractor)
    if items:
        dummy_combinations = list(combinations(items[0], 2)) if len(items[0]) >= 2 else []
    
    # Filter strings based on length threshold (key filtering step)
    filtered = [item for item in items if len(item) >= threshold]
    
    # Count how many have palindromic substrings of length > 2
    palindrome_count = 0
    for item in filtered:
        found = False
        for i in range(len(item) - 2):
            substr = item[i:i+3]
            if substr == substr[::-1]:
                found = True
                break
        if found:
            palindrome_count += 1
    
    # Weighted score calculation (actual answer source)
    base_score = len(filtered) * 10
    bonus = palindrome_count * 7
    penalty = analyze_pattern(item_lengths) * 2  # Uses repeated lengths as penalty
    
    # Dummy string operations (distraction)
    upper_items = [item.upper() for item in items]
    joined = ''.join(upper_items)
    mid_char = joined[len(joined)//2] if joined else ''
    
    # Final score computation
    final_score = base_score + bonus - penalty
    
    # Additional irrelevant transformation
    shifted = ''.join(chr((ord(c) - ord('A') + 3) % 26 + ord('A')) for c in mid_char)
    
    return final_score

# Input data
input_items = ['radar', 'level', 'hello', 'kayak', 'noon', 'world']
threshold_value = 5

# Execute
result_entropy = compute_entropy([len(x) for x in input_items])  # Unused result
final_score = calculate_final_score(input_items, threshold_value)
print(f"Result: {final_score}")