def analyze_metrics(data, threshold=5.0):
    # Irrelevant helper function – dead code path
    cumulative = 0
    for x in data:
        if x > threshold:
            cumulative += x ** 0.5
    return cumulative * 0.1


def validate_entry(record):
    # Misleading validation logic – not actually used in critical path
    if not record.get('active'):
        return False
    if record['score'] < 0 or record['score'] > 100:
        return False
    return True

# Decoy data structures
test_results = [78, 85, 92, 45, 67]
dummy_weights = [0.1, 0.2, 0.3, 0.4]

# Real input data
assessment_log = [
    {'id': 'A1', 'score': 88, 'level': 'senior', 'active': True},
    {'id': 'B2', 'score': 76, 'level': 'mid', 'active': True},
    {'id': 'C3', 'score': 95, 'level': 'senior', 'active': False},
    {'id': 'D4', 'score': 82, 'level': 'mid', 'active': True}
]

# Unused accumulator – red herring
aggregate = sum([entry['score'] for entry in assessment_log if entry['level'] == 'junior'])

# Complex distractor: nested counting with irrelevant conditionals
counted = 0
for entry in assessment_log:
    if entry['score'] >= 75:
        if entry['level'] == 'senior':
            counted += 2
        else:
            counted += 1

# Hidden normalization factor computed via conditional expression
normalizer = 10 if len([e for e in assessment_log if e['active']]) > 2 else 5

# Core logic disguised among distractions
def evaluate_performance(log):
    base_total = 0
    bonus = 0
    active_count = 0
    
    for item in log:
        # Only active users contribute to base total
        if item['active']:
            base_total += item['score']
            active_count += 1
            # Bonus logic: senior-level active users get extra points
            bonus += 5 if item['level'] == 'senior' else 0
    
    # Conditional expression used (required feature)
    multiplier = 1.5 if active_count >= 3 else 1.0
    
    # Composite calculation combining multiple concepts
    raw_score = (base_total + bonus) * multiplier
    
    # Final adjustment using normalizer from earlier
    return int(raw_score / normalizer)

# Critical execution point
final_score = evaluate_performance(assessment_log)

# Output result as required
print(f"Target result: {final_score}")