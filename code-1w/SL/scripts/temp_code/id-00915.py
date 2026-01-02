import itertools

# Simulated system performance metrics with noise data
def generate_noise(length):
    return [i % 7 for i in range(length)]

def cleanup_data(data):
    # Irrelevant preprocessing step
    return [x for x in data if x > 2]

# Misleading auxiliary function (never called)
def decrypt_sequence(seq):
    return [pow(x, 3, 11) for x in seq]

# Unused transformation map
cipher_map = {k: (k * 11) % 17 for k in range(20)}

# Real weighting logic embedded in distractions
base_weights = [0.1, 0.25, 0.15, 0.3, 0.2]
adjustment_factor = 1.2

# Phantom variables to mislead
shadow_buffer = [4, 8, 15, 16, 23, 42]
dummy_mask = {f'flag_{i}': False for i in range(10)}

# Core evaluation logic
lambda_transform = lambda x: round(x ** 0.5, 3)

# Actual metric processor
def evaluate_metric(value, weight):
    normalized = value / 100
    adjusted = normalized * weight * adjustment_factor
    return round(adjusted, 4)

def evaluate_performance(metrics, weights):
    # Apply square root transform via lambda
    processed = list(map(lambda_transform, metrics))
    
    # Irrelevant set operations as distractors
    temp_set_a = {x for x in processed if x > 0.5}
    temp_set_b = {round(w, 2) for w in weights}
    temp_set_c = temp_set_a.symmetric_difference(temp_set_b)
    _ = len(temp_set_c)  # unused
    
    # Core calculation
    total = 0.0
    for i in range(len(processed)):
        if i % 2 == 0:
            total += evaluate_metric(processed[i] * 10, weights[i])
        else:
            total += weights[i] * (processed[i] / 10) * adjustment_factor
    
    # Additional irrelevant data structure
    history_log = []
    for combo in itertools.combinations_with_replacement([1, 2], 3):
        history_log.append(sum(combo))
    
    return round(total, 6)

# Noise-injected real data
raw_metrics = [85, 92, 78, 96, 88]
noise = generate_noise(len(raw_metrics))
metrics = [raw_metrics[i] + noise[i] % 3 for i in range(len(raw_metrics))]

# Unused alternate weights
fallback_weights = [w * 0.9 for w in base_weights]

# Final computation
final_score = evaluate_performance(metrics, base_weights)

# Output result
print(f"Result: {final_score}")