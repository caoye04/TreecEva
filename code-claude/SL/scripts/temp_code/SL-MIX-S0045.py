import itertools

def calculate_overlap(sequence1, sequence2, use_optimization=False):
    # Calculate the overlap between two sequences using different methods
    potential_overlap = 0
    distraction_factor = sum(ord(c) % 7 for c in ''.join(map(str, sequence1)))
    
    # Unnecessary computation to distract
    noise_values = [x**2 % 10 for x in range(len(sequence1) + len(sequence2))]
    
    # Red herring: complex but irrelevant computation
    def generate_noise(seq):
        noise = 0
        for i, val in enumerate(seq):
            if i % 3 == 0:
                noise += val * 2
            elif i % 3 == 1:
                noise -= val // 2
            else:
                noise ^= val & 0x0F
        return abs(noise) % 100
    
    noise_level = generate_noise(sequence1) if len(sequence1) > 2 else 0
    
    if not use_optimization:
        # This branch is never taken in our question
        common_elements = set(sequence1).intersection(set(sequence2))
        return len(common_elements) * 10 + noise_level
    
    # The actual computation we care about
    # Count elements that appear in both sequences
    s1_counter = {}
    for item in sequence1:
        s1_counter[item] = s1_counter.get(item, 0) + 1
    
    # More distraction: unnecessary list comprehension
    filtered_seq2 = [x for x in sequence2 if x % 2 == 0 or x % 3 == 0]
    
    # Misleading variable that seems important but isn't used for the result
    overlap_candidates = []
    
    # The actual calculation mixed with distractions
    overlap_count = 0
    for item in sequence2:
        if item in s1_counter and s1_counter[item] > 0:
            overlap_count += 1
            s1_counter[item] -= 1
            # Distractor: collect items but never use them
            overlap_candidates.append(item)
    
    # More distractions that don't affect the result
    if len(overlap_candidates) > 0:
        max_candidate = max(overlap_candidates)
        min_candidate = min(overlap_candidates)
        candidate_range = max_candidate - min_candidate
    else:
        candidate_range = 0
    
    # Final calculation with misleading variables
    weighted_noise = noise_level / 100 if noise_level > 50 else 0
    apparent_result = overlap_count * 2 - weighted_noise
    
    # The actual result we want
    return overlap_count

# Setup test data with distractions
base_values = [3, 6, 9, 12, 15, 18]
distractor_values = [i**2 % 20 for i in range(10)]

# More distractions: complex sequence generation
expanded_values = list(itertools.chain.from_iterable(
    [base_values[i:i+2] for i in range(0, len(base_values), 2)]
))

# Create our sequences with some overlap
seq1 = [3, 7, 9, 12, 15]
seq2 = [4, 9, 10, 12, 20]

# Distraction: compute something that looks important
seq_product = [a*b for a, b in zip(seq1, seq2)] if len(seq1) == len(seq2) else []
seq_sum = sum(seq_product) if seq_product else 0

# Distraction: conditional that's always false
if seq_sum > 1000:
    # This won't be reached
    seq1 = [x // 2 for x in seq1]
    seq2 = [x * 2 for x in seq2]

# The key calculation we're asking about
actual_overlap = calculate_overlap(seq1, seq2, use_optimization=True)

# More distractions after the calculation
modified_overlap = actual_overlap * 3 if actual_overlap > 5 else actual_overlap * 2

# Print the result
print(f"Result: {actual_overlap}")