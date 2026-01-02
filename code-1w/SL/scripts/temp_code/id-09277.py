import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = [45, 87, 12, 76, 58, 91, 33, 64]
    offsets = [2, -5, 8, -3, 0, 6, -9, 4]
    adjusted = [raw_data[i] + offsets[i] for i in range(len(raw_data))]
    
    # Irrelevant transformation: frequency analysis of digits (red herring)
    digit_count = {}
    for val in raw_data:
        for digit in str(val):
            digit_count[int(digit)] = digit_count.get(int(digit), 0) + 1
    
    # Decoy metric with no downstream use
    anomaly_flags = [x < 20 or x > 90 for x in adjusted]
    
    # Actual normalized metrics used later
    normalized = [max(0.0, min(100.0, x)) / 100.0 for x in adjusted]
    return normalized

# Weighting model for performance dimensions
def generate_weights():
    base_weights = [0.1, 0.2, 0.15, 0.05, 0.1, 0.1, 0.2, 0.05]
    
    # Distractor: entropy calculation on weights (unused)
    entropy = 0.0
    for w in base_weights:
        if w > 0:
            entropy -= w * math.log(w)
    
    # Noise injection and cleanup (misleading path)
    noisy = [w + (0.01 if i % 2 == 0 else -0.01) for i, w in enumerate(base_weights)]
    cleaned = [max(0.01, abs(w)) for w in noisy]
    total = sum(cleaned)
    cleaned = [w / total for w in cleaned]  # Re-normalized but not used
    
    # Correct fixed weights actually used
    return base_weights

# Core evaluation logic
def evaluate_performance(metrics, weights):
    if len(metrics) != len(weights):
        raise ValueError("Mismatched dimensions")
    
    # Step 1: Apply weighted sum
    weighted_sum = sum(metrics[i] * weights[i] for i in range(len(metrics)))
    
    # Step 2: Apply non-linear compression using tanh (important)
    compressed = math.tanh(weighted_sum * 2)
    
    # Step 3: Boost based on consistency bonus (custom heuristic)
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    consistency_bonus = max(0, (0.1 - variance) * 5)  # Caps at 0.1 when variance is low
    
    # Step 4: Apply bonus
    boosted = compressed + consistency_bonus
    
    # Step 5: Scale to 0-100 score
    score_100 = boosted * 100
    
    # Step 6: Apply final threshold clamp
    clamped = max(10, min(95, score_100))  # Hard bounds
    
    # Irrelevant alternative scoring models (dead code paths)
    def quadratic_model():
        return sum(w * m**2 for w, m in zip(weights, metrics)) * 80
    
    def rank_based_model():
        sorted_vals = sorted(metrics)
        ranks = [sorted_vals.index(m) + 1 for m in metrics]
        return sum(r * w for r, w in zip(ranks, weights)) * 10
    
    # Unused conditional branch with misleading intermediate
    if False:  # Dead branch
        temp_result = math.sqrt(score_100)
        fallback = temp_result * 10
        return fallback
    
    return clamped

# Auxiliary function that looks important but isn't used in main flow
def calculate_reliability_index(data):
    mean = sum(data) / len(data)
    deviations = [abs(x - mean) for x in data]
    mad = sum(deviations) / len(deviations)
    return 1 / (1 + mad) if mad > 0 else 1

# Unused utility: computes prime factors of a number (completely irrelevant)
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Main execution
if __name__ == "__main__":
    # Collect performance metrics
    metrics = collect_metrics()  # Returns [0.47, 0.82, 0.2, 0.73, 0.58, 0.97, 0.24, 0.68]
    
    # Generate weighting scheme
    weights = generate_weights()
    
    # Compute final score
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")