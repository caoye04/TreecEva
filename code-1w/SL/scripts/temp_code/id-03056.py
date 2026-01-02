def calculate_rating(entries, factors):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant pre-processing (distractor)
    offset = len(entries) % 3
    dummy_accum = sum([x ** 0.5 for x in factors if x > 0])  # Unused computation

    for i, (val, weight) in enumerate(zip(entries, factors)):
        adjusted = val * weight
        base += adjusted

        # Conditional bonus logic (partially relevant)
        if i % 2 == 0 and adjusted > 10:
            bonus += 2
        elif val > 15:
            bonus += 1

        # Red herring: tracking values not used in final score
        temp_result.append((i, adjusted, val ** 2))

    # Unnecessary intermediate transformation
    mapped_vals = list(map(lambda x: (x[0] + 1) * x[1], temp_result))
    ignored_total = sum(mapped_vals) / (len(mapped_vals) + 1) if mapped_vals else 0

    # Real adjustment: modular correction based on total base
    mod_correction = (int(base) % 7) if base > 0 else 0

    # Final score calculation – only `base`, `bonus`, and `mod_correction` matter
    final_rating = base + bonus + mod_correction

    return final_rating


# Main execution
assessments = [12, 18, 9, 21, 14]
weights = [1.5, 0.8, 2.0, 1.2, 1.0]

# Dead code path (distractor)
if len(assessments) > 10:
    weights.extend([0.5] * (len(assessments) - 10))

intermediate_sum = sum([x * y for x, y in zip(assessments, weights)])  # Semi-relevant but not final
normalization_factor = intermediate_sum / (sum(assessments) + 0.1)  # Unused

# Key statement
final_score = calculate_rating(assessments, weights)

print(f"Result: {final_score}")