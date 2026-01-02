def analyze_pattern(seq):
    """Irrelevant analysis function - distractor"""
    count = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and i % 3 == 0:
            count += 1
    return count * 2

# Misleading data structures
temp_log = [1, 3, 5, 7, 9]
dummy_weights = [0.1, 0.1, 0.1, 0.1, 0.1]
offset_table = {i: i*3 for i in range(10)}

# Actual problem context: Academic ranking system with weighted scoring
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
raw_scores = [88, 92, 76, 94, 85]
participation = [4, 5, 3, 5, 4]
attendance = [95, 98, 88, 100, 92]

# Irrelevant transformation
transformed = []
for idx, val in enumerate(raw_scores):
    transformed.append(val + (idx % 4))

# Decoy processing
buffer_data = []
for s in students:
    buffer_data.append({"name": s, "code": hash(s) % 100})

# Real computation begins: normalize scores to ranking positions
sorted_indices = sorted(range(len(raw_scores)), key=lambda i: raw_scores[i], reverse=True)
rankings = [0] * len(raw_scores)
for rank, idx in enumerate(sorted_indices):
    rankings[idx] = rank + 1

# Secondary metric: participation bonus mapping
bonus_map = {}
for i, p in enumerate(participation):
    bonus_map[i] = max(0, min(10, p * 2))

# Weight configuration (some weights are red herrings)
weights = {
    'performance': 0.6,
    'engagement': 0.3,
    'appearance': 0.1,  # decoy weight - not used
    'punctuality': 0.0   # dead weight - misleading
}

# Unused function simulating alternate logic path
def legacy_scoring(data):
    result = 0
    for x in data:
        result ^= int(x / 2)
    return result

# Another distraction: character frequency analysis on names
char_freq = {}
for name in students:
    for c in name.lower():
        char_freq[c] = char_freq.get(c, 0) + 1
rare_chars = [c for c, cnt in char_freq.items() if cnt == 1]

# Core algorithm: combine rankings and valid weights only
valid_weight_sum = weights['performance'] + weights['engagement']
adjusted_weights = {
    'performance': weights['performance'] / valid_weight_sum,
    'engagement': weights['engagement'] / valid_weight_sum
}

# Processing function that computes final score
def process_results(ranks, w):
    base_score = 0.0
    adjustment = 0.0
    
    # Map ranking to performance points (inverse relationship)
    performance_points = []
    for r in ranks:
        performance_points.append(100 - (r - 1) * 5)
    
    # Use enumerate and zip as required
    for i, (pt, part) in enumerate(zip(performance_points, participation)):
        contribution = pt * w['performance'] + bonus_map[i] * w['engagement']
        if i % 2 == 0:
            adjustment += 1.5  # minor correction factor
        base_score += contribution
    
    # Apply attendance multiplier only for top-ranked student
    top_idx = sorted_indices[0]
    attendance_factor = max(1.0, min(1.2, attendance[top_idx] / 100))
    
    # Final computation
    final = (base_score / len(students)) * attendance_factor + adjustment
    
    # Dead code branch - never executed but looks important
    if len(rare_chars) > 10:
        final -= hash(''.join(students)) % 5
        
    return final

# Execute main logic
final_score = process_results(rankings, weights)

# Print result as required
print(f"Target result: {final_score}")