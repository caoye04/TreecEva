from itertools import combinations

# Simulated system performance metrics over time
metrics = [0.85, 0.91, 0.76, 0.94, 0.88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Auxiliary diagnostic data (not directly used in final calculation)
diagnostic_logs = [(t, val * 100) for t, val in enumerate(metrics)]
temp_analysis = [abs(x - 0.85) for x in metrics]

# Misleading intermediate transformation (unused in result)
transformed_metrics = [round(m ** 2 / w, 3) for m, w in zip(metrics, weights)]

# Generate all possible metric pairs for redundancy analysis (distractor)
pairwise_consistency = []
for pair in combinations(metrics, 2):
    pairwise_consistency.append(round(abs(pair[0] - pair[1]), 3))

# Secondary weight adjustment (irrelevant to final path)
adjusted_weights = [w + 0.05 if m > 0.8 else w for m, w in zip(metrics, weights)]

# Real-time fluctuation index (dead computation)
fluctuation_index = sum(1 for i in range(1, len(metrics)) if abs(metrics[i] - metrics[i-1]) > 0.05)

# Key function computing weighted harmonic mean with filtering
valid_indices = [i for i, m in enumerate(metrics) if m >= 0.75]
filtered_metrics = [metrics[i] for i in valid_indices]
filtered_weights = [weights[i] for i in valid_indices]

# Normalize filtered weights
norm_factor = sum(filtered_weights)
normalized_weights = [w / norm_factor for w in filtered_weights]

# Compute weighted harmonic mean
inverse_sum = sum(w / m for w, m in zip(normalized_weights, filtered_metrics))
harmonic_mean = 1 / inverse_sum

# Apply secondary scaling based on count of high-performing metrics
bonus_factor = 1 + (sum(1 for m in metrics if m >= 0.9) * 0.02)
adjusted_mean = harmonic_mean * bonus_factor

# Final scoring with artificial offset (this is the actual final score)
baseline_offset = 5.0
final_score = int(round(adjusted_mean * 100 + baseline_offset))

print(f"Result: {final_score}")