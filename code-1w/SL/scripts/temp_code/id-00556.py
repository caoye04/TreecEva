def compute_weights(values):
    return [round(v ** 0.5, 2) for v in values if v > 0]

# Sensor readings from environmental monitoring stations
event_readings = [16, 25, 0, 36, -4, 49, 64]
valid_indices = [i for i in range(len(event_readings)) if event_readings[i] > 0]

# Compute derived weights and pair with indices
weights = compute_weights(event_readings)
prioritized = {idx: weights[idx] for idx in range(len(weights))}

# Rank by weight strength
sorted_pairs = sorted(prioritized.items(), key=lambda x: x[1], reverse=True)
final_ranking = [index for index, _ in sorted_pairs]

dummy_var = sum(1 for w in weights if w > 5)  # Irrelevant metric (minimal distraction)
threshold_score = final_ranking[2]
print(f"Result: {threshold_score}")