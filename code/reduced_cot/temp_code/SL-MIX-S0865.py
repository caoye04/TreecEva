from collections import defaultdict
import math

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_variance(values):
    if len(values) == 0:
        return 0
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)

daily_changes = [3, -1, 4, -2, 5, -3, 6]
weight_factors = [fibonacci(i) for i in range(1, len(daily_changes) + 1)]
portfolio_log = defaultdict(list)

for idx, (change, weight) in enumerate(zip(daily_changes, weight_factors)):
    adjusted_change = change * weight
    portfolio_log['adjusted'].append(adjusted_change)
    if idx > 0 and adjusted_change > 0 and portfolio_log['adjusted'][-2] < 0:
        portfolio_log['signals'].append(idx)

# Greedy selection of top 3 positive adjustments
positive_adjustments = [(i, val) for i, val in enumerate(portfolio_log['adjusted']) if val > 0]
positive_adjustments.sort(key=lambda x: x[1], reverse=True)
top_indices = {i for i, _ in positive_adjustments[:3]}

selected_values = [portfolio_log['adjusted'][i] for i in top_indices]
variance_of_selected = calculate_variance(selected_values)

final_adjustment_score = int(sum(selected_values) - variance_of_selected)
print(f"Result: {final_adjustment_score}")