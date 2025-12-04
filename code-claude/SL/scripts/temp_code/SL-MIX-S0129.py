import itertools

# Function to check if a sequence has consecutive repeating elements
def has_consecutive_repeats(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return True
    return False

# Generate all possible 3-digit combinations using digits 1-5
all_digits = [1, 2, 3, 4, 5]
possible_combinations = list(itertools.product(all_digits, repeat=3))

# Filter sequences that meet our criteria
valid_sequences = []
for combo in possible_combinations:
    # Convert to list for easier manipulation
    seq = list(combo)
    
    # Check various conditions
    sum_of_digits = sum(seq)
    has_repeats = has_consecutive_repeats(seq)
    
    # Add sequence if sum is greater than 7 and has no consecutive repeats
    if sum_of_digits > 7 and not has_repeats:
        valid_sequences.append(seq)

# Find the maximum length among valid sequences
max_sequence_length = max(len(seq) for seq in valid_sequences)

# Additional statistics (not relevant to the answer)
total_valid = len(valid_sequences)
avg_sum = sum(sum(seq) for seq in valid_sequences) / total_valid if total_valid > 0 else 0

print(f"Result: {max_sequence_length}")