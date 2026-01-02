def analyze_sequence(data):
    # Irrelevant transformation: bit manipulation with no impact
    masked = [x ^ 0b1010 for x in data]
    shifted = [(x << 2) & 255 for x in masked]
    return [x for x in shifted if x > 50]  # Unused result

def preprocess_inputs(raw):
    # Distractor function: processes but never used
    cleaned = [r.strip().lower() for r in raw if r]
    parts = [c.split(',') for c in cleaned]
    flattened = [item for sublist in parts for item in sublist]
    as_ints = [int(f) if f.isdigit() else 0 for f in flattened]
    return as_ints[::-1]  # Never called

def calculate_baseline(values, offset=3):
    # Seemingly important but unused baseline logic
    base = sum(values) / len(values)
    adjusted = [v - base + offset for v in values]
    return [round(a * 1.05, 2) for a in adjusted]

def compute_rankings(entries):
    # Red herring ranking system
    sorted_entries = sorted(entries, reverse=True)
    ranks = {val: idx + 1 for idx, val in enumerate(sorted_entries)}
    normalized = {k: round(v / len(entries), 3) for k, v in ranks.items()}
    return normalized  # Not used

def evaluate_performance(metrics, weights):
    # Core relevant logic starts here
    weighted_sum = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            weighted_sum += metrics[i] * weights[i]
        else:
            weighted_sum += metrics[i] + weights[i]  # Different operation on odd indices
    
    # Apply non-linear adjustment using lambda
    adjuster = lambda x: x ** 0.5 if x > 0 else 0
    adjusted_sum = adjuster(weighted_sum * 2)
    
    # Use slicing to extract mid-section for secondary check (distractor)
    segment = metrics[1:-1]
    bonus = sum(segment) * 0.1 if len(segment) > 2 else 0  # Minor bonus
    
    # Final computation
    final_score = int(adjusted_sum + bonus)
    
    # Dead code path: unreachable due to structure
    if False:
        fallback = sum(weights) * 10
        final_score = fallback
    
    return final_score

# Main execution
raw_data = ['10,20', '30', '', '40,50']
data_stream = [7, 14, 21, 28]

# Irrelevant preprocessing calls (never assigned)
calculate_baseline(data_stream)
analyze_sequence(data_stream)

# Key data structures
metrics = [85, 72, 90, 61, 77]
weights = [0.2, 0.4, 0.3, 0.5, 0.1]

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")