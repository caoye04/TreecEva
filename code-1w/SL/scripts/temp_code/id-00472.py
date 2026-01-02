def analyze_sequence(data):
    # Irrelevant transformation: character frequency counting
    freq = {}
    for char in ''.join(map(str, data)):
        freq[char] = freq.get(char, 0) + 1
    
    # Distractor: unused statistical computation
    mean_val = sum(data) / len(data) if data else 0
    variance = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    threshold = mean_val + (variance ** 0.5)

    # Red herring function defined but not used
    def decrypt_key(seq):
        return [seq[i] ^ i for i in range(len(seq))]

    # Another decoy: string-based misdirection
    status_flags = ['PASS', 'FAIL', 'WARN']
    result_label = status_flags[len(data) % 3]

    # Real logic begins: filter and transform based on conditions
    processed = []
    for i, val in enumerate(data):
        if val > threshold:  # dynamic threshold based on mean+std
            processed.append(val * 2)
        elif val < mean_val:
            processed.append(val // 2)
        else:
            processed.append(val)

    # Use of enumerate and zip — required language feature
    indexed = list(enumerate(processed))
    shifts = [i % 5 for i in range(len(processed))]
    shifted_data = [a + b for a, b in zip(processed, shifts)]

    # Apply masking using set operations — required feature
    unique_shifts = set(shifts)
    masked_values = [v for i, v in enumerate(shifted_data) if (i % 5) not in unique_shifts]

    # Simulated normalization (not actually affecting final path)
    max_val = max(masked_values) if masked_values else 1
    normalized = [round(v / max_val, 4) for v in masked_values]

    # Core calculation hidden among distractions
    base_total = sum(v for v in processed if v % 2 == 0)
    penalty = len([v for v in data if v < 0]) * 10
    bonus = len(set(data))  # diversity bonus

    # Intermediate decoy variable with misleading name
    apparent_score = base_total - penalty + (bonus * 5)

    # Dead code path — never executed due to condition
    if False and apparent_score > 1000:
        correction_factor = 0.9
        apparent_score = int(apparent_score * correction_factor)

    return base_total, bonus, penalty  # Note: apparent_score not returned


def compute_weights(config):
    # Unrelated weight schema
    schema = {'A': 1.1, 'B': 2.2, 'C': 3.3}
    weights = []
    for k, v in config.items():
        if k in schema:
            weights.append(schema[k] * v)
    return weights

def evaluate_performance(metrics, results):
    # metrics: weights for different components
    # results: tuple from analyze_sequence
    total_raw, diversity_bonus, negative_penalty = results
    
    # Dictionary operation — required feature
    score_breakdown = {
        'base': total_raw,
        'bonus': diversity_bonus * metrics[0],
        'penalty_adj': abs(negative_penalty * metrics[1])
    }
    
    # More red herrings
    audit_log = []
    for key, value in score_breakdown.items():
        audit_log.append(f'{key}:{value}')
    
    # Final distraction: conditional that doesn't affect output
    if len(audit_log) > 2 and 'base' in score_breakdown:
        temp_adjust = score_breakdown['base'] % 7
        # Not used anywhere
        dummy_flag = temp_adjust > 3

    # Actual final score computation
    raw_contribution = score_breakdown['base']
    bonus_contribution = score_breakdown['bonus']
    penalty_contribution = score_breakdown['penalty_adj']

    final_value = raw_contribution + bonus_contribution - penalty_contribution
    return int(final_value)  # deterministic integer result

# Main execution flow
if __name__ == '__main__':
    # Input data with mixed properties
    input_sequence = [12, -5, 18, 24, 9, 33, -1, 15]
    
    # Irrelevant configuration map (partially used)
    config_params = {'A': 3, 'B': 2, 'X': 99}  # X is ignored
    metric_weights = compute_weights(config_params)
    
    # Decoy variables
    temp_result = sum(x ** 2 for x in input_sequence if x > 0)
    debug_state = {"stage": "pre-eval", "size": len(input_sequence)}
    
    # Key computation chain
    raw_results = analyze_sequence(input_sequence)
    final_score = evaluate_performance(metric_weights, raw_results)
    
    # Output as required
    print(f"Result: {final_score}")