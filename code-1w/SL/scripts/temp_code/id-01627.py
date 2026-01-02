def compute_status_score(levels, threshold=5):
    """Calculate status score based on level progression."""
    progression = [i for i, level in enumerate(levels) if level > threshold]
    if not progression:
        return 0
    return progression[0] * 2

# System status levels over time
status_levels = [3, 4, 6, 7, 8, 5, 2]

# Compute activation score
score = compute_status_score(status_levels)

# Bitwise normalization with system mask
normalized = score & 7  # Mask to 3 bits

# Status mapping dictionary
status_map = {
    'initial': 0,
    'active': 1,
    'final': 2
}

# Simulate stage transitions using slicing
stages = ['start', 'mid', 'end']
recent_stages = stages[-2:]

# Final scores based on normalized result and stage
base_value = 100
increment = 25
final_scores = [
    base_value,
    base_value + increment,
    base_value + (normalized ^ 3)  # XOR adjustment
]

result = final_scores[status_map['final']]
print(f"Result: {result}")