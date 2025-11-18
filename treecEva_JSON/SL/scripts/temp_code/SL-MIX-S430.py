import itertools
import statistics

primary_metrics = [12, 15, 8, 20, 15, 30]
secondary_metrics = [45, 15, 60, 25, 15, 40]

valid_xors = [
    a ^ b
    for a, b in itertools.product(primary_metrics, secondary_metrics)
    if (a > 10 and b < 50) or (a == b)
]

performance_score = int(statistics.mean(valid_xors))

print(f"Result: {performance_score}")