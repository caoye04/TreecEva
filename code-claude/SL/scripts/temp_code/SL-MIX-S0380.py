import itertools

# Analyzing password sequence patterns
def is_valid_sequence(sequence):
    # Check if sequence has no consecutive duplicates
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return False
    
    # Check if sequence contains both even and odd digits
    has_even = False
    has_odd = False
    for digit in sequence:
        if digit % 2 == 0:  # even
            has_even = True
        else:  # odd
            has_odd = True
        if has_even and has_odd:
            break
    
    return has_even and has_odd

# Available digits for the password
digits = [1, 3, 5, 6, 8]
password_length = 3

# Generate all possible combinations
all_possible = list(itertools.product(digits, repeat=password_length))

# Count valid combinations
valid_combinations = len(list(filter(is_valid_sequence, all_possible)))

# Display result
print(f"Result: {valid_combinations}")