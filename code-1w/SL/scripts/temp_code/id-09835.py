def analyze_pattern(seq):
    count_vowels = sum(1 for c in seq.lower() if c in 'aeiou')
    count_consonants = sum(1 for c in seq.lower() if c.isalpha() and c not in 'aeiou')
    unique_chars = len(set(seq.lower()))
    
    # Secondary processing: weight vowels double
    weighted_score = count_vowels * 2 + count_consonants
    
    # Adjust score by uniqueness penalty
    adjusted_score = weighted_score - (unique_chars // 3)
    
    return adjusted_score

sequence = "OptimizationTask"
result = analyze_pattern(sequence)
print(f"Result: {result}")