def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def smooth_data(arr):
    if not arr:
        return []
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        smoothed.append((arr[i-1] + arr[i] + arr[i+1]) / 3)
    smoothed.append(arr[-1])
    return smoothed

# Unused transformation (dead code path)
def transform_scale(val, exp=2):
    base = val % 7
    shift = base ** exp
    return (shift * 10) // 3 + 1

# Misleading intermediate calculation
def compute_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# String-based distractor processing
def validate_code(token: str) -> bool:
    if not token.isalnum() or len(token) != 8:
        return False
    upper_count = sum(1 for c in token if c.isupper())
    digit_count = sum(1 for c in token if c.isdigit())
    return upper_count >= 2 and digit_count >= 2

# Heavily distracted but correct core logic
def process_results(raw_data, importance_weights):
    # Distractor: string preprocessing with no impact
    tag = "DXR-90210"
    if tag.startswith("DX") and tag.endswith("10"):
        tag_valid = True
        version_code = tag.lower().replace("dxr", "core").strip("-")  # unused
    
    # Core data filtering (relevant)
    filtered = [x for x in raw_data if x >= 0]
    
    # Irrelevant normalization attempt
    max_val = max(filtered) if filtered else 1
    normalized = [round(x / max_val, 5) for x in filtered] if max_val != 0 else filtered
    
    # Real computation begins here
    adjusted = []
    for i, val in enumerate(filtered):
        weight = importance_weights[i % len(importance_weights)]
        temp_score = val * weight
        if temp_score > 50:
            temp_score = 50 + (temp_score - 50) * 0.5  # diminishing returns
        adjusted.append(temp_score)
    
    # Secondary adjustment based on pattern analysis
    trend_boost = analyze_pattern(adjusted) * 3.5
    
    # Another misleading metric (not used in final score)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    peak_index = -1
    for idx, val in enumerate(adjusted):
        if val == max(adjusted):
            peak_index = idx
            break
    
    # Red herring: complex bit manipulation with no effect
    decoy_state = 0b101010
    for x in adjusted:
        if x > 10:
            decoy_state ^= int(x) & 0b1111
    decoy_state = (decoy_state << 2) | (decoy_state >> 6)
    
    # Final aggregation (key step)
    base_total = sum(adjusted)
    penalty = 0
    if len(filtered) != len(raw_data):
        penalty = (len(raw_data) - len(filtered)) * 2.75
    
    # Actual answer computation
    final_score = base_total + trend_boost - penalty
    
    # Dead return branch (never reached due to unconditional below)
    # if final_score < 0: return 0  
    
    return final_score  # This is the real output

# Global irrelevant constants
data_snapshot = "2023-Q4"
config_mode = data_snapshot.split("-")[0].upper() if "-" in data_snapshot else "UNK"

# Input data
measurements = [12, -5, 23, 67, 45, -3, 18, 91, 15]
weights = [1.2, 0.8, 1.5]

# Trigger execution
result_cache = {}
input_hash = hash(str(measurements) + str(weights))
if input_hash not in result_cache:
    processed = process_results(measurements, weights)
    result_cache[input_hash] = processed

final_score = result_cache[input_hash]

# Print result as required
print(f"Target result: {final_score}")