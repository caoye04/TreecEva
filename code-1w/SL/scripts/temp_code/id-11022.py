def analyze_efficiency(values):
    squared = [x ** 2 for x in values]
    shifted = [x >> 1 for x in squared]
    filtered = [x for x in shifted if x > 50]
    return sum(filtered)


def extract_features(data_list):
    indexed = list(enumerate(data_list))
    zipped = list(zip(indexed, [x * 2 for x in data_list]))
    features = []
    for (i, val), doubled in zipped:
        if i % 2 == 0:
            features.append(val + doubled)
    return features

# Simulate sensor metrics with redundant computations
data_stream = [3, 7, 4, 9, 2, 8]

# Irrelevant transformation chain (distractor)
distorted = []
for x in data_stream:
    temp_val = x ^ 5
    temp_val = temp_val & 10
    distorted.append(temp_val)

# Relevant feature extraction
features = extract_features(data_stream)

# Additional distracting set operations
unique_features = set(features)
duplicated = set([x * 2 for x in features])
overlap = unique_features.intersection(duplicated)

# Core metric computation
raw_metrics = [analyze_efficiency(data_stream)]

# Weight assignment with red herring variables
weights = [0.3, 0.5, 0.2]  # only first weight used
bias_correction = 0.1  # never applied
normalization_factor = max(features) if features else 1  # computed but unused

# Actual performance evaluation logic
def evaluate_performance(metrics, w):
    base = metrics[0] * w[0]
    adjustment = 0
    for i, f in enumerate(features):
        if f > 10:
            adjustment += 1
    result = base + adjustment
    
    # Dead code branch (never reached due to structure)
    if len(metrics) > 5:
        result -= 5  # unreachable
    
    return int(result)

# Final score calculation
final_score = evaluate_performance(raw_metrics, weights)
print(f"Target result: {final_score}")