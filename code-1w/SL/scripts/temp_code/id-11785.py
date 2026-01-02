import itertools

def analyze_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

def validate_sequence(seq):
    return all(x in [-1, 0, 1] for x in seq)

def compute_weighted_sum(values, weights):
    # Misleading: this function is not used in final calculation
    return sum(v * w for v, w in zip(values, weights))

def calculate_final_score(data, multiplier):
    base_score = 0
    adjustments = 0
    
    # Extract rankings and preprocess
    filtered_ranks = [x for x in data if x > 0]
    sorted_ranks = sorted(filtered_ranks)
    
    # Compute rank-based score
    for i, rank in enumerate(sorted_ranks):
        base_score += (len(sorted_ranks) - i) * rank  # higher weight to better ranks
    
    # Dummy transformation - irrelevant
    temp_transform = ''.join(str(r) for r in sorted_ranks)
    padded_str = temp_transform.ljust(10, '0')
    
    # Conditional adjustment based on pattern analysis
    trend = analyze_pattern(sorted_ranks)
    if validate_sequence(trend):
        adjustments += sum(1 for t in trend if t == 1)  # count upward trends
    
    # Use itertools to generate redundant combinations (distractor)
    combos = list(itertools.combinations_with_replacement([1, 2], 3))
    combo_count = len(combos)  # unused but adds cognitive load
    
    # Final composition
    raw_score = base_score + adjustments
    scaling_factor = 1.5 if len(sorted_ranks) > 3 else 1.2
    intermediate = raw_score * scaling_factor
    
    # Apply bonus
    final_score = int(intermediate * multiplier)
    
    # Dead code branch (never executed)
    if False:
        fallback = sum(sorted_ranks) // len(sorted_ranks)
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
rank_data = [4, 2, 7, 1, 5]
bonus_multiplier = 2
offset_value = 33  # unused variable (distractor)
threshold_limit = 100  # misleading constant

# Irrelevant string processing
raw_input_tag = "RANK_001"
formatted_tag = raw_input_tag.lower().replace('_', '-')
display_label = f"[tag:{formatted_tag}]"

# Key computation
final_score = calculate_final_score(rank_data, bonus_multiplier)

print(f"Result: {final_score}")