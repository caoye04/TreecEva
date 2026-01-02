def analyze_pattern(seq, threshold_map):
    score = 0
    temp_buffer = []
    for idx, (char, val) in enumerate(zip(seq, threshold_map)):
        if char.isalpha():
            offset = ord(char.lower()) - ord('a') + 1
            adjusted_val = val * offset
            if adjusted_val > threshold_map[idx % len(threshold_map)]:
                score += adjusted_val // 2
            else:
                score -= offset
            temp_buffer.append(adjusted_val)
        elif char.isdigit():
            numeric = int(char)
            score += numeric if numeric % 2 == 0 else -numeric
    return score


def validate_sequence_integrity(seq):
    count_alpha = sum(1 for c in seq if c.isalpha())
    count_digits = sum(1 for c in seq if c.isdigit())
    return count_alpha >= count_digits


def calculate_equilibrium(sequences, thresholds):
    equilibrium_score = 0
    history = []
    scaling_factor = 1.5
    
    for i, seq in enumerate(sequences):
        base_threshold = [t * (i + 1) for t in thresholds]
        
        # Irrelevant pre-check (distractor)
        valid = validate_sequence_integrity(seq)
        if not valid:
            continue
        
        raw_score = analyze_pattern(seq, base_threshold)
        
        # Misleading transformation (semi-relevant but unused later)
        transformed = [x ^ i for x in base_threshold[:len(seq)]]
        dummy_sum = sum(transformed) % 100
        
        # Actual contribution logic
        if raw_score > 0:
            equilibrium_score += raw_score * scaling_factor
        else:
            equilibrium_score -= abs(raw_score) / 2
        
        history.append(raw_score)
    
    # Final adjustment based on aggregate behavior
    if len(history) > 2:
        variance_proxy = max(history) - min(history)
        equilibrium_score -= variance_proxy * 0.1
    
    return int(equilibrium_score)

# Input data
sequences = [
    "abc3xYz", 
    "p9q8r7s", 
    "LMN456def"
]

thresholds = [3, 7, 2, 5, 4]

# Execution point of interest
equilibrium_score = calculate_equilibrium(sequences, thresholds)

print(f"Result: {equilibrium_score}")