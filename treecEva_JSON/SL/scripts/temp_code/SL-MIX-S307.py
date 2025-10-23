import re
from bisect import bisect_left

def binary_range_filter(values, low, high):
    sorted_vals = sorted(values)
    left_idx = bisect_left(sorted_vals, low)
    right_idx = bisect_left(sorted_vals, high)
    return sorted_vals[left_idx:right_idx]

def compute_weighted_score(filtered_values):
    weights = [i+1 for i in range(len(filtered_values))]
    total = sum(val * weight for val, weight in zip(filtered_values, weights))
    return round(total, 2)

class ExchangePattern:
    def __init__(self, pattern_regex, threshold):
        self.pattern = re.compile(pattern_regex)
        self.threshold = threshold

exchange_log = [
    "RATE:+0.0023",
    "RATE:-0.0015",
    "RATE:+0.0041",
    "RATE:+0.0009",
    "RATE:-0.0032",
    "RATE:+0.0058",
    "RATE:+0.0017",
    "RATE:-0.0004"
]

pattern_matcher = ExchangePattern(r"RATE:([+-]\d+\.\d+)", 0.002)
fluctuation_values = []

for entry in exchange_log:
    match = pattern_matcher.pattern.search(entry)
    if match:
        value = float(match.group(1))
        if abs(value) >= pattern_matcher.threshold:
            fluctuation_values.append(value)

significant_changes = binary_range_filter(fluctuation_values, -0.005, 0.006)
final_aggregation_score = compute_weighted_score(significant_changes)
print(f"Result: {final_aggregation_score}")