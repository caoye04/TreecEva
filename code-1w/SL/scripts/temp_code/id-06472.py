import math

def analyze_signal(strength, threshold=5.0):
    if strength < threshold:
        return 'weak'
    elif strength < threshold * 2:
        return 'moderate'
    else:
        return 'strong'


def transform_value(x):
    if x <= 0:
        return 0
    return int(math.log(x) * 10)


def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum += (i + 1) * val
    return checksum % 17


def decode_sequence(seq):
    result = []
    for s in seq:
        if s.isdigit():
            result.append(int(s) ** 2)
    return result


def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)


def filter_outliers(data, factor=1.5):
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]


def compute_hash_chain(seed_val, length):
    hash_seq = [seed_val]
    for i in range(1, length):
        new_val = (hash_seq[-1] * 7 + 3) % 101
        hash_seq.append(new_val)
    return hash_seq


def adjust_weights(weights, mode='linear'):
    if mode == 'linear':
        scale = 1.0 / sum(weights)
        return [round(w * scale, 3) for w in weights]
    elif mode == 'softmax':
        exp_vals = [math.exp(w) for w in weights]
        total = sum(exp_vals)
        return [e / total for e in exp_vals]
    return weights


def evaluate_pattern(pattern):
    score = 0
    for i, p in enumerate(pattern):
        if p == 'A':
            score += i * 2
        elif p == 'B':
            score -= i
        else:
            score += 1
    return score


def process_metrics(data, config):
    # Irrelevant pre-processing (distractor)
    temp_buffer = [transform_value(x) for x in data if x > 0]
    signal_status = analyze_signal(sum(data) / len(data))
    
    # Decoy operation: decoding unrelated sequence
    raw_seq = "3a1b9c2"
    decoded = decode_sequence(raw_seq)
    
    # Another red herring: calculating entropy of transformed data
    entropy = calculate_entropy([x % 10 + 1 for x in data])
    
    # Filter outliers but use only size as distraction
    filtered = filter_outliers(data)
    outlier_count = len(data) - len(filtered)  # Unused later
    
    # Hash chain used to generate decoy weights
    hash_chain = compute_hash_chain(5, len(data))
    fake_weights = adjust_weights(hash_chain[:len(data)], mode='linear')
    
    # Real logic begins here — actual path to answer
    base_score = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            base_score += val * config.get('multiplier', 3)
        else:
            base_score -= val // 2
    
    # Conditional expression used as required
    penalty = 10 if len([x for x in data if x < 0]) > 0 else 0
    
    intermediate = base_score - penalty
    
    # Apply pattern-based adjustment using config
    pattern = config.get('pattern', 'ACBA')
    pattern_score = evaluate_pattern(pattern)
    
    # Final transformation
    final_score = intermediate + pattern_score
    
    # Additional irrelevant computation (misleading)
    checksum = validate_checksum(data)
    entropy_contribution = int(entropy * 100)
    final_score += entropy_contribution - checksum  # Net zero effect due to design
    
    return final_score

# Main execution
if __name__ == '__main__':
    data = [12, -4, 7, 15, 3, 9]
    config = {
        'multiplier': 4,
        'pattern': 'ABBA'
    }
    final_score = process_metrics(data, config)
    print(f"Target result: {final_score}")