from itertools import combinations

def analyze_pattern(sequence, depth):
    """ Analyze cyclic patterns in a sequence (distractor function) """
    if depth == 0:
        return 0
    cycle_sum = 0
    for i in range(len(sequence)):
        shifted = sequence[i:] + sequence[:i]
        cycle_sum += sum(a * b for a, b in zip(shifted, sequence))
    return cycle_sum // len(sequence)

def transform_value(x, mode=0):
    """ Misleading transformation with unused branches """
    if mode == 0:
        return (x ** 2 + 3 * x + 1) % 97
    elif mode == 1:
        return x ^ (x << 1) % 101
    else:
        return abs(x - 50) * 2

def validate_entry(record):
    """ Validate data entry format (partially relevant) """
    required_keys = ['id', 'score', 'active']
    return all(k in record for k in required_keys) and isinstance(record['score'], int)

def process_results(data_batch, min_threshold):
    """ Core logic: compute final score based on filtered and transformed scores """
    valid_scores = []
    temp_buffer = []  # Used for tracking intermediate states
    
    for entry in data_batch:
        if not validate_entry(entry):
            continue
        if not entry['active']:
            # Apply special decay for inactive entries (red herring)
            decayed = entry['score']
            for _ in range(2):
                decayed = (decayed * 0.95) // 1
            temp_buffer.append(int(decayed))
            continue
        
        raw_score = entry['score']
        adjusted = transform_value(raw_score, mode=0)
        normalized = (adjusted % 89) + 10  # Normalize into positive range
        
        # Additional check using modular arithmetic
        if normalized % 7 == 0:
            normalized = (normalized // 7) * 5
        
        if normalized > min_threshold:
            # Use combination logic to simulate consensus scoring (itertools usage)
            contribs = [normalized]
            for r in range(2, 4):
                combs = list(combinations([normalized] * 3, r))
                contribs.append(len(combs) * (normalized // (r * 10 + 1)))
            valid_scores.append(sum(contribs[:2]))  # Only first two used
        else:
            valid_scores.append(normalized)
    
    # Final aggregation with distraction from temp_buffer
    base_total = sum(valid_scores)
    bonus = len(temp_buffer) * 3 if sum(temp_buffer) > 100 else 0  # Rarely triggers
    penalty = analyze_pattern(valid_scores, depth=1) // 50  # Small effect, but computed
    
    final_score = (base_total + bonus - penalty) // 1
    return final_score

# Simulated dataset
assessment_data = [
    {'id': 'A7', 'score': 42, 'active': True},
    {'id': 'B9', 'score': 18, 'active': False},
    {'id': 'C3', 'score': 61, 'active': True},
    {'id': 'D5', 'score': 25, 'active': True},
    {'id': 'E1', 'score': 12, 'active': False},
    {'id': 'F4', 'score': 73, 'active': True}
]

threshold = 40
final_score = process_results(assessment_data, threshold)
print(f"Result: {final_score}")