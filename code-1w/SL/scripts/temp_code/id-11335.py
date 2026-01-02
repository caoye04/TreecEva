import itertools

def analyze_sequence(data):
    """Irrelevant function analyzing patterns (dead code path)"""
    count = 0
    for a, b in itertools.pairwise(data):
        if (a + b) % 3 == 0:
            count += 1
    return count

def validate_checksum(sequence):
    """Unused validation logic - red herring"""
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val * (i + 1))
    return checksum % 7

def transform_values(arr, key_offset=3):
    """Distraction: complex-looking transformation not fully used"""
    shifted = [((x << 2) ^ key_offset) % 101 for x in arr]
    filtered = [s for s in shifted if s > 25]
    return list(set(filtered))  # Remove duplicates, never actually needed

def compute_entropy(values):
    """Misleading advanced calculation - unused in final result"""
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 6)

def main_logic():
    # Core data
    raw_input = [12, 15, 8, 23, 9, 18]
    
    # Irrelevant transformations (distractors)
    temp_analysis = analyze_sequence(raw_input)
    dummy_checksum = validate_checksum(raw_input)
    processed_layer = transform_values(raw_input, key_offset=5)
    shadow_entropy = compute_entropy(raw_input)
    
    # Real computation chain begins here (nested logic with interdependencies)
    baseline = 14
    metrics = []
    
    for val in raw_input:
        if val < baseline:
            # Two-step adjustment logic
            adjusted = val + 2
            if adjusted % 2 == 0:
                adjusted = (adjusted * 3) // 2  # Branch divergence
        else:
            adjusted = val - 1
            if adjusted % 5 == 0:
                adjusted = (adjusted * 4) // 5  # Another conditional branch
        
        # String-based flag generation (uses string methods - required feature)
        flag_str = f"{adjusted:b}".zfill(5)  # Convert to binary string padded to 5 digits
        ones_count = flag_str.count('1')
        parity_flag = "odd" if ones_count % 2 == 1 else "even"
        
        # Only this part matters: filter and collect based on condition
        if parity_flag == "odd" and adjusted > 10:
            metrics.append(adjusted * 2)
    
    # Critical statement: evaluation using collected metrics
    def evaluate_performance(met, base):
        score = 0
        multiplier = 1
        for i, m in enumerate(met):
            if i % 2 == 0:
                score += m + base
            else:
                score += m * 2
            # Simulated cooldown mechanism
            if score > 100:
                score = score // 2
                multiplier += 1
        return score * multiplier
    
    # Dead code - looks important but unused
    debug_trace = [f"Step_{i}: {v}" for i, v in enumerate(metrics)]
    log_snapshot = '\n'.join(debug_trace).upper()
    
    # Key execution point
    final_score = evaluate_performance(metrics, baseline)
    
    # Irrelevant aggregation
    aggregate_key = ''.join(itertools.chain(['X'], ['Y'], ['Z']))  # Use of itertools
    
    # Output required format
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main_logic()