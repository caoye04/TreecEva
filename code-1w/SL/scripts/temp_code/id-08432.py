def preprocess_input(raw_data):
    cleaned = [x.strip().lower() for x in raw_data if x.strip()]
    encoded = [sum(ord(c) for c in item) for item in cleaned]
    return encoded

raw_input = [' Alice ', 'BOB', 'charlie!', 'DORIS', 'ed']

# Irrelevant transformation chain
shifted_values = [val + 10 for val in range(5)]
temp_matrix = [[i * j for j in shifted_values] for i in range(3)]
matrix_sum = sum(sum(row) for row in temp_matrix)

# Main data path
encoded_data = preprocess_input(raw_input)
scaled_data = [x / max(encoded_data) * 100 for x in encoded_data]

# Weighting system with red herring
weights = [0.1, 0.2, 0.3, 0.25, 0.15]
fake_weights = [w ** 2 for w in weights]  # Unused but plausible

# Conditional scaling based on pattern
threshold = 75
adjusted_data = [
    val * 1.1 if val > threshold else val * 0.9
    for val in scaled_data
]

# Dummy state tracker (distractor)
count_high = 0
for val in adjusted_data:
    if val > threshold:
        count_high += 1

# Actual computation buried in logic
status_flags = [1 if x > 90 else 0 for x in adjusted_data]
bonus_points = sum(flag * 5 for flag in status_flags)

# Core calculation
base_total = sum(val * weight for val, weight in zip(adjusted_data, weights))

# Secondary adjustment
penalty = 0
for i, val in enumerate(adjusted_data):
    if i % 2 == 1 and val < 80:
        penalty += 2

intermediate_score = base_total - penalty + bonus_points

# Final nonlinear adjustment using conditional expression
final_score = intermediate_score * (1.05 if bonus_points >= 10 else 1.0)

print(f"Result: {final_score}")