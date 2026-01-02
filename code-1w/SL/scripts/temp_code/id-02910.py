from collections import defaultdict
import math

# Function to calculate combinations (n choose k)
def calculate_combinations(n, k):
    if k > n or k < 0:
        return 0
    return math.comb(n, k)

# Irrelevant helper (minor distraction)
def normalize_scores(scores):
    total = sum(scores)
    return [s / total for s in scores]

# Main data
participants = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
teams = len(participants)

# Extra variable (low interference)
score_map = defaultdict(int)
for i, name in enumerate(participants):
    score_map[name] = i + 1

# Key computation
selection_size = 3
result = calculate_combinations(teams, selection_size)

# Print final result
print(f"Target result: {result}")