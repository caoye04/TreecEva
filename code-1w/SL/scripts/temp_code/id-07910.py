def process_metrics(entries, importance):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant transformation (distractor)
    transform = lambda x: (x ** 2 + 1) * 0.5
    transformed = [transform(v['value']) for v in entries]

    # Real computation begins
    for i, entry in enumerate(entries):
        weight = importance.get(entry['type'], 1.0)
        contribution = entry['value'] * weight

        # Conditional state tracking (semi-relevant)
        if contribution > 10:
            bonus += 2
            flag_state = True
        else:
            flag_state = False

        # Bitwise validation check (mildly relevant)
        validity_key = entry['flags'] & 0b1111
        if validity_key ^ 0b1010 == 0:
            penalty -= 1

        base += contribution

        # Dead code path (irrelevant)
        if i % 100 == 0:
            temp_result.append(-999)  # Never reached due to small input size

    # Dictionary-based adjustment map (relevant)
    adjustments = {'A': 1.2, 'B': 0.9, 'C': 1.0}
    category_boost = sum(adjustments.get(e['type'], 1.0) for e in entries if e['value'] > 5)

    # Final score with controlled interference
    intermediate = base + bonus + penalty
    final_score = int(intermediate * 0.8 + category_boost)

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data = [
    {'value': 7, 'type': 'A', 'flags': 0b1010},
    {'value': 6, 'type': 'B', 'flags': 0b1100},
    {'value': 12, 'type': 'A', 'flags': 0b1010},
    {'value': 4, 'type': 'C', 'flags': 0b0011}
]

weights = {'A': 1.5, 'B': 0.8, 'C': 1.0}

# Trigger execution
final_score = process_metrics(data, weights)