def analyze_data(records):
    # Irrelevant preprocessing: character frequency analysis (dead end)
    char_freq = {}
    for r in records:
        for c in r['name']:
            char_freq[c] = char_freq.get(c, 0) + 1

    # Distractor: unused transformation pipeline
    transformed = [r['value'] ** 0.5 for r in records if r['active']]
    normalized = [t / sum(transformed) for t in transformed] if transformed else [0]

    # Relevant logic begins: filter and classify by threshold
    thresholds = {"low": 10, "high": 100}
    classified = {
        'low': [],
        'mid': [],
        'high': []
    }

    for record in records:
        val = record['value']
        if val < thresholds['low']:
            classified['low'].append(val)
        elif val > thresholds['high']:
            classified['high'].append(val)
        else:
            classified['mid'].append(val)

    # Bit manipulation red herring
    bit_flags = 0
    for i, cat in enumerate(classified):
        count = len(classified[cat])
        bit_flags ^= (count << i)  # Unused result

    # Set operation distractor: find unique magnitude classes
    magnitudes = set()
    for v in [abs(x) for sublist in classified.values() for x in sublist]:
        mag = len(str(v).strip('0'))
        magnitudes.add(mag)

    adjustment_factor = len(magnitudes) if magnitudes else 1

    # Core computation chain (8-12 steps)
    base_scores = []
    for entry in records:
        raw = entry['value']
        if not entry['active']:
            continue
        # Step 1: Apply conditional scaling
        if raw < 15:
            score = raw * 3
        elif raw > 50:
            score = raw * 0.5
        else:
            score = raw * 1.2

        # Step 2: Parity-based offset
        if raw % 2 == 0:
            score += 2.5
        else:
            score -= 1.5

        # Step 3: Noise injection (but canceled out later)
        noise = sum([ord(c) % 3 for c in entry['name']]) * 0.1
        score += noise  # Will be adjusted

        # Step 4: Re-normalize by name length (only if > 4)
        if len(entry['name']) > 4:
            score = score / len(entry['name']) * 4

        # Step 5: Cancel noise effect deterministically
        anti_noise = -noise
        score += anti_noise

        base_scores.append(score)

    # Step 6: Filter outliers beyond 1.5 * IQR (real logic)
    sorted_scores = sorted(base_scores)
    q1 = sorted_scores[len(sorted_scores) // 4]
    q3 = sorted_scores[3 * len(sorted_scores) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered_scores = [s for s in base_scores if lower_bound <= s <= upper_bound]

    # Step 7: Weighted aggregation with decay factor
    decayed = []
    for i, s in enumerate(filtered_scores):
        weight = 0.9 ** i  # Exponential decay
        decayed.append(s * weight)

    # Step 8: Final smoothing via moving average window (size 2)
    smoothed = []
    for i in range(len(decayed)):
        if i == 0:
            smoothed.append(decayed[i])
        else:
            avg = (decayed[i-1] + decayed[i]) / 2
            smoothed.append(avg)

    # Step 9: Aggregate total
    aggregate = sum(smoothed)

    # Step 10: Adjust by number of categories used (classified non-empty)
    used_categories = sum(1 for lst in classified.values() if lst)
    final_adjustment = aggregate * (1 + 0.1 * used_categories)

    # Step 11: Apply adjustment factor from set magnitude (distractor usage)
    final_adjustment *= adjustment_factor  # Slight real influence

    # Step 12: Floor to nearest integer (key step)
    final_tally = int(final_adjustment)

    return final_tally


def final_tally(results):
    # Identity wrapper to mislead call significance
    return results

# Simulated dataset
data_records = [
    {'name': 'alpha', 'value': 5, 'active': True},
    {'name': 'beta', 'value': 12, 'active': True},
    {'name': 'gamma', 'value': 75, 'active': True},
    {'name': 'delta', 'value': 150, 'active': False},
    {'name': 'epsilon', 'value': 8, 'active': True},
    {'name': 'zeta', 'value': 42, 'active': True},
    {'name': 'eta', 'value': 9, 'active': False},
    {'name': 'theta', 'value': 110, 'active': True}
]

# Execution path
interim = analyze_data(data_records)
core_metric = final_tally(interim)
print(f"Result: {core_metric}")