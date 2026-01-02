def analyze_data(records):
    # Irrelevant data transformation
    names = [r['name'].upper() for r in records if len(r['name']) > 3]
    ages = [r['age'] for r in records if r['age'] >= 18]
    avg_age = sum(ages) / len(ages) if ages else 0

    # Distractor: complex but unused string processing
    name_parts = set()
    for name in names:
        parts = name.split(' ')
        for p in parts:
            if p.startswith('A'):
                name_parts.add(p)
    reversed_names = [n[::-1] for n in names]

    # Real computation path begins
    values = [r['score'] for r in records]
    threshold = sum(values) / len(values)
    high_performers = [v for v in values if v > threshold]
    low_performers = [v for v in values if v <= threshold]

    adjustment = len(high_performers) - len(low_performers)

    # Bit manipulation red herring
    masked_adjustment = adjustment ^ 0xFF
    shifted = (masked_adjustment << 2) >> 1

    # Another decoy function definition (never called)
    def calculate_robustness(data):
        return sum([abs(x - min(data)) for x in data])

    # Actual relevant logic buried here
    metrics = []
    for i, v in enumerate(values):
        if i % 2 == 0:
            metrics.append(v * 0.9 + adjustment)
        else:
            metrics.append(v * 1.1 - abs(adjustment) / 2)

    baseline = [75, 80, 78, 82]

    def evaluate_performance(met, base):
        # Use of set operations (required feature)
        met_set = set([round(x) for x in met])
        base_set = set(base)
        overlap = met_set & base_set  # intersection
        bonus = len(overlap) * 2.5

        # String method distractor
        flag_str = "performance_check_active"
        tokens = flag_str.split('_')
        valid_tokens = [t for t in tokens if t.isalpha() and len(t) > 1]
        token_score = sum(len(t) for t in valid_tokens)

        # Core calculation
        raw_score = sum(met) / len(met)
        base_avg = sum(base) / len(base)
        diff = raw_score - base_avg
        penalty = 0
        if diff < 0:
            penalty = 10

        # Final composition
        result = raw_score + bonus - penalty
        return round(result, 4)

    # Execution point of interest
    final_score = evaluate_performance(metrics, baseline)

    # Dead code path
    if final_score < 0:
        fallback = 0
        for c in str(final_score):
            if c.isdigit():
                fallback += int(c)
        final_score = fallback

    print(f"Result: {final_score}")