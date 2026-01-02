def analyze_response_time(rt):
    if rt < 0.1:
        return 'exceptional'
    elif rt < 0.25:
        return 'good'
    elif rt < 0.5:
        return 'average'
    else:
        return 'slow'

# Simulated user interaction data
timestamps = [1.2, 1.5, 1.7, 2.0, 2.4, 2.9, 3.1]
response_times = [round((timestamps[i] - timestamps[i-1]) * 100) / 100 for i in range(1, len(timestamps))]

# Categorize each response time
categories = [analyze_response_time(rt) for rt in response_times]

# Irrelevant distraction: unused function
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Unused statistical artifact
mean_rt = sum(response_times) / len(response_times)
variance = compute_variance(response_times)  # Dead computation path

# Weight mapping for performance levels (used later)
level_weights = {'exceptional': 5, 'good': 3, 'average': 1, 'slow': -2}

# Misleading transformation: not used in final logic
decay_factors = [0.9 ** i for i in range(len(categories))]
adjusted_weights = [level_weights[cat] * decay_factors[i] for i, cat in enumerate(categories)]

# Another red herring: complex but unused list comprehension with zip
paired_analysis = [
    f'{cat} at {rt}s' for rt, cat in zip(response_times, categories) if rt > 0.2
]

# Core logic begins here — actual path to answer
feedback_levels = [analyze_response_time(rt) for rt in response_times]
weights = [level_weights[level] for level in feedback_levels]

# Accumulate base score without decay (correct path)
basic_accumulation = 0
for w in weights:
    basic_accumulation += w

# Decoy loop with no effect
running_total = 0
for i in range(len(weights)):
    running_total += weights[i] * (i + 1)  # Unused weighted index sum

# Actual aggregation function used
def aggregate_performance(levels, weight_map):
    total = 0
    bonus_triggered = False
    penalty_count = 0
    
    for idx, lvl in enumerate(levels):
        value = weight_map[lvl]
        total += value
        
        # Conditional bonus logic
        if value == 5 and idx > 0 and weight_map[levels[idx-1]] > 0:
            bonus_triggered = True
            
        if value == -2:
            penalty_count += 1
            
    # Apply conditional adjustments
    if bonus_triggered and penalty_count == 0:
        total += 4
    elif penalty_count >= 2:
        total -= penalty_count * 3
        
    # Hidden adjustment: first and last category same?
    if levels[0] == levels[-1]:
        total += 2
        
    return total

# Critical assignment — this is the key statement
final_score = aggregate_performance(feedback_levels, weights)

# Distractor: another function that looks important but isn't called
def finalize_report(score, history):
    import math
    normalized = math.tanh(score / 10)
    return {'score': score, 'status': 'valid' if normalized > 0 else 'invalid'}

# Print result as required
print(f"Result: {final_score}")