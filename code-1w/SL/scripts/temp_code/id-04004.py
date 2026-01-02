def balance_score(seq):
    length = len(seq)
    midpoint = length // 2
    left_part = seq[:midpoint]
    right_part = seq[midpoint:]
    
    # Count vowels in left half (irrelevant for final result, mild distraction)
    vowel_count = sum(1 for c in left_part if c.lower() in 'aeiou')
    
    # Actual logic: count consonants in reversed right half
    reversed_right = right_part[::-1]
    consonant_count = sum(1 for c in reversed_right if c.isalpha() and c.lower() not in 'aeiou')
    
    # Compute score based on positional weights
    weighted_sum = 0
    for i, char in enumerate(reversed_right):
        if char.isupper():
            weighted_sum += i + 1  # weight by 1-indexed position
    
    result = consonant_count * 2 + weighted_sum
    return result

# Main execution
sequence = "ProgrammingIsFun"
result = balance_score(sequence)
print(f"Result: {result}")