from collections import defaultdict

# Simulate a ranked voting system with weighted preferences
votes = [
    ['A', 'B', 'C'],
    ['B', 'C', 'A'],
    ['C', 'A', 'B'],
    ['A', 'C', 'B'],
    ['B', 'A', 'C']
]

# Weight assigned to each rank position (1st, 2nd, 3rd)
weights = [3, 2, 1]

# Tally votes by candidate using defaultdict for convenience
tally = defaultdict(int)
rankings = defaultdict(list)

# Accumulate raw vote counts per candidate (irrelevant distractor for final score)
for ballot in votes:
    for i, candidate in enumerate(ballot):
        tally[candidate] += 1

# Record which positions each candidate appeared in (used later)
for ballot in votes:
    for i, candidate in enumerate(ballot):
        rankings[candidate].append(i)

# Misleading intermediate: compute average rank (not used in final formula)
avg_ranks = {}
for candidate, ranks in rankings.items():
    avg_ranks[candidate] = sum(ranks) / len(ranks)

# Compute total weighted score based on frequency of appearance in each rank
weighted_sum = defaultdict(float)
for candidate, ranks in rankings.items():
    for rank in ranks:
        if rank < len(weights):
            weighted_sum[candidate] += weights[rank]

# Secondary distraction: normalize scores between 0-1 (not used)
max_weight = max(weighted_sum.values()) if weighted_sum else 1
normalized = {c: s / max_weight for c, s in weighted_sum.items()}

# Another red herring: simulate tie-breaker margin (unused)
tie_breaker = abs(weighted_sum['A'] - weighted_sum['B']) * 0.5

# Core logic: final score is total weight of candidate 'A' plus bonus for being top-ranked at least twice
top_rank_count = rankings['A'].count(0)
bonus = 5 if top_rank_count >= 2 else 0

# Critical statement
final_score = weighted_sum['A'] + bonus

print(f"Result: {final_score}")