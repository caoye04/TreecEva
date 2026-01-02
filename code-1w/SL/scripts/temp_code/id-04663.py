import itertools

def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

def validate_sequence(seq):
    # Irrelevant validation logic (not used in final computation)
    if len(seq) < 5:
        return False
    sorted_seq = sorted(seq)
    diff = [b - a for a, b in zip(sorted_seq, sorted_seq[1:])]
    return all(d == diff[0] for d in diff)

def preprocess_data(raw):
    # Extract digits from string and convert
    digit_str = ''.join([c for c in raw if c.isdigit()])
    parsed = [int(d) for d in digit_str]
    
    # Dummy transformation (distractor)
    shifted = [(x * 2 + 1) % 10 for x in parsed]
    
    # Actual relevant processing
    filtered = [x for x in parsed if x % 2 == 1]  # Keep only odd digits
    reversed_filtered = list(reversed(filtered))
    
    # Use itertools to create pairwise combinations (semi-relevant)
    pairs = list(itertools.combinations(reversed_filtered, 2))
    pair_sums = [a + b for a, b in pairs if a > b]  # Only include when first > second
    
    # Intermediate score (distractor)
    temp_score = sum(shifted) * 0.1
    
    # Return meaningful data and some noise
    return {
        'processed': reversed_filtered,
        'pair_sums': pair_sums,
        'temp_score': temp_score,
        'length_orig': len(parsed),
        'useless_flag': True
    }

def calculate_final_score(data_dict):
    processed = data_dict['processed']
    pair_sums = data_dict['pair_sums']
    
    base = sum(processed)
    bonus = 0
    
    # Conditional bonus based on length
    if len(processed) > 2:
        bonus += 10
    
    # Additional logic with distractor variables
    avg_pair = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    adjustment = 0
    if avg_pair > 5:
        adjustment -= 3
    else:
        adjustment += 2
    
    # Final calculation
    final = base + bonus + adjustment
    
    # Dead code path (irrelevant)
    if data_dict.get('useless_flag'):
        dummy = [i ** 2 for i in range(3)]
        dummy_sum = sum(dummy)
    
    return int(final)

# Main execution
raw_input = "abc149def723xyz"
data_summary = analyze_pattern(raw_input)  # Unused analysis

# Validate sequence (result unused)
validation_result = validate_sequence([1, 3, 5, 7, 9])

# Preprocess the raw input
dataset = preprocess_data(raw_input)

# Critical statement
final_score = calculate_final_score(dataset)
print(f"Target result: {final_score}")