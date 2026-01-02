def process_entry(entry):
    # Extract and clean name
    name = entry['name'].strip().lower()
    if not name:
        return None

    # Irrelevant string transformation (distractor)
    reversed_name = name[::-1].capitalize()
    vowel_count = sum(1 for c in name if c in 'aeiou')

    # Scoring logic based on conditions
    base_score = len(name)
    if 'x' in name or 'z' in name:
        base_score += 5
    elif len(name) > 6:
        base_score += 2

    # Bonus for short names with many vowels
    if len(name) <= 5 and vowel_count >= 2:
        base_score += 3

    # Irrelevant computation: counts syllables (not used)
    syllable_estimate = 0
    prev_was_vowel = False
    for c in name:
        if c in 'aeiou':
            if not prev_was_vowel:
                syllable_estimate += 1
            prev_was_vowel = True
        else:
            prev_was_vowel = False

    # Return processed data including unused fields
    return {
        'original': entry['name'],
        'processed_name': name,
        'base_score': base_score,
        'vowel_count': vowel_count,  # Not used later
        'syllable_estimate': syllable_estimate  # Dead code path
    }


def calculate_final_score(dataset):
    total = 0
    count = 0
    max_temp_score = 0

    for item in dataset:
        processed = process_entry(item)
        if processed is None:
            continue

        temp_score = processed['base_score']

        # Track maximum temp score (unused)
        if temp_score > max_temp_score:
            max_temp_score = temp_score

        # Accumulate only total and count
        total += temp_score
        count += 1

        # Fake filtering condition that doesn't change flow
        if temp_score < 3:
            pass  # Dead code branch

    # Final scoring uses average adjusted by count
    if count == 0:
        return 0

    average = total / count

    # Apply adjustment based on data size
    adjustment_factor = 1.0
    if count > 5:
        adjustment_factor = 1.1
    elif count > 3:
        adjustment_factor = 1.05

    # Unused metric: harmonic mean calculation (distraction)
    harmonic_mean = 0
    if count > 0:
        try:
            harmonic_mean = count / sum(1 / (p['base_score'] + 1e-5) for p in [process_entry(x) for x in dataset] if p)
        except ZeroDivisionError:
            harmonic_mean = 0

    final_score = int(round(average * adjustment_factor))
    return final_score

# Main execution
raw_data = [
    {'name': 'Xavier'},
    {'name': 'Zoe'},
    {'name': 'Anna'},
    {'name': 'Bob'},
    {'name': 'Elizabeth'},
    {'name': 'Max'},
    {'name': 'Aria'}
]

result = calculate_final_score(raw_data)
print(f"Result: {result}")