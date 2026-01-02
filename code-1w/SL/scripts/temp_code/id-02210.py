def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: analyze oscillations (not used later)
    oscillations = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1] and trend[j] != 0:
            oscillations += 1

    # Actual relevant logic
    growth_streak = 0
    max_streak = 0
    for val in trend:
        if val == 1:
            growth_streak += 1
            max_streak = max(max_streak, growth_streak)
        else:
            growth_streak = 0

    return max_streak


def validate_entry(record):
    # String validation - uses string methods
    if not record.get('id', '').startswith('USR'):
        return False
    if len(record.get('tag', '')) == 0 or record.get('tag').isnumeric():
        return False
    try:
        age = int(record.get('age', -1))
    except ValueError:
        return False
    return 18 <= age <= 80


def compute_baseline(entries):
    total = 0
    valid_count = 0
    extra_weight = 0.0

    # Dictionary operations and filtering
    stats = {}
    for entry in entries:
        category = entry.get('category', 'unknown')
        if category not in stats:
            stats[category] = 0
        stats[category] += 1

    # Distractor: normalize weights (semi-relevant)
    total_entries = sum(stats.values())
    normalized = {k: v / total_entries for k, v in stats.items()}
    for k, v in normalized.items():
        if v > 0.1:
            extra_weight += 0.05

    # Core calculation
    for entry in entries:
        if validate_entry(entry):
            raw_value = entry.get('value', 0)
            adjusted = raw_value * (1 + extra_weight)
            if entry.get('flag', False):
                adjusted *= 1.2
            total += adjusted
            valid_count += 1

    return total / valid_count if valid_count > 0 else 0


def process_results(raw_data, limits):
    # Extract sequences from data
    sequences = []
    temp_seq = []
    for item in raw_data:
        if item['type'] == 'marker':
            if temp_seq:
                sequences.append(temp_seq)
                temp_seq = []
        else:
            temp_seq.append(item['value'])
    if temp_seq:
        sequences.append(temp_seq)
    
    # Analyze each sequence
    streaks = [analyze_pattern(seq) for seq in sequences]
    avg_streak = sum(streaks) / len(streaks) if streaks else 0

    # Compute baseline from auxiliary data
    aux_entries = [{'id': f'USR{i}', 'age': 20 + i, 'tag': f'tag_{i}', 'value': i*3, 'category': 'X' if i%3==0 else 'Y', 'flag': i%5==0} for i in range(1, 16)]
    base = compute_baseline(aux_entries)

    # Use modular arithmetic and integer division
    modifier = 0
    for s in streaks:
        if s % 2 == 0 and s > 0:
            modifier += s // 2
        else:
            modifier -= (-s) // 3

    # Final logic with conditional branches
    if avg_streak >= limits['streak_threshold']:
        confidence = 0.9
    elif avg_streak >= limits['streak_threshold'] * 0.7:
        confidence = 0.6
    else:
        confidence = 0.3

    intermediate_result = (base + modifier * 10) * confidence

    # Key variable assignment
    final_score = int(intermediate_result + 0.5)  # Round to nearest integer

    # Dead code path (distractor)
    if False:
        fallback = 0
        for k in range(len(str(final_score))):
            fallback += int(str(final_score)[k])
        final_score = fallback

    return final_score

# Main execution
if __name__ == '__main__':
    data = [
        {'type': 'data', 'value': 1},
        {'type': 'data', 'value': 3},
        {'type': 'data', 'value': 2},
        {'type': 'data', 'value': 5},
        {'type': 'marker', 'value': 0},
        {'type': 'data', 'value': 4},
        {'type': 'data', 'value': 6},
        {'type': 'data', 'value': 8},
        {'type': 'data', 'value': 7},
        {'type': 'marker', 'value': 0},
        {'type': 'data', 'value': 10},
        {'type': 'data', 'value': 12}
    ]
    thresholds = {
        'streak_threshold': 2
    }
    final_score = process_results(data, thresholds)
    print(f"Result: {final_score}")