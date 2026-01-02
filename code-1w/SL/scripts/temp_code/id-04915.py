import itertools

def preprocess_data(entries):
    # Irrelevant transformation (not used in final computation)
    normalized = [round((x - min(entries)) / (max(entries) - min(entries)) * 100) for x in entries]
    return [x for x in entries if x > 0]  # Only keep positive values

def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def calculate_final_score(raw_data, limits):
    filtered = [x for x in raw_data if x >= limits['min_val']]
    
    # Distractor: complex but unused list comprehension
    shifted_pairs = [(a, b) for a, b in itertools.combinations(filtered, 2) if abs(a - b) > 5]
    pair_count_hint = len(shifted_pairs)  # Semi-relevant, not directly used
    
    # Key logic begins
    base_score = 0
    for val in filtered:
        if val % 2 == 0:
            base_score += val // 3  # Integer division
        else:
            base_score += val % 7
    
    adjustment_factor = calculate_entropy(filtered)
    
    # Additional distraction: case conversion on string representation
    str_rep = ''.join([str(int(b)) for b in [base_score > 100, base_score < 200]])
    flag_value = str_rep.upper().count('1')  # Always 1 or 2; mildly relevant
    
    final_score = base_score + int(adjustment_factor) + flag_value
    
    # Dead code path (never executed due to logic)
    if len(filtered) > 1000:
        backup = sum(filtered) // 100
        final_score = max(final_score, backup)
    
    return final_score

def main():
    # Input data
    raw_input = [12, 15, 22, 8, 33, 41, 16, 9, 55]
    config = {'min_val': 10, 'threshold_high': 50}
    
    # Preprocessing (result not fully utilized)
    cleaned_data = preprocess_data(raw_input)
    
    # Dummy intermediate calculations (distractors)
    avg_val = sum(cleaned_data) / len(cleaned_data)
    squared_sum = sum([x**2 for x in cleaned_data])  # Unused
    
    # Critical execution point
    final_score = calculate_final_score(cleaned_data, config)
    
    # Output result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()