from collections import defaultdict

# Simulate a ranked voting system with weighted preferences
votes = [
    ['Alice', 'Bob', 'Charlie'],
    ['Bob', 'Charlie', 'Alice'],
    ['Alice', 'Charlie', 'Bob'],
    ['Charlie', 'Bob', 'Alice'],
    ['Bob', 'Alice', 'Charlie']
]

weights = {'first': 3, 'second': 2, 'third': 1}
distraction_matrix = [[i * j for j in range(3)] for i in range(3)]
offset_map = defaultdict(lambda: 5)
offset_map['Alice'] = 3
offset_map['Bob'] = 4
offset_map['Charlie'] = 2

# Irrelevant accumulation (distractor)
counter_distractor = 0
for i in range(len(votes)):
    for j in range(len(votes[i])):
        counter_distractor += (i + j) % 2

# Precompute position-based scores using lambda
scoring_rule = lambda pos: weights[['first', 'second', 'third'][pos]]

rankings = defaultdict(int)

# Accumulate scores based on rankings
for ballot in votes:
    for idx, candidate in enumerate(ballot):
        rankings[candidate] += scoring_rule(idx)

# Another distractor: unused helper function
def analyze_pattern(seq):
    return sum(1 for a, b in zip(seq, seq[1:]) if a != b)

# More distraction: fake normalization
fake_norm_factor = sum(offset_map.values()) / len(offset_map)
adjusted_scores = {k: v - fake_norm_factor for k, v in rankings.items()}

# Final score calculation — this is where the answer is determined
def calculate_final_score(ranking_dict, weight_dict):
    base_total = sum(ranking_dict.values())
    bonus = 0
    for name, score in ranking_dict.items():
        if score >= 7:
            bonus += offset_map[name]
    return int(base_total * 1.1 + bonus)

total_score = calculate_final_score(rankings, weights)
print(f"Result: {total_score}")