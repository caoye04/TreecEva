import itertools

def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(1 for a, b in itertools.pairwise(sequence) if a < b)

def preprocess_data(raw):
    # Distractor: transforms data but not used in final computation
    cleaned = [x for x in raw if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return [round(x, 3) for x in normalized]

def calculate_entropy(vals):
    # Misleading intermediate: looks important but unused
    from math import log2
    freq = {}
    for v in vals:
        freq[v] = freq.get(v, 0) + 1
    total = len(vals)
    return -sum((count / total) * log2(count / total) for count in freq.values())

def evaluate_performance(metrics, weights):
    # Core logic buried among distractions
    base = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            base += metrics[i] * weights[i]
        else:
            base -= metrics[i] * 0.5  # Irregular rule to increase complexity

    adjustment = 0
    for w in weights:
        if w > 0.2:
            adjustment += w ** 2

    # Key transformation using lambda and list comprehension
    factors = list(map(lambda x: x + adjustment, [0.1, 0.3, 0.6]))
    
    # Red herring: complex-looking but unused itertools operation
    permutations = list(itertools.permutations([1, 2, 3]))
    cycle = itertools.cycle([1])
    next(cycle); next(cycle)  # Consumed but irrelevant

    # Actual answer derivation
    temp = base * factors[1]  # factors[1] = 0.3 + adjustment
    final_score = int(round(temp * 1000)) // 10  # Final deterministic transformation

    # Dead branches with early returns that don't trigger
    if final_score < 0:
        return -1
    if final_score == 42:
        return 999

    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = [85, 90, 78, 92]
    weights = [0.3, 0.4, 0.2, 0.1]

    # Irrelevant preprocessing
    processed_metrics = preprocess_data(metrics)
    entropy = calculate_entropy(metrics)

    # Unused pattern analysis
    trend = analyze_pattern([10, 20, 30, 25, 35])

    # Key computation
    final_score = evaluate_performance(metrics, weights)

    # Output result as required
    print(f"Result: {final_score}")