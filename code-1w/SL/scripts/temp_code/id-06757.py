import math

# Irrelevant helper function (decoy)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Misleading preprocessing with dead-end logic
def filter_outliers(scores):
    mean = sum(scores) / len(scores)
    std_dev = (sum((x - mean) ** 2 for x in scores) / len(scores)) ** 0.5
    return [x for x in scores if abs(x - mean) <= 2 * std_dev]

# Unused transformation chain
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(int(math.sqrt(abs(val))))
    return result

# Core data used in actual computation
rankings = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Distractor variables
baseline = sum(rankings) / len(rankings)
sorted_ranks = sorted(rankings, reverse=True)
duplicate_ranks = [x * 1.05 for x in rankings]
offset_map = {i: val for i, val in enumerate(duplicate_ranks)}

# Red herring: complex but unused bitwise operation
temp_flag = 0
for i in range(len(rankings)):
    temp_flag ^= (i + 1) << (rankings[i] % 4)

temp_flag = temp_flag & 0xFF  # Mask to 8 bits (unused later)

# Irrelevant list slicing and zip usage (set up for distraction)
even_slice = rankings[::2]
odd_slice = rankings[1::2]
paired_data = list(zip(even_slice, odd_slice))

# Fake aggregation path
total_pairs = 0
for a, b in paired_data:
    total_pairs += a + b * 0.1

# Real processing begins here — non-obvious due to noise above
def compute_weighted_sum(values, coeffs):
    # Element-wise multiplication using enumerate
    weighted = [values[i] * coeffs[i] for i in range(len(values))]
    return sum(weighted)

# Secondary transformation with filtering that actually matters
def adjust_for_variance(data):
    variance = sum((x - sum(data)/len(data))**2 for x in data) / len(data)
    adjustment = math.log(1 + variance)  # Stabilizing nonlinear adjustment
    return [x - adjustment for x in data]

# Main processing function buried among decoys
def process_results(ranks, wts):
    # Step 1: Adjust rankings based on internal variance
    adjusted = adjust_for_variance(ranks)
    
    # Step 2: Use slicing to exclude lowest performer temporarily
    trimmed = adjusted[:-1]
    trimmed_weights = wts[:-1]
    
    # Step 3: Re-normalize weights to sum to 1.0
    weight_sum = sum(trimmed_weights)
    normalized_weights = [w / weight_sum for w in trimmed_weights]
    
    # Step 4: Compute primary score
    primary_score = sum(adjusted[i] * wts[i] for i in range(len(adjusted)))
    
    # Step 5: Apply penalty based on spread (using set operations as idiom)
    unique_ranks = set(adjusted)
    duplicate_count = len(adjusted) - len(unique_ranks)
    penalty = duplicate_count * 0.5
    
    # Step 6: Incorporate positional bonuses via enumeration
    bonus = 0
    for idx, val in enumerate(adjusted):
        if val > 85 and idx % 2 == 0:
            bonus += 2.5
    
    # Step 7: Combine all components
    raw_result = primary_score - penalty + bonus
    
    # Step 8: Final clamping and rounding to simulate scoring system
    final = max(50, min(100, raw_result))
    return round(final, 4)

# Critical execution point
final_score = process_results(rankings, weights)

# Output required format
print(f"Result: {final_score}")