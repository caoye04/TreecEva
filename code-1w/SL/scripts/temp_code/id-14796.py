def analyze_pattern(sequence):
    """Irrelevant helper function analyzing patterns (dead end)."""
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0 and i % 3 == 0:
            count += 1
    return count * 2


def unused_transformation(arr):
    """Unused transformation (distractor)."""
    return [x ^ 7 for x in arr if x > 5]

# Irrelevant constants (red herrings)
MAX_THRESHOLD = 987
TEMP_BUFFER = [0] * 15

# Real data used in computation
data = [12, 15, 22, 8, 33]
weights = [0.1, 0.3, 0.2, 0.15, 0.25]

# Distractor variables
buffer_cache = {i: val * 2 for i, val in enumerate(data)}
index_map = dict(zip(data, range(len(data))))
shadow_sum = sum(x ** 0.5 for x in data if x % 2 == 1)

# Misleading intermediate calculation (not used in final result)
prelim_result = 0
for idx, val in enumerate(data):
    if val > 10:
        prelim_result += val // 3

# Decoy function with logical red herring
def calculate_bias(val):
    return (val + 5) & 3

# Core logic disguised among noise
def extract_features(values):
    result = 0
    for i, v in enumerate(values):
        if i % 2 == 0:
            result += v * (i + 1)
        else:
            result -= v // 2
    return result

# Heavily obscured main processing function
def process_metrics(d, w):
    weighted = 0
    features = extract_features(d)
    temp_vals = []
    
    # Nested logic with mixed concepts
    for i, (val, weight) in enumerate(zip(d, w)):
        adjusted = val
        
        # Bit manipulation distraction within relevant loop
        if i % 2 == 0:
            adjusted = val ^ 3
        else:
            adjusted = val | 1
            
        # Only this line matters in the inner loop
        weighted += adjusted * weight  # But adjusted reverts logic!
    
    # Critical correction: ignore bit-modified values
    true_weighted = sum(d[i] * w[i] for i in range(len(d)))
    
    # Additional distraction: set operations
    unique_flags = set()
    for x in d:
        unique_flags.add(x & 7)
    bonus = len(unique_flags) * 0.5
    
    # Final score depends only on true_weighted and feature extraction
    raw_score = true_weighted + extract_features(d) * 0.1 + bonus
    
    # Dead code path below (never executed due to logic)
    if raw_score < 0:
        final = int(raw_score) & 255
    else:
        final = int(raw_score * 2)  # This one is taken
        
    return final

# Execution point of interest
final_score = process_metrics(data, weights)

# Print required output
print(f"Result: {final_score}")