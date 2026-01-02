from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(2, len(sequence) + 1):
        for combo in combinations(sequence, i):
            if sum(combo) % 3 == 0:
                count += 1
    return count

def validate_entry(entry):
    return len(entry['name']) > 3 and entry['active']

def compute_weighted_sum(values, weights):
    # Irrelevant computation - distractor
    temp_result = 0
    for v, w in zip(values, weights):
        temp_result += v * w ** 0.5
    return temp_result

def calculate_final_score(data, thresholds):
    raw_scores = []n    extra_analysis = set()
    total_valid = 0
    debug_flags = []

    for item in data:
        if not validate_entry(item):
            continue
        
        base_value = item['value']
        offset = len(item['tags'])
        adjusted = base_value + offset
        
        # Real logic path
        if adjusted > thresholds['high']:
            category = 'A'
        elif adjusted > thresholds['medium']:
            category = 'B'
        else:
            category = 'C'

        # Semi-relevant: used in filtering later
        tag_pairs = list(combinations(item['tags'], 2))
        pair_count = len(tag_pairs)
        extra_analysis.update(tag_pairs)
        
        # Only category A contributes to final score
        if category == 'A':
            raw_scores.append(adjusted)
            total_valid += 1
        else:
            debug_flags.append(f"skipped_{item['name']}")

    # Distractor: complex but unused structure
    ignored_summary = {
        'pattern_count': analyze_patterns([len(t) for t in extra_analysis]),
        'flags': debug_flags,
        'computed': compute_weighted_sum(raw_scores, [1]*len(raw_scores))
    }

    # Actual final computation
    if raw_scores:
        average_raw = sum(raw_scores) / len(raw_scores)
        penalty = 0.1 * len(debug_flags)
        final_score = int(average_raw - penalty)
    else:
        final_score = 0

    return final_score

# Main execution
data = [
    {'name': 'alpha', 'value': 45, 'tags': ['x', 'y'], 'active': True},
    {'name': 'beta', 'value': 38, 'tags': ['z'], 'active': True},
    {'name': 'g', 'value': 52, 'tags': ['x', 'z', 'w'], 'active': True},
    {'name': 'delta', 'value': 29, 'tags': ['y'], 'active': False},
    {'name': 'epsilon', 'value': 48, 'tags': ['a', 'b'], 'active': True}
]

time_stamps = [12345, 12346, 12347]  # Unused metadata
thresholds = {'low': 30, 'medium': 40, 'high': 50}

intermediate_values = [d['value'] for d in data if d['active']]  # Not directly used

final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")