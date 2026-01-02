def evaluate_performance(data, importance):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = []

    for i, (val, weight) in enumerate(zip(data, importance)):
        adjusted = val * weight
        base += adjusted

        # Distractor: tracking squares for no reason
        dummy_square = val ** 2
        temp_result.append(dummy_square)

    # Irrelevant list processing
    reversed_data = data[::-1]
    for j, item in enumerate(reversed_data):
        if j % 2 == 0 and item > 50:
            bonus += 2  # Misleading bonus not used
        else:
            penalty += 1  # Also unused

    # Extra distraction with string manipulation
    status_flag = "Performance_Evaluation_Complete"
    char_list = [c.lower() for c in status_flag if c.isalpha()]
    vowel_count = sum(1 for c in char_list if c in 'aeiou')

    # Actual logic happens here, independent of above distractions
    multiplier = 1.0
    if base > 100:
        multiplier = 1.2
    elif base > 80:
        multiplier = 1.1
    else:
        multiplier = 1.0

    intermediate = 0
    for x in data:
        if x >= 60:
            intermediate += x * 0.1

    final_score = int(base * multiplier + intermediate)

    # Additional red herring: tuple unpacking that does nothing
    summary_stats = (len(data), max(data), min(data))
    count, peak, floor = summary_stats

    # Final output
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics = [75, 82, 61, 93]
weights = [0.2, 0.3, 0.1, 0.4]

# Call function
final_score = evaluate_performance(metrics, weights)