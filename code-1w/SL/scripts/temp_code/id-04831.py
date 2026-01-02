def analyze_pattern(sequence):
    """ Analyze binary pattern for symmetry and balance (distractor function) """
    length = len(sequence)
    midpoint = length // 2
    left_half = sequence[:midpoint]
    right_half = sequence[midpoint + (length % 2):]
    symmetric = left_half == right_half[::-1]
    
    # Bitwise analysis (partially relevant)
    ones_count = sum(1 for bit in sequence if bit == '1')
    parity_flag = ones_count & 1
    
    score = 0
    if symmetric:
        score += 10
    if parity_flag:
        score += 5
    return score


def validate_input(data_str):
    """ Validate formatting of input string (distractor) """
    if not data_str.strip():
        return False
    if not all(c in '01' for c in data_str.replace(',', '').replace(' ', '')):
        return False
    segments = data_str.split(',')
    for seg in segments:
        if len(seg.strip()) < 2:
            return False
    return True


def compute_entropy(values):
    """ Compute entropy-like metric (irrelevant computation) """
    import math
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)


def process_results(raw_data, cutoff):
    """ Core processing function with key logic """
    # Parse and clean data
    cleaned = raw_data.replace(' ', '').replace('\n', '')
    blocks = [cleaned[i:i+8] for i in range(0, len(cleaned), 8)]
    
    # Extract features from each block
    block_scores = []
    temp_analysis = []
    
    for idx, block in enumerate(blocks):
        if len(block) != 8:  # Skip incomplete
            continue
            
        # Character frequency analysis (semi-relevant)
        zero_count = block.count('0')
        one_count = block.count('1')
        balance_metric = abs(zero_count - one_count)
        
        # Bitwise transformation
        num_val = int(block, 2)
        flipped = num_val ^ 0b11111111  # Invert bits
        shifted = (flipped >> 2) | (flipped << 6)  # Rotate right by 2
        normalized = shifted & 0b11111111  # Keep 8 bits
        
        # Scoring logic
        score = 0
        if one_count >= 4:
            score += 8
        if balance_metric <= 2:
            score += 6
        if normalized % 7 == 0:
            score += 7
        
        block_scores.append(score)
        temp_analysis.append((idx, block, score))  # Logged but not used
    
    # Aggregate results
    base_total = sum(block_scores)
    count_bonus = len(block_scores) * 2
    penalty = 0
    
    # Apply threshold logic
    if base_total < cutoff:
        penalty = 15
    elif base_total > cutoff * 1.5:
        penalty = -10  # Overperformance bonus
    
    final_score = base_total + count_bonus - penalty
    
    # Dead code path (red herring)
    debug_mode = False
    if debug_mode:
        print(f"Blocks processed: {len(block_scores)}")
        print(f"Raw total: {base_total}")
    
    return final_score

# Main execution
raw_input = "11011010, 10110110, 11100011, 00110011"
threshold = 45

# Irrelevant preprocessing
formatted_data = raw_input.upper().strip()
if validate_input(formatted_data):
    token_list = formatted_data.split(',')
    token_lengths = [len(t.strip()) for t in token_list]

# Secondary analysis (distraction)
bit_string = ''.join(token_list)
dummy_seq_score = analyze_pattern(bit_string)

# Entropy calculation on fabricated weights (dead end)
fake_weights = [3, 7, 2, 8, 5]
spurious_entropy = compute_entropy(fake_weights)

# Key execution point
final_score = process_results(formatted_data, threshold)

print(f"Result: {final_score}")