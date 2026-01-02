def process_data(items, limit):
    # Irrelevant transformation (distractor)
    temp_scale = lambda x: (x * 9/5) + 32
    scaled_values = [temp_scale(v) for v in items if v % 2 == 0]

    # Semi-relevant pre-processing
    filtered = [x for x in items if x > 0]
    normalized = [x / sum(filtered) for x in filtered]

    # Core logic disguised among distractions
    weights = [i+1 for i in range(len(normalized))]
    weighted_sum = sum(w * n for w, n in zip(weights, normalized))

    # Red herring: unused complex calculation
    entropy = -sum(p * __import__('math').log(p) for p in normalized if p > 0)
    max_entropy = __import__('math').log(len(normalized)) if normalized else 1

    # Actual decision logic
    adjustment_factor = 2 if len(items) % 4 == 0 else 0.5
    score = weighted_sum * adjustment_factor

    # Final result based on threshold comparison
    threshold = 1.0
    if score > threshold:
        result = int(score * 100) % 97
    else:
        result = int(score * 50) % 97

    return result

# Setup data
raw_input = "8,4,12,6,10"
data = list(map(int, raw_input.split(',')))
dummy_matrix = [[i*j for j in range(3)] for i in range(3)]  # Unused structure
threshold = 9.5

# Execute main logic
temperature_warning = False
if any(t > 30 for t in data):
    temperature_warning = True

result = process_data(data, threshold)
print(f"Target result: {result}")