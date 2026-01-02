def analyze_efficiency(data, thresholds):
    efficiency_list = []
    for i, val in enumerate(data):
        if val > thresholds[i % len(thresholds)]:
            efficiency_list.append(val * 0.85)
        else:
            efficiency_list.append(val * 1.15)
    return efficiency_list

# Irrelevant helper function (decoy)
def calculate_redundant_metric(x):
    temp = 0
    for i in range(len(x)):
        temp += x[i] * (i + 1) ** 2
    return temp // 7 if temp > 0 else 0

# Another decoy with dead logic
def predict_outcome(values):
    if sum(values) < 0:
        return [v * 2 for v in values]
    elif len(values) > 10:
        return [v - 1 for v in values]
    else:
        return None  # Dead end, never used

# Core data
raw_metrics = [42, 78, 56, 91, 33, 67, 88]
thresholds = [50, 70, 60]
weights = [0.2, 0.15, 0.18, 0.22, 0.1, 0.08, 0.07]

# Distractor variables
junk_data = [x ** 2 for x in raw_metrics if x < 70]
scaling_factor = 1.04
offset_adjustment = sum(junk_data) / 100 if junk_data else 0

# Misleading intermediate transformation
adjusted_metrics = [m + offset_adjustment for m in raw_metrics]

# Real processing begins: efficiency analysis
processed_efficiency = analyze_efficiency(adjusted_metrics, thresholds)

# Secondary irrelevant smoothing
smoothed = []
for idx, (a, b) in enumerate(zip(processed_efficiency, processed_efficiency[1:])):
    smoothed.append((a + b) / 2 * 0.95)
smoothed.append(processed_efficiency[-1])  # Align lengths

# Simulate environmental interference (unused)
environmental_factors = [1.01, 0.99, 1.02, 0.98, 1.03, 0.97, 1.04]

# Decoy list comprehension with no impact
tainted_check = [e * f for e, f in zip(smoothed, environmental_factors) if e > 60]

# Key function that computes the answer
def evaluate_performance(metrics, weights):
    total = 0.0
    for i, (m, w) in enumerate(zip(metrics, weights)):
        contribution = m * w
        if i % 2 == 0:
            contribution *= 1.1  # Bonus on even indices
        else:
            contribution *= 0.95
        total += contribution
    
    # Artificial complexity: add checksum only if length matches
    if len(metrics) == len(weights):
        checksum = sum(int(w * 100) for w in weights)
        total += checksum * 0.01
    
    # Early return red herring (never triggered due to data)
    if total < 0:
        return -1
        
    return total

# Final computation
final_score = evaluate_performance(processed_efficiency, weights)

# Print result as required
print(f"Target result: {final_score}")