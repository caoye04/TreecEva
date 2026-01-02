from itertools import filterfalse

def filtered_sum(predicate, values):
    filtered = list(filter(predicate, values))
    return sum(filtered) if filtered else 0

data = [3, 7, -2, 8, 5, 12, 1]
threshold = 4

# Some auxiliary computation to mirror real-world preprocessing
weights = [1.0] * len(data)
normalized = [round(w * val, 2) for w, val in zip(weights, data)]
above_avg = len([n for n in normalized if n > sum(normalized) / len(normalized)])

# Key logic
use_advanced = len(data) > 5
result = filtered_sum(lambda x: x > threshold, data) if use_advanced else sum(filterfalse(lambda x: x <= threshold, data))

print(f"Target result: {result}")