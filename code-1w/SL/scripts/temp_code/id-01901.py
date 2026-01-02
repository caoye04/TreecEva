def calculate_rating(items, deductions):
    base = sum(item[1] for item in items)
    multiplier = 1.0
    
    # Irrelevant tracking variables (distractors)
    total_accesses = 0
    temp_buffer = []
    for i, (name, value) in enumerate(items):
        if i % 2 == 0:
            temp_buffer.append(value * 1.1)  # Not used later
        total_accesses += 1  # Dead-end counter

    # Semi-relevant adjustment logic with conditional expression
    adjustment = sum(d for d in deductions if d > 0) or 5
    multiplier += 0.1 if adjustment > 10 else 0.05
    
    # Core computation interleaved with noise
    weighted_sum = 0
    weights = [1.0, 1.5, 2.0, 1.7, 1.2]
    for idx, (_, val) in enumerate(items):
        if idx < len(weights):
            weighted_sum += val * weights[idx]
        else:
            weighted_sum += val * 0.8
    
    # Misleading intermediate calculation (not final)
    provisional_score = (base + weighted_sum) / 2.0
    
    # Actual key logic: combining weighted sum and adjustment
    raw_score = weighted_sum - adjustment
    
    # Another distraction: unused list comprehension
    _ = [x * x for x in range(len(items) + len(deductions)) if x % 3 == 0]
    
    # Final rating formula
    final_rating = int(raw_score * multiplier)
    
    return final_rating

# Main data setup
contributions = [
    ('review', 8),
    ('docs', 6),
    ('tests', 10),
    ('design', 7),
    ('debug', 5)
]

penalties = [3, -2, 8, 0]  # Only positive values count as real penalties

# State tracking distractor
iteration_log = {}
for step, entry in enumerate(zip(contributions, penalties + [0])):
    key = f'step_{step}'
    iteration_log[key] = {
        'item_value': entry[0][1],
        'penalty_raw': entry[1],
        'impact': entry[0][1] - entry[1]
    }

# Key assignment statement
final_score = calculate_rating(contributions, penalties)

print(f"Result: {final_score}")