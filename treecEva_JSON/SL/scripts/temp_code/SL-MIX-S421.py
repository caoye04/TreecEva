from collections import defaultdict
from itertools import permutations
import statistics

def calculate_satisfaction(votes):
    # Count occurrences of each vote type
    vote_counter = defaultdict(int)
    for vote in votes:
        vote_counter[vote] += 1
    
    # Generate all permutations of unique votes
    unique_votes = list(vote_counter.keys())
    perm_count = 0
    valid_perms = []
    
    for p in permutations(unique_votes):
        perm_count += 1
        # Check if permutation satisfies logical condition
        if all(x <= y for x, y in zip(p, p[1:])) and len(p) > 1:
            valid_perms.append(p)
    
    # Compute scores for valid permutations
    scores = []
    for perm in valid_perms:
        # Calculate weighted score based on frequency
        score = sum(vote_counter[vote] * (i + 1) for i, vote in enumerate(perm))
        scores.append(score)
    
    # Return mean of scores or 0 if no valid permutations
    return statistics.mean(scores) if scores else 0

# Simulation data
voter_preferences = [3, 1, 2, 3, 2, 1, 3, 3, 2]

# Short-circuit evaluation in assignment
is_diverse = len(set(voter_preferences)) > 1 and max(voter_preferences) <= 5

final_score = 0
if is_diverse:
    final_score = calculate_satisfaction(voter_preferences)
else:
    final_score = -1  # Indicates insufficient diversity

print(f"Result: {final_score}")