import itertools

def preprocess_data(raw):
    # Irrelevant preprocessing (distractor)
    cleaned = [x for x in raw if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return [round(x, 3) for x in normalized]

def filter_outliers(seq):
    # Dead code path — never called
    mean_val = sum(seq) / len(seq)
    return [x for x in seq if abs(x - mean_val) < 2]

def transform_bits(value):
    # Bit manipulation red herring
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 1

def accumulate_with_weights(series, factors):
    # Relevant but obscured accumulation logic
    weighted = []
    for i, val in enumerate(series):
        weight = factors[i % len(factors)]
        weighted.append(val * weight)
    return weighted

def generate_combinations(values):
    # Distractor using itertools — produces unused data
    combos = []
    for r in range(2, 4):
        combos.extend(itertools.combinations(values, r))
    return [sum(combo) for combo in combos[:10]]  # Partial use, misleading

def compute_entropy(arr):
    # Scientific-looking but irrelevant computation
    total = sum(arr)
    probs = [x / total for x in arr if x > 0]
    from math import log2
    return -sum(p * log2(p) for p in probs)

def calculate_final_score(dataset, importance):
    # Core function with mixed relevant and irrelevant steps
    
    # Step 1: Preprocess — actually used
    processed = preprocess_data(dataset)
    
    # Step 2: Generate decoy entropy (distraction)
    _entropy = compute_entropy(processed)  # Unused later
    
    # Step 3: Accumulate with weights — critical path
    accumulated = accumulate_with_weights(processed, importance)
    
    # Step 4: Apply bit transformation to each (red herring)
    disguised = [transform_bits(int(x * 100)) for x in accumulated]  # Not used in final result
    
    # Step 5: Create combination sums — looks important, not used
    combo_sums = generate_combinations([int(x) for x in accumulated])
    
    # Step 6: Real computation hidden here
    base_score = sum(accumulated) * 1000
    
    # Step 7: Conditional adjustment based on length (relevant)
    if len(processed) >= 5:
        bonus = 17
    else:
        bonus = 5
    
    # Step 8: Add constant derived from bitwise pattern (misleading comment)
    # The following line uses a fixed offset — not actually from bits
    magic_offset = 42  # Named to mislead, but constant
    
    # Final score calculation — only some inputs matter
    final_score = base_score + bonus + magic_offset
    
    # Irrelevant print statements (don't affect logic)
    debug_flag = False
    if debug_flag:
        print('Entropy:', _entropy)
        print('Combos:', combo_sums)
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    sensor_data = [150, -50, 200, 300, 100, 400]  # Includes negative (filtered out)
    feature_weights = [0.1, 0.3, 0.6]
    
    # Extraneous variable
    calibration_matrix = [[1, 2], [3, 4]]
    
    # Key execution point
    final_score = calculate_final_score(sensor_data, feature_weights)
    
    # Output result as required
    print(f"Target result: {final_score}")