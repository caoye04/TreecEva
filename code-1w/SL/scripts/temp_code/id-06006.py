def analyze_sentiment(value):
    return value * 0.9 if value > 0 else abs(value) * 1.1

# Simulate multi-stage feedback processing in a training loop
raw_inputs = [12, -8, 15, -22, 9]
sentiment_adjusted = list(map(analyze_sentiment, raw_inputs))

# Distractor: Irrelevant transformation on same data
normalized_data = [x / max(raw_inputs) for x in raw_inputs if x != 0]
weight_map = {i: val * 0.1 for i, val in enumerate(raw_inputs)}

# Real computation begins: build feedback chain using zip and enumerate
feedback_strength = []
for idx, (raw, adj) in enumerate(zip(raw_inputs, sentiment_adjusted)):
    adjustment_factor = abs(adj - raw)
    if adjustment_factor > 5:
        feedback_strength.append(adjustment_factor * 0.7)
    else:
        feedback_strength.append(adjustment_factor * 1.3)

# Apply lambda-based filtering and aggregation
valid_feedback = list(filter(lambda x: x > 4, feedback_strength))
baseline_offset = sum([abs(raw_inputs[i]) * 0.05 for i in range(len(raw_inputs))])

# Secondary distractor: unused helper logic
compute_deviation = lambda seq: sum((x - sum(seq)/len(seq))**2 for x in seq) / len(seq) if seq else 0
dev_value = compute_deviation(normalized_data)  # Dead computation

# Core evaluation logic with dictionary accumulation
feedback_chain = {}
for i, val in enumerate(valid_feedback):
    key = f"stage_{i % 3}"
    feedback_chain[key] = feedback_chain.get(key, 0) + val

# Final scoring with conditional weighting
rolling_total = 0
tier_multiplier = {'stage_0': 1.2, 'stage_1': 1.5, 'stage_2': 1.1}
for k, v in feedback_chain.items():
    if k in tier_multiplier:
        rolling_total += v * tier_multiplier[k]

final_score = int(rolling_total + baseline_offset)

# Print result as required
print(f"Target result: {final_score}")