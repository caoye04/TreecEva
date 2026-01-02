def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    magnitude = sum([abs(x) for x in filtered])
    return magnitude if magnitude > 10 else 0

samples = [0.1, -0.8, 1.3, -2.1, 0.4, 1.7, -3.2, 0.9]
signal_strength = analyze_signal(samples)

# Irrelevant transformation chain (distractor)
def transform_grid(grid):
    rotated = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    flattened = [item for row in rotated for item in row]
    normalized = [x / max(flattened) for x in flattened]
    return normalized

game_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transformed = transform_grid(game_grid)

# Unused function - red herring
def compute_entropy(sequence):
    from math import log
    freq = {}
    for s in sequence:
        freq[s] = freq.get(s, 0) + 1
    total = len(sequence)
    entropy = -sum((count/total) * log(count/total) for count in freq.values())
    return entropy

# Boolean logic and control flow with decoy variables
is_active = True
temp_flag = False
status_code = 200 if signal_strength > 5 else 404

if status_code == 200 and is_active:
    temp_flag = True

# Data structure manipulation (sets and lists)
available_ids = {101, 102, 103, 104, 105}
pending_ids = {103, 104, 106, 107}
conflict_ids = available_ids & pending_ids  # intersection

resolved_ids = {x for x in conflict_ids if x % 2 == 1}  # set comprehension

# Weighted scoring logic (actual relevant path)
data = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

# Misleading intermediate calculation
temp_sum = sum([a * w**2 for a, w in zip(data, weights)])  # irrelevant squared weights

# Core processing function (key logic)
def process_metrics(values, weight_vector):
    if len(values) != len(weight_vector):
        return -1
    weighted_total = sum(v * w for v, w in zip(values, weight_vector))
    adjustment = 0.0
    
    # Conditional correction based on signal strength (real dependency)
    if signal_strength > 0:
        adjustment += 5.0
    
    # Nested condition with dummy check
    if len(resolved_ids) > 0 and temp_flag:
        adjustment += 2.0  # never reached due to temp_flag
    
    # Final computation
    result = weighted_total + adjustment
    
    # String-based switch (distraction)
    mode = 'standard'
    if 'debug' in mode.upper().lower():
        result *= 0.9
        
    return result

# Critical execution point
final_score = process_metrics(data, weights)

# Output requirement
print(f"Result: {final_score}")