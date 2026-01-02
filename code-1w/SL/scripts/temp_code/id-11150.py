from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'X' and i + 1 < len(sequence) and sequence[i+1] == 'Y':
            count += 1
    return count

def evaluate_streak(data):
    max_streak = 0
    current = 0
    for val in data:
        if val > 0:
            current += val
        else:
            max_streak = max(max_streak, current)
            current = 0
    max_streak = max(max_streak, current)
    return max_streak

def calculate_performance(results):
    raw_values = [x['score'] for x in results if x['active']]
    adjustments = [0.5 * x for x in raw_values if x > 10]
    base = sum(raw_values)
    bonus = len(adjustments)
    penalty = analyze_pattern('XYYXY')
    streak = evaluate_streak(raw_values)
    final = base + bonus - penalty + streak
    return final

# Simulated benchmark data
benchmark_results = [
    {'score': 12, 'active': True},
    {'score': 8, 'active': True},
    {'score': 15, 'active': True},
    {'score': 5, 'active': False},
    {'score': 20, 'active': True}
]

intermediate = list(combinations([1, 2, 3], 2))  # Irrelevant usage of itertools

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")