from itertools import combinations
from functools import reduce

# Simulate a ranked voting system with weighted preferences
votes = [
    ['A', 'B', 'C', 'D'],
    ['B', 'C', 'A', 'D'],
    ['C', 'B', 'D', 'A'],
    ['B', 'A', 'C', 'D']
]

# Weight assigned to each rank position (first, second, etc.)
weights = [5, 3, 2, 1]

# Tally raw points based on rank positions
rankings = {candidate: 0 for candidate in 'ABCD'}
for ballot in votes:
    for idx, candidate in enumerate(ballot):
        rankings[candidate] += weights[idx]

# Irrelevant distraction: compute pairwise comparison counts (not used later)
pairwise_counts = {}
for a, b in combinations('ABCD', 2):
    a_beats_b = 0
    for ballot in votes:
        if ballot.index(a) < ballot.index(b):
            a_beats_b += 1
    pairwise_counts[(a, b)] = a_beats_b

# Another distraction: simulate redundant normalization
normalized_ranks = {k: round(v / sum(rankings.values()) * 100, 2) for k, v in rankings.items()}

# Dummy state tracking that doesn't affect outcome
current_leader = max(rankings, key=rankings.get)
leader_points = rankings[current_leader]

# Function uses lambda and higher-order reduction
compute_weighted_sum = lambda vals, w: reduce(lambda acc, i: acc + vals[i] * w[i], range(len(vals)), 0)

def calculate_final_score(ranks, w):
    # Apply transformation: boost candidates with prime-numbered scores
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    boosted = {}
    for k, v in ranks.items():
        boost_factor = 1.5 if is_prime(int(v)) else 1.0
        boosted[k] = v * boost_factor

    # Secondary distraction: count how many received a boost
    boosted_count = sum(1 for x in boosted.values() if x != ranks[list(boosted.keys())[list(boosted.values()).index(x)]])

    # Final score is the difference between highest and lowest boosted score
    return int(max(boosted.values()) - min(boosted.values()))

# Critical execution point
final_score = calculate_final_score(rankings, weights)

# Additional red herring: unused aggregation using itertools
all_triplets = list(combinations([v for v in rankings.values()], 3))
triplet_sums = [sum(t) for t in all_triplets]
median_sum = sorted(triplet_sums)[len(triplet_sums)//2] if triplet_sums else 0

print(f"Result: {final_score}")