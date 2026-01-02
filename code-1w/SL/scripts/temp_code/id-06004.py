def analyze_efficiency(metrics):
    base = sum([m ** 0.5 for m in metrics if m > 0])
    adjustment = len([m for m in metrics if m < 50]) * 0.1
    return base - adjustment

productivity = [81, 64, 25, 100, 49]
efficiency = analyze_efficiency(productivity)

# Distractor: irrelevant transformation on string version
str_metrics = ''.join(map(str, productivity))
shifted = str_metrics[2:] + str_metrics[:2]  # slicing operation
int_sequence = int(shifted) % 97

# Dummy risk factors with red herring calculations
raw_inputs = [3, 7, 2, 8, 5]
filtered = list(filter(lambda x: x > 4, raw_inputs))
dummy_risk = sum([x * 1.5 for x in filtered]) / len(filtered)

risk_factor = 0.4 * (efficiency / 10)

# Simulate conditional weighting using boolean logic and comparisons
weight = 1.2 if efficiency > 18 and risk_factor < 0.6 else 0.8
penalty = 0.05 if '100' in shifted else 0.0

adjusted_efficiency = efficiency * weight - (10 * penalty)

# Secondary distraction: combinatorics-like count (not directly used)
total_pairs = 0
for i in range(len(productivity)):
    for j in range(i + 1, len(productivity)):
        if (productivity[i] + productivity[j]) % 10 == 0:
            total_pairs += 1

# Core evaluation function using multiple concepts
def evaluate_performance(perf_data, rsk):
    base_val = sum(perf_data) / len(perf_data)
    boost = 5 if base_val >= 60 else 0
    decay = 3 if rsk > 0.35 else 0
    return int(base_val + boost - decay)

final_score = evaluate_performance(productivity, risk_factor)

# Print required output
print(f"Result: {final_score}")