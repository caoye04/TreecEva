def analyze_text(s):
    return s.lower().count('e'), len(s.split())

# Irrelevant helper function (decoy)
def validate_input(x):
    if isinstance(x, str):
        return sum(ord(c) for c in x) % 7 == 0
    return False

# Unused transformation chain
def transform_values(vals):
    temp = [v * 1.5 for v in vals if v > 0]
    return sorted(temp, reverse=True)

# Core logic disguised among distractors
def compute_metric(a, b, op='xor'):
    if op == 'xor':
        return a ^ b
    elif op == 'and':
        return a & b
    return 0

def extract_features(texts):
    result = []
    for t in texts:
        e_count, word_count = analyze_text(t)
        # Distractor computation
        noise = (e_count + word_count) % 3
        if noise > 1:
            _ = [i**2 for i in range(3)]  # Dead code path
        result.append(e_count * 2 + word_count)
    return result

def merge_dicts(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = merged.get(k, 0) + v
    return merged

# Misleading data initialization
dummy_logs = [
    "Error: failed to connect",
    "Warning: low memory",
    "Info: system online"
]

# Never called function (red herring)
def audit_sequence(seq):
    total = 0
    for i, val in enumerate(seq):
        total += val << i
    return total % 1000

# Main processing with hidden signal
def process_results(data, weights):
    # Step 1: Extract text features
    features = extract_features(data)
    
    # Step 2: Create frequency map (set usage via keys)
    freq_map = {}
    for word in ' '.join(data).split():
        clean = word.strip('.,!').lower()
        freq_map[clean] = freq_map.get(clean, 0) + 1
    
    # Step 3: Compute weighted sum
    weighted_sum = sum(f * w for f, w in zip(features, weights))
    
    # Step 4: Apply bit manipulation on aggregate stats
    total_length = sum(len(s) for s in data)
    unique_words = len(set(freq_map.keys()))
    
    # Critical intermediate calculation
    magic_factor = compute_metric(total_length, unique_words, 'xor')
    
    # Step 5: Use dictionary operations to derive adjustment
    profile = {"size": total_length, "diversity": unique_words}
    adjustment = 0
    if profile["size"] > 50 and profile["diversity"] > 10:
        adjustment = 5
    
    # Step 6: Incorporate string method side-effect
    combined = ''.join(data).upper()
    bonus = len([c for c in combined if c in 'AEIOU']) // 4  # Hidden contribution
    
    # Final composition (answer built from multiple reasoning steps)
    base_score = weighted_sum + magic_factor + adjustment
    final_score = base_score + bonus
    
    # Irrelevant cleanup
    temp_files = [f"tmp_{i}" for i in range(len(data))]
    del temp_files  # Meaningless operation
    
    return final_score

# Actual input data driving the result
data = [
    "The neural network processes complex patterns efficiently.",
    "Machine learning models require large datasets for training.",
    "Deep architectures improve representation learning capabilities."
]

weights = [1.2, 0.8, 1.0]

# Execution point of interest
final_score = process_results(data, weights)
print(f"Result: {final_score}")