def evaluate_performance(records, baseline):
    total = 0
    adjustments = []
    penalty_factor = 0.9
    bonus_tracker = [0] * len(records)
    cumulative_shift = 0

    for i, entry in enumerate(records):
        raw_value = sum(entry['metrics'])
        normalized = raw_value / len(entry['metrics'])

        # Distractor: tracking bonuses that may not be used
        if normalized > baseline:
            bonus_tracker[i] = (normalized - baseline) * 0.1

        # Real logic path
        if i % 2 == 0:
            adjusted = normalized * penalty_factor
        else:
            adjusted = normalized + (0.05 * i)

        # Only every third record contributes to total
        if (i + 1) % 3 == 0 or i == len(records) - 1:
            total += adjusted

        adjustments.append(adjusted)

    # Misleading dead-end calculation
    hypothetical_max = len(records) * 10
    decay_rate = 0.95
    projected_loss = hypothetical_max * (1 - decay_rate)

    # Actual final computation
    trend = sum(adjustments[::2])  # Slice: even indices
    volatility = abs(adjustments[-1] - adjustments[0])

    final_score = int(total + trend - volatility)

    # Irrelevant cleanup
    bonus_tracker.clear()
    del penalty_factor

    return final_score

# Input data
assessments = [
    {'metrics': [2.1, 3.4, 1.8, 4.0]},
    {'metrics': [3.0, 2.9, 3.1]},
    {'metrics': [4.2, 3.8, 4.0, 3.9]},
    {'metrics': [2.5, 2.7]}
]
benchmark = 3.0

result = evaluate_performance(assessments, benchmark)
final_score = result
print(f"Target result: {final_score}")