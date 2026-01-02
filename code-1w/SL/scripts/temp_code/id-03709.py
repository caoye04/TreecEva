from itertools import cycle

# Simulate sensor weights and harmonic response frequencies
weights = [0.8, 1.2, 0.9, 1.5, 1.1]
base_freq = 2.0
harmonics = [round(base_freq ** (i % 4 + 1), 2) for i in range(5)]

# Irrelevant auxiliary sequence (distractor)
indices_tracker = list(enumerate(['A', 'B', 'C', 'D', 'E']))

# Key computation: weighted harmonic contribution
weighted_products = []
for i, w in enumerate(weights):
    weighted_products.append(w * harmonics[i])

# Combine using generator expression with zip
total_harmonic_weight = sum(weights[i] * harmonics[i] for i in range(len(weights)))

# Additional unrelated variable (minor distraction)
status_codes = dict(zip(['INIT', 'RUN', 'ERR'], [100, 200, 500]))

print(f"Result: {total_harmonic_weight}")