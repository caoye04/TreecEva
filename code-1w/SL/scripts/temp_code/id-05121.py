def process_intervals(intervals, limit):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    
    for i, (start, end) in enumerate(intervals):
        duration = end - start
        if duration > limit:
            adjustment = (duration % 3) * weights[i % len(weights)]
            weighted_sum += duration + adjustment
    
    apply_bonus = lambda x: x * 1.1 if x > 25 else x
    return int(apply_bonus(weighted_sum))

# Irrelevant auxiliary variable (minimal distraction)
counter_hint = [x for x in range(4)]

intervals = [(10, 15), (20, 28), (30, 33), (40, 46)]
threshold = 7
result = process_intervals(intervals, threshold)
print(f"Result: {result}")