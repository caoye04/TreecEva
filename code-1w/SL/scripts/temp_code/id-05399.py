from itertools import permutations

def analyze_patterns(sequence):
    # Distractor function – not used in final computation
    counts = {}
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        counts[pair] = counts.get(pair, 0) + 1
    return sum(counts.values())

# Simulated sensor readings with noise
sensor_data = [12, 15, 10, 8, 20, 14]
filtered_readings = [x for x in sensor_data if x > 10]
noise_offset = sum([x % 3 for x in sensor_data])  # Irrelevant computation

# Candidate rankings from three evaluators
rankings = [
    ['A', 'B', 'C', 'D'],
    ['B', 'A', 'D', 'C'],
    ['A', 'D', 'B', 'C']
]

# Weight configuration for aggregation (more weight on earlier evaluators)
weights = [0.5, 0.3, 0.2]

# Precompute position maps
position_maps = []
for ranking in rankings:
    pos_map = {candidate: idx for idx, candidate in enumerate(ranking)}
    position_maps.append(pos_map)

# Candidate pool
candidates = ['A', 'B', 'C', 'D']

# Initialize scores
raw_scores = {c: 0.0 for c in candidates}

# Accumulate weighted rank positions
for i, weight in enumerate(weights):
    for candidate in candidates:
        raw_scores[candidate] += weight * (3 - position_maps[i][candidate])  # Higher score for higher rank

# Normalize scores to prevent overflow (distractor normalization)
norm_factor = sum(raw_scores.values()) / len(candidates)
normalized_scores = {c: raw_scores[c] / norm_factor for c in candidates}

# Apply non-linear boost based on consistency across evaluators
consistency_bonus = {c: 0 for c in candidates}
for candidate in candidates:
    positions = [position_maps[i][candidate] for i in range(len(rankings))]
    variance = sum((p - sum(positions)/len(positions))**2 for p in positions) / len(positions)
    consistency_bonus[candidate] = 1.0 / (1 + variance)  # Bonus for low variance

# Compute preliminary adjusted score
preliminary_scores = {c: normalized_scores[c] + consistency_bonus[c] for c in candidates}

# Determine top candidate by preliminary score
sorted_candidates = sorted(preliminary_scores.keys(), key=lambda x: preliminary_scores[x], reverse=True)
top_candidate = sorted_candidates[0]

# Calculate final score using original raw scores with bonus
final_raw = raw_scores[top_candidate]
bonus_applied = consistency_bonus[top_candidate]

# Final aggregation function
def calculate_final_score(rankings, weights):
    base = 0
    for i, w in enumerate(weights):
        winner = rankings[i][0]  # First in each ranking
        impact = (ord(winner) - ord('A')) * w
        base += impact
    # Additional logic based on top performer's average rank
    avg_rank = sum(position_maps[i][top_candidate] for i in range(len(rankings))) / len(rankings)
    adjustment = 10 * (3 - avg_rank)  # Better rank -> higher adjustment
    return round(final_raw + bonus_applied + adjustment, 4)

# Execute final computation
final_score = calculate_final_score(rankings, weights)

# Print result as required
print(f"Target result: {final_score}")