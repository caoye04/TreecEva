import itertools

# Password pattern analysis
def analyze_patterns(digits, length):
    # Generate all possible combinations of digits with given length
    all_patterns = list(itertools.product(digits, repeat=length))
    
    # Count patterns that don't start and end with the same digit
    valid_patterns = [p for p in all_patterns if sum(p) <= 10]
    valid_combinations = len([p for p in valid_patterns if p[0] != p[-1]])
    
    # Calculate some statistics
    avg_sum = sum(sum(p) for p in valid_patterns) / len(valid_patterns) if valid_patterns else 0
    
    return valid_combinations, avg_sum

# Security parameters
digits = [1, 2, 3, 4]
length = 3

# Run analysis
result, avg = analyze_patterns(digits, length)
print(f"Result: {result}")