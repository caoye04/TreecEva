def process_item(x):
    return x * 2 + 1

# Irrelevant helper that isn't used
def dummy_transform(items):
    return [item ** 2 for item in items if item % 3 == 0]

# Data preprocessing with distraction
raw_values = [3, 7, 12, 15, 21, 22]
filtered = list(filter(lambda y: y > 10, raw_values))

# Misleading aggregation
sum_check = 0
for val in raw_values:
    if val < 15:
        sum_check += val

# Actual computation path
transformed = []
for v in filtered:
    if v % 2 == 1:
        transformed.append(process_item(v))

# Simulate state tracking (only some states matter)
counters = {'odd_processed': 0, 'total_steps': 0}
intermediate_results = []
for num in transformed:
    counters['total_steps'] += 1
    if num > 30:
        counters['odd_processed'] += 1
    # Apply another layer of logic
    adjusted = num - 5
    intermediate_results.append(adjusted)

# Use of dictionary mapping (semi-relevant)
mapping = {i: val for i, val in enumerate(intermediate_results)}

# Final processor function that determines result
def processor(data):
    base = 0
    for idx, value in enumerate(data):
        if idx % 2 == 0:
            base += value
        else:
            base -= value
    return base * 2

result = processor(intermediate_results)
print(f"Target result: {result}")