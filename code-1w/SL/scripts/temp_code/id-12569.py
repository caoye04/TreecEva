import itertools

def analyze_pattern(seq):
    # Irrelevant helper: analyzes string patterns (distractor)
    counts = {}
    for c in seq:
        counts[c] = counts.get(c, 0) + 1
    return {k: v for k, v in counts.items() if v > 1}

def validate_checksum(arr):
    # Dead-end function: computes XOR checksum but unused
    checksum = 0
    for x in arr:
        checksum ^= x * 3
    return checksum % 7 == 0

def transform_key(val, shift):
    # Misleading transformation used only once
    return ((val << 2) ^ shift) & 0xFF

def filter_outliers(data_list):
    # Real but overcomplicated filtering with red herrings
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    lower, upper = mean_val - 1.5 * std_dev, mean_val + 1.5 * std_dev
    
    filtered = [x for x in data_list if lower <= x <= upper]
    outlier_flags = [x not in filtered for x in data_list]  # Unused
    return filtered

def compute_entropy(values):
    # Decoy scientific computation (not actually used in final path)
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    from math import log
    return -sum(p * log(p) for p in probs)

def process_metrics(raw_data, config):
    # Core logic buried in noise
    temp_a = [x * config['gain'] for x in raw_data]
    temp_b = [y + config['offset'] for y in temp_a]
    
    # Bit manipulation red herring
    magic_shift = transform_key(len(temp_b), config['offset'])
    shifted_vals = [z ^ magic_shift for z in temp_b]  # Not used later

    # Real processing starts here
    abs_vals = [abs(v) for v in temp_b]
    capped_vals = [min(v, 100) for v in abs_vals]
    
    # Weighted sum with tuple unpacking distraction
    weights_tuple = (config['w1'], config['w2'], config['w3'])
    w1, w2, w3 = weights_tuple
    
    part_x = sum(capped_vals[::3]) * w1
    part_y = sum(capped_vals[1::3]) * w2
    part_z = sum(capped_vals[2::3]) * w3

    # Critical combination
    aggregate = part_x + part_y + part_z
    
    # String-based distractor: uses itertools and string methods
    tag = "metric_v2"
    repeated_tag = ''.join(itertools.chain(*zip(tag, tag)))  # e.g., mmeeattriicc__vv22
    tag_sum = sum(ord(c) for c in repeated_tag if c.isdigit())  # Only digits contribute
    
    # Final score computed here — this is the answer
    final_score = int(aggregate - tag_sum)  # deterministic
    
    # Dead code paths below
    if final_score < 0:
        backup_weights = sorted(config.values())
        final_score += sum(backup_weights)  # Never reached in this case
    
    return final_score

# Main execution with decoys
if __name__ == "__main__":
    # Input setup
    data = [8, -15, 22, 34, -50, 61, 13, -7, 44, 29]
    weights = {'gain': 2.5, 'offset': 10, 'w1': 1, 'w2': 2, 'w3': 3}

    # Irrelevant preprocessing
    checksum_valid = validate_checksum([d % 10 for d in data])
    pattern_report = analyze_pattern("aabbccddeeff")

    # Real pipeline
    cleaned = filter_outliers(data)
    entropy = compute_entropy([abs(x) for x in data])

    # Key execution point
    final_score = process_metrics(cleaned, weights)

    # Output
    print(f"Result: {final_score}")