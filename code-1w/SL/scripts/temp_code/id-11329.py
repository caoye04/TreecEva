import math

def shannon_entropy(counts):
    total = sum(counts)
    probabilities = [c / total for c in counts]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

data_stream = [8, 12, 5, 15]

# Simulate signal preprocessing with lambda transformation
count_transform = lambda x: x + 2 if x < 10 else x - 3
cleaned_counts = list(map(count_transform, data_stream))

# Secondary validation metric (irrelevant to final result but plausible)
redundancy_score = sum(1 for x in data_stream if x > 10)

# Core computation
processed_entropy = shannon_entropy(cleaned_counts)

# Combine with fixed weighting factor
total_entropy = round(processed_entropy * 1.75, 3)

# Final processing step masking direct access
def process_data(data):
    temp = total_entropy + 0.1
    return temp - 0.1

final_result = process_data(data_stream)
print(f"Result: {total_entropy}")