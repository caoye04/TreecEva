from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for length in range(2, len(sequence) + 1):
        for subset in combinations(sequence, length):
            if sum(subset) % 3 == 0:
                count += 1
    return count

def validate_entry(record):
    # Irrelevant validation logic (distractor)
    if not record.get('active'):
        return False
    if record.get('age', 0) < 18:
        return False
    return True

def compute_entropy(values):
    # Dead function - not used in final computation
    from math import log
    total = sum(values)
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log(prob, 2)
    return entropy

def compute_final_score(data, thresholds):
    raw_values = [x['value'] for x in data if validate_entry(x)]
    
    # Linear search for threshold crossings (relevant)
    crossed = 0
    for val in raw_values:
        for t in thresholds:
            if val > t:
                crossed += 1
                break
    
    # Character counting in labels (semi-relevant distraction)
    char_count = 0
    label_lengths = []
    for item in data:
        label = item.get('label', '')
        char_count += len(label)
        label_lengths.append(len(label))
    
    # Core logic: pattern analysis on filtered values
    filtered = [v for v in raw_values if v > 50]
    pattern_strength = analyze_patterns(filtered)
    
    # Distractor variables
    avg_length = sum(label_lengths) / len(label_lengths) if label_lengths else 0
    max_value = max(raw_values) if raw_values else 0
    temp_offset = avg_length * 0.5
    
    # Final score calculation (depends only on 'crossed' and 'pattern_strength')
    base_score = crossed * 3
    bonus = pattern_strength // 10
    final_score = base_score + bonus - 7  # offset adjustment
    
    return final_score

data = [
    {'value': 65, 'label': 'A1', 'active': True, 'age': 25},
    {'value': 45, 'label': 'B22', 'active': True, 'age': 30},
    {'value': 80, 'label': 'C333', 'active': False, 'age': 20},
    {'value': 90, 'label': 'D4444', 'active': True, 'age': 45},
    {'value': 55, 'label': 'E55555', 'active': True, 'age': 17},
    {'value': 70, 'label': 'F666666', 'active': True, 'age': 35}
]

thresholds = [50, 75, 100]

# Key statement
final_score = compute_final_score(data, thresholds)
print(f"Target result: {final_score}")