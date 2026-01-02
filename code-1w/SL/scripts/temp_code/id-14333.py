from itertools import groupby

def analyze_pattern(sequence):
    streaks = []
    current_streak = 0
    prev = None
    for val in sequence:
        if val == prev:
            current_streak += 1
        else:
            if current_streak > 0:
                streaks.append(current_streak + 1)
            current_streak = 1
        prev = val
    if current_streak > 0:
        streaks.append(current_streak + 1)
    
    # Distractor: unused computation
    max_gap = 0
    for i in range(1, len(streaks)):
        gap = abs(streaks[i] - streaks[i-1])
        if gap > max_gap:
            max_gap = gap
    
    return streaks

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 2 == 0]

# Another distractor variable
scaling_factor = 3.14159
offset_adjustment = sum([i * 2 for i in range(5)])  # evaluates to 20

sequence_data = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# Misleading transformation
transformed = list(map(lambda x: x ^ 1, sequence_data))  # flips bits

# Grouping operation (semi-relevant)
grouped = [list(g) for k, g in groupby(transformed)]

# Count groups of size >= 2 (this is actually used later)
large_groups = len([g for g in grouped if len(g) >= 2])

# More distraction: fake statistical analysis
mean_val = sum(transformed) / len(transformed)
deviation = sum([(x - mean_val) ** 2 for x in transformed]) / len(transformed)

# Real logic starts here
streak_analysis = analyze_pattern(sequence_data)

# Secondary processing: count how many streaks are odd
odd_streaks = len([s for s in streak_analysis if s % 2 == 1])

def calculate_final_score(raw_results):
    base = len(raw_results) * 7
    bonus = 0
    if odd_streaks > 2:
        bonus += 15
    if large_groups >= 2:
        bonus += 10
    penalty = 0
    if mean_val > 0.5:
        penalty += 5
    # Final formula uses only some components
    return base + bonus - penalty

# Key execution point
final_score = calculate_final_score(streak_analysis)

print(f"Result: {final_score}")