def analyze_pattern(seq, threshold):
    """ Analyzes bit patterns but contains red herrings """
    ones_count = sum(1 for b in seq if b == 1)
    parity = ones_count % 2
    shifted = [(b << 1) % 2 for b in seq]  # Distractor: unused later
    score = 0
    for i, bit in enumerate(seq):
        if i % 2 == 0 and bit == 1:
            score += 3
    return score if score > threshold else threshold + 1


def evaluate_series(data):
    """ Processes data with multiple distractions """
    temp_results = []
    decoy_sum = 0
    for x in data:
        decoy_sum += x * x  # Dead path: not used in final logic
        if x % 2 == 0:
            temp_results.append(x // 2)
    # Irrelevant transformation
    transformed = [t ** 0.5 for t in temp_results if t > 0]
    return len(temp_results)


def compute_entropy(values):
    """ Fake entropy calculation - misleading name """
    total = sum(values)
    if total == 0:
        return 0
    weighted = [v / total for v in values]  # Not actually used
    return total % 17


def extract_features(record):
    """ Extracts features using set operations and conditional logic """
    feature_set_a = {x for x in record if x % 3 == 0}
    feature_set_b = {x for x in record if x % 5 == 0}
    common = feature_set_a & feature_set_b  # Useful intersection
    unique_to_a = feature_set_a - feature_set_b
    
    # Decoy metrics
    dummy_metric_1 = len(feature_set_a) * 2
    dummy_metric_2 = sum(unique_to_a) ^ 1234  # Bitwise XOR red herring
    
    base_score = len(common) * 5
    bonus = 0
    for val in common:
        if val > 10:
            bonus += val // 10
    return base_score + bonus


def calculate_aggregate(entries, config):
    """ Core function that combines multiple results """
    # Real computation begins
    raw_values = [e['value'] for e in entries]
    
    # Conditional expression with distractors
    scaling_factor = 2.5 if sum(raw_values) > config['limit'] else 1.8
    
    # Tuple unpacking with extra variables
    (a, b, c) = (config['alpha'], config['beta'], config['gamma'])
    
    # Enumerate and zip usage (required)
    indexed = list(enumerate(raw_values))
    paired = list(zip([e['flag'] for e in entries], raw_values))
    
    primary_contributions = 0
    secondary_adjustment = 0
    
    for i, val in indexed:
        flag_val = paired[i][0]
        if flag_val:
            if i % 3 == 0:
                primary_contributions += val * a
            elif i % 3 == 1:
                secondary_adjustment += val * b
        else:
            secondary_adjustment -= val * c

    # Set operation to filter significant indices
    sig_indices = {i for i, v in indexed if v > 50}
    penalty = len(sig_indices) * 4

    # Real answer depends on this chain
    feature_input = [e['value'] for e in entries if e['track']]
    features = extract_features(feature_input)

    # Final computation — only this matters
    stage_one = primary_contributions - secondary_adjustment
    stage_two = stage_one * scaling_factor
    final_score = int(stage_two + features - penalty)

    # Several irrelevant variables below
    debug_info = {
        'raw': raw_values,
        'scaled': stage_two,
        'features_raw': feature_input,
        'decoy': compute_entropy(raw_values),
        'unused_analysis': analyze_pattern([1,0,1,1,0], 2),
        'series_eval': evaluate_series(raw_values)
    }
    
    return final_score  # This is what we care about

# Main execution
if __name__ == '__main__':
    data_entries = [
        {'value': 60, 'flag': True, 'track': True},
        {'value': 45, 'flag': False, 'track': True},
        {'value': 72, 'flag': True, 'track': False},
        {'value': 38, 'flag': True, 'track': True},
        {'value': 91, 'flag': False, 'track': False},
        {'value': 55, 'flag': True, 'track': True}
    ]
    
    settings = {
        'limit': 200,
        'alpha': 3,
        'beta': 2,
        'gamma': 4
    }
    
    # Trigger main computation
    final_score = calculate_aggregate(data_entries, settings)
    
    # Print result as required
    print(f"Target result: {final_score}")