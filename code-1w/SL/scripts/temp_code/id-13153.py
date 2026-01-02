from collections import defaultdict

def analyze_data(entries):
    counts = defaultdict(int)
    totals = 0
    temp_sum = 0  # distractor
    redundant_flag = False  # dead code

    for entry in entries:
        category = entry['type']
        value = entry['value']
        counts[category] += value
        totals += value
        if value > 100:
            temp_sum += value * 0.1

    adjusted_totals = 0
    for k, v in counts.items():
        if v > 50:
            adjusted_totals += v * 1.1
        else:
            adjusted_totals += v

    return adjusted_totals

def validate_inputs(data, schema):
    """Irrelevant validation function - not used in final result."""
    errors = []
    for i, item in enumerate(data):
        for field in schema:
            if field not in item:
                errors.append(f"Missing {field} at index {i}")
    return len(errors) == 0

def calculate_final_score(raw_data, importance_weights):
    base_scores = []
    cumulative = 0
    tracker = {}  # semi-relevant tracking

    for idx, (val, weight) in enumerate(zip(raw_data, importance_weights)):
        weighted_val = val * weight
        base_scores.append(weighted_val)
        cumulative += weighted_val
        tracker[f'step_{idx}'] = cumulative  # tracking but not critical

    avg_base = sum(base_scores) / len(base_scores) if base_scores else 0

    # Complex conditional with red herring logic
    bonus = 0
    threshold_met = False
    for x in base_scores:
        if x > 25:
            bonus += 5
            threshold_met = True
        if threshold_met and x < 10:  # never reached due to logic flow
            bonus -= 2

    # Real computation path
    adjustment = 0
    for ch in "analysis":  # string method usage
        if ch in "aeiou":
            adjustment += 1

    final_score = int(cumulative + bonus + adjustment)
    return final_score

# Main execution
if __name__ == "__main__":
    data = [
        {'type': 'A', 'value': 30},
        {'type': 'B', 'value': 45},
        {'type': 'A', 'value': 25},
        {'type': 'C', 'value': 60}
    ]

    # Unused but distracting variables
    processed_stats = analyze_data(data)
    schema = ['type', 'value', 'timestamp']
    is_valid = validate_inputs(data, schema)

    raw_values = [12, 18, 22, 31]
    weights = [1.5, 0.8, 1.2, 1.0]

    intermediate_total = sum([a*b for a,b in zip(raw_values, weights)])
    scaling_factor = 1.0  # unused in final logic

    final_score = calculate_final_score(raw_values, weights)
    print(f"Result: {final_score}")