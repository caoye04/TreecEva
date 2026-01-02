import math

# Simulate a physics-informed data processing pipeline with red herrings
def preprocess(inputs):
    temp_a = [x ** 2 for x in inputs if x > 0]
    temp_b = [math.sqrt(y) for y in temp_a]
    padding = sum(temp_b) / len(temp_b) if temp_b else 0
    return [z + padding for z in temp_a]

# Misleading helper: looks important but only used once trivially
def outlier_detector(seq):
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq)
    return [x for x in seq if abs(x - mean_val) > math.sqrt(variance)]

# Core transformation chain
def transformer(block):
    shifted = [x * 0.5 for x in block]
    modded = [int(y) % 7 for y in shifted]
    return list(map(lambda val: val ** 3 - val, modded))

# Another irrelevant utility to increase cognitive load
def entropy_approx(data):
    total = sum(data)
    probs = [d / total for d in data if d > 0]
    return -sum(p * math.log(p) for p in probs)

# Data refinement with conditional filtering
def refine(chunk):
    filtered = []
    for item in chunk:
        if item < 50:
            filtered.append(item + 3)
        elif item > 100:
            filtered.append(item - 10)
        else:
            filtered.append(item)
    return [f for f in filtered if f % 2 == 1]  # Keep only odds

# Final aggregation logic
def finalizer(cleaned):
    base = sum(cleaned)
    adjustment = len(cleaned) * 2
    return base - adjustment

# Main execution flow
if __name__ == "__main__":
    raw_input = [4, -2, 8, 1, 0, 6]

    # Step 1: Preprocess with hidden side-effect (only padding matters indirectly)
    stage_one = preprocess(raw_input)

    # Distractor: Compute outliers but do not use them
    detected_outliers = outlier_detector(stage_one)

    # Step 2: Transform using lambda-heavy logic
    stage_two = transformer(stage_one)

    # Step 3: Refine with conditional rules
    processed_data = refine(stage_two)

    # Distractor: Calculate entropy but never use it
    _ = entropy_approx(processed_data)

    # Key statement: Compute final equilibrium score
    equilibrium_score = finalizer(processed_data)

    print(f"Result: {equilibrium_score}")