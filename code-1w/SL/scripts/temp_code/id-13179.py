import itertools

def preprocess_data(raw):
    # Distractor: normalization that isn't used in final calculation
    normalized = [(x - min(raw)) / (max(raw) - min(raw)) for x in raw]
    scaled = [int(x * 100) for x in normalized]  # Unused path
    return [x for x in raw if x > 0]  # Only filtering matters

def calculate_entropy(values):
    # Red herring function, never called in execution
    from math import log
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * log(p) for p in probs if p > 0)

def calculate_final_score(entries, importance):
    # Core logic begins
    filtered = preprocess_data(entries)
    weighted = [a * b for a, b in zip(filtered, importance[:len(filtered)])]
    
    # Intermediate transformation with distractor variables
    squared_devs = [(x - sum(weighted)/len(weighted))**2 for x in weighted]
    variance_proxy = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    # Real computation path
    running_total = 0
    for i, val in enumerate(itertools.islice(itertools.cycle(weighted), 0, 10)):
        if i % 3 == 0:
            running_total += val * 2
        elif i % 5 == 0:
            running_total -= val
        else:
            running_total += val // 2
    
    # Final adjustment
    adjustment = len([x for x in weighted if x > 5])
    final_score = int(running_total + adjustment)
    
    # Dead code branch (never reached)
    if False:
        fallback = sum(weighted) * 0.5
        final_score = max(fallback, final_score)

    return final_score

# Main execution
raw_data = [3, -1, 4, 1, 5, -2]
weights = [2, 3, 1, 4, 2]

intermediate_sum = sum(x * 2 for x in raw_data)  # Irrelevant computation
placeholder = lambda x: x ** 0  # Unused lambda

processed_data = preprocess_data(raw_data)
clean_weights = [w + 0.0 for w in weights]  # Trivial copy

final_score = calculate_final_score(raw_data, clean_weights)
print(f"Result: {final_score}")