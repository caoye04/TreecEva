def analyze_signal(sequence, threshold=0.7):
    """ Misleading function – never called but distracts from main logic """
    count = 0
    for s in sequence:
        if s > threshold:
            count += 1
    return count / len(sequence)


def transform_node(node, shift=3):
    """ Another decoy transformation – not used in actual flow """
    return (node << 2) ^ shift


def process_metrics(data_stream):
    temp_cache = []
    running_total = 0
    overflow_flag = False
    
    for idx, val in enumerate(data_stream):
        if idx % 4 == 0 and val > 50:
            running_total += val // 4
        elif idx % 3 == 1:
            running_total -= (val % 7) * 2
        else:
            running_total += (val + idx) & 15
            
        temp_cache.append(running_total)
    
    # Dead code path – condition never met due to above logic
    if overflow_flag and len(temp_cache) > 200:
        running_total = -9999
        
    return temp_cache


def evaluate_stages(stage_codes):
    result = 0
    for code in stage_codes:
        if code.startswith('A'):
            result += 10
        elif code.startswith('B'):
            result += 5
        else:
            result -= 2
    return result


def filter_candidates(candidates, blacklist={101, 205, 307}):
    """ Irrelevant filtering – included to mislead about data importance """
    return [c for c in candidates if c not in blacklist]


def compute_entropy(values):
    """ Unused scientific computation – adds false depth """
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)


def harvest_results(data):
    accumulator = 0
    scaling_factor = 1.75
    
    for i, x in enumerate(zip(data[::2], data[1::2])):
        even_val, odd_val = x
        
        # Key logic: conditional expression with bitwise mix
        adjustment = (even_val & 7) if (i + 1) % 3 == 0 else (odd_val ^ 5)
        
        if i % 4 == 0:
            accumulator += even_val * 1.1
        elif i % 4 == 2:
            accumulator -= odd_val * 0.3
        else:
            accumulator += adjustment * scaling_factor
        
        # Early termination red herring – never triggers
        if accumulator < -1000:
            return -1
            
    return int(accumulator + 0.5)  # Round to nearest integer

# Main execution block
if __name__ == '__main__':
    raw_input = [88, 105, 72, 93, 64, 110, 58, 97, 76, 102, 60, 89]
    
    # Distractor variables – unused in final calculation
    signal_strength = [x / 128.0 for x in raw_input if x > 70]
    node_map = {i: transform_node(x, 5) for i, x in enumerate(raw_input)}
    stage_labels = ['A1', 'B2', 'C3', 'A4', 'B5', 'D6']
    candidate_ids = [101, 102, 103, 205, 206, 307, 308]
    
    # Real processing begins here
    processed_data = process_metrics(raw_input)
    
    # More distractions
    metric_entropy = compute_entropy([len(processed_data), sum(processed_data) % 100])
    valid_candidates = filter_candidates(candidate_ids)
    stage_score = evaluate_stages(stage_labels)
    
    # Critical assignment point
    final_yield = harvest_results(processed_data)
    
    print(f"Result: {final_yield}")