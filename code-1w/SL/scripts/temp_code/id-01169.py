def process_entry(entry):
    # Extract and clean data
    raw_value = entry.strip().lower()
    if not raw_value:
        return 0

    # Misleading transformation chain
    temp_a = len(raw_value) * 2
    temp_b = raw_value.count('a') + raw_value.count('e') + raw_value.count('i')
    temp_c = temp_a - temp_b * 3  # Semi-relevant adjustment

    # Core logic: count vowels and apply weight
    vowel_count = sum(1 for c in raw_value if c in 'aeiou')
    consonant_count = sum(1 for c in raw_value if c.isalpha() and c not in 'aeiou')
    score = vowel_count * 5 - consonant_count * 2

    # Dead code path (never taken due to prior check)
    if raw_value is None:
        return -999

    return max(score, 0)


def calculate_final_score(data_list):
    total = 0
    bonus_applied = False
    entry_weights = []

    for i, entry in enumerate(data_list):
        # Irrelevant weighting preparation
        weight = (i + 1) / len(data_list) if len(data_list) > 0 else 0
        entry_weights.append(weight)

        # Actual processing
        entry_score = process_entry(entry)
        total += entry_score

        # Bonus logic with condition
        if entry_score > 10 and not bonus_applied:
            total += 5
            bonus_applied = True  # Only apply once

    # Distractor computation: normalized average (not used)
    if entry_weights:
        weighted_avg = sum(total * w for w in entry_weights) / len(entry_weights)
        rounded_avg = round(weighted_avg, 3)

    # Final adjustment based on length patterns
    long_entries = [e for e in data_list if len(e.strip()) > 6]
    if len(long_entries) >= 2:
        total += 3

    return total

# Main execution
raw_data = ["Hello World", "AI Benchmark", "Code Reasoning Test", "", "Python"]
intermediate_result = [x.upper() for x in raw_data]  # Irrelevant transformation
stats_summary = {"count": len(raw_data), "total_chars": sum(len(x) for x in raw_data)}  # Unused tracking

final_score = calculate_final_score(raw_data)
print(f"Result: {final_score}")