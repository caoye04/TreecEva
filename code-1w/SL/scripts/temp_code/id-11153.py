import math

def analyze_signal(samples):
    # Irrelevant function - signal processing red herring
    fft_magnitude = lambda x: sum(math.sin(s) ** 2 for s in x if s > 0.5)
    return [fft_magnitude(samples[i:i+4]) for i in range(0, len(samples), 4)]

def transform_coordinates(coords):
    # Distractor function - geometric transformation decoy
    rotate = lambda c: (c[0] * math.cos(math.pi/4) - c[1] * math.sin(math.pi/4),
                      c[0] * math.sin(math.pi/4) + c[1] * math.cos(math.pi/4))
    return list(map(rotate, coords))

def compute_entropy(data):
    # Seemingly important but unused function
    total = sum(data)
    probabilities = [d / total for d in data if d > 0]
    return -sum(p * math.log(p) for p in probabilities)

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjustment = 0
    if len(metrics) > base:
        adjustment += 12
    
    # Complex conditional with distractors
    temp_results = []
    for m in metrics:
        if m < 0:
            temp_results.append(abs(m) * 0.5)
        elif m > base * 2:
            temp_results.append(m * 0.8)
        else:
            temp_results.append(m)
    
    # Key calculation buried in list comprehension and lambda
    processed = [(lambda x: x + base)(val) for val in temp_results if val != 0]
    filtered = [p for p in processed if p <= 100]
    
    # Misleading average calculation (not used in final result)
    avg = sum(filtered) / len(filtered) if filtered else 0
    peak = max(filtered) if filtered else 0
    
    # Dead code path - looks important but unused
    if peak > 90:
        for i in range(len(filtered)):
            if filtered[i] < avg:
                filtered[i] = avg  # never actually affects final result

    # Critical intermediate value disguised as part of noise
    scaling_factor = 3
    aggregate = sum(filtered) * scaling_factor // len(filtered) if filtered else 0
    
    # Secondary distraction: recursive bit manipulation (unused)
    def count_bits(n):
        return 1 + count_bits(n & (n - 1)) if n else 0
    
    # Final score computed from non-obvious aggregation
    final_score = aggregate - adjustment
    return final_score

# Irrelevant data structures
signal_samples = [0.6, 0.3, 0.7, 0.9, 0.1, 0.4, 0.8]
geo_coords = [(3, 4), (5, 12), (8, 15)]
entropy_data = [20, 30, 50, 10]

# Unused but plausible-looking computations
_ = analyze_signal(signal_samples)
_ = transform_coordinates(geo_coords)
_ = compute_entropy(entropy_data)

# Main execution flow
metric_data = [10, -5, 25, 15, 0, 40, 8, 12]
baseline = 10

# Decoy loop that modifies nothing
for i in range(3):
    temp_val = baseline ** (i+1) * 2.5
    baseline -= 1  # Reverted immediately after
    baseline += 1

final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")