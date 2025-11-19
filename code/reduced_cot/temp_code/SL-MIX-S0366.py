import math
from collections import deque

def compute_windowed_correlation(signal_a, signal_b, window_size):
    scores = []
    for i in range(len(signal_a) - window_size + 1):
        window_a = signal_a[i:i+window_size]
        window_b = signal_b[i:i+window_size]
        mean_a, mean_b = sum(window_a)/len(window_a), sum(window_b)/len(window_b)
        numerator = sum((a - mean_a) * (b - mean_b) for a, b in zip(window_a, window_b))
        denominator = math.sqrt(sum((a - mean_a)**2 for a in window_a) * sum((b - mean_b)**2 for b in window_b))
        scores.append(numerator / denominator if denominator != 0 else 0)
    return scores

signal_x = [1, 3, -2, 4, 5, -1, 2, 0, 3, 1]
signal_y = [2, 1, 3, -1, 4, 2, -2, 1, 0, 2]
window_len = 4

raw_scores = compute_windowed_correlation(signal_x, signal_y, window_len)
filtered_scores = [score for score in raw_scores if abs(score) > 0.1]

stack = deque()
for val in filtered_scores:
    if stack and abs(stack[-1] - val) < 0.15:
        stack.pop()
    stack.append(val)

processed_values = list(stack)
thresh_map = {val: idx for idx, val in enumerate(sorted(processed_values, reverse=True))}
lambda_func = lambda x: x**2 if x > 0 else -abs(x)**1.5
transformed = [lambda_func(val) for val in processed_values]

final_metric = round(sum(transformed) / len(transformed), 4) if transformed else 0
print(f"Result: {final_metric}")