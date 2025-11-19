import math
from functools import reduce

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        seq = [1, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq

# Sensor readings with time intervals and strength values
sensor_readings = [
    {'start': 0, 'end': 3, 'strength': 8},
    {'start': 1, 'end': 4, 'strength': 7},
    {'start': 3, 'end': 5, 'strength': 4},
    {'start': 5, 'end': 7, 'strength': 11},
    {'start': 6, 'end': 9, 'strength': 6},
    {'start': 8, 'end': 10, 'strength': 5}
]

# Sort by end time for greedy selection
sorted_signals = sorted(sensor_readings, key=lambda x: x['end'])

# Calculate variances for statistical weighting
signal_strengths = [s['strength'] for s in sorted_signals]
mean_strength = sum(signal_strengths) / len(signal_strengths)
variance = sum((x - mean_strength) ** 2 for x in signal_strengths) / len(signal_strengths)

# Apply Fibonacci weights based on position
fib_weights = fibonacci_sequence(len(sorted_signals))
weighted_signals = [
    {
        'start': s['start'],
        'end': s['end'],
        'strength': s['strength'],
        'weighted_strength': s['strength'] * fib_weights[i] * (1 + variance/100)
    }
    for i, s in enumerate(sorted_signals)
]

# Dynamic programming array for maximum non-overlapping signal selection
n = len(weighted_signals)
dp = [0] * (n + 1)

# Fill DP table using greedy approach with short-circuit evaluation
for i in range(1, n + 1):
    current = weighted_signals[i-1]['weighted_strength']
    # Find latest non-overlapping signal using comparison operations
    j = i - 1
    while j >= 1 and weighted_signals[j-1]['end'] > weighted_signals[i-1]['start']:
        j -= 1
    
    # Short-circuit evaluation to determine optimal selection
    dp[i] = dp[i-1] if j == 0 else max(dp[i-1], dp[j] + current) if current > 0 else dp[i-1]

# Final score combines DP result with statistical adjustment
optimal_selection_score = int(dp[n] * (1 + math.log(variance + 1)))
print(f"Result: {optimal_selection_score}")