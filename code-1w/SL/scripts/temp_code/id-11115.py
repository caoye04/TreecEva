from collections import defaultdict, Counter
import math

# Simulated financial transaction analyzer with decoy logic

def analyze_trend(data):
    """Irrelevant trend analysis function (dead code path)"""
    positive = sum(1 for x in data if x > 0)
    negative = sum(1 for x in data if x < 0)
    return 'bullish' if positive > negative else 'bearish'

def dummy_transform(seq):
    """Misleading transformation that isn't used in main logic"""
    return [x ** 2 - x for x in seq if x % 2 == 0]

def validate_checksum(items):
    """Distraction: computes a checksum not used in final result"""
    chk = 0
    for i, v in enumerate(items):
        chk ^= (v + i) * 3
    return chk % 1000

def compute_aggregate(transactions, weights):
    # Core logic embedded within distractions
    weighted_sum = 0.0
    total_weight = 0.0
    temp_store = defaultdict(float)
    
    # Real logic: process each transaction with weight
    for idx, (t, w) in enumerate(zip(transactions, weights)):
        if w <= 0:  # Valid guard, part of real logic
            continue
        adjusted = t * (1.0 + math.sin(idx))  # Minor adjustment based on position
        temp_store[idx] = adjusted
        weighted_sum += adjusted * w
        total_weight += w
    
    # Distractor: unused counter over indices
    index_counter = Counter(temp_store.keys())
    avg_index = sum(index_counter.elements()) / len(index_counter) if index_counter else 0
    
    # Decoy intermediate calculation (never used)
    peak_value = max(temp_store.values(), default=0)
    normalized_peak = peak_value / (weighted_sum / total_weight) if weighted_sum != 0 else 0
    
    # Another red herring: bit manipulation on sum components
    bitwise_fuse = 0
    for val in temp_store.values():
        intval = int(abs(val))
        bitwise_fuse ^= (intval & 255) << 1
    
    # Actual answer computation
    raw_average = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Secondary adjustment using only first and last valid index
    valid_indices = [i for i, w in enumerate(weights) if w > 0]
    index_span_factor = (valid_indices[-1] - valid_indices[0]) if len(valid_indices) > 1 else 1
    
    enhanced_result = raw_average * (1 + 0.1 * math.log(index_span_factor + 1))
    
    # Final nonlinear transformation (key step)
    final_score = int(enhanced_result * 100) / 100.0  # Round to nearest cent
    
    # Dead code: string manipulation unrelated to logic
    status_msg = "Processing Complete"
    status_msg = status_msg.lower().replace(' ', '_')
    
    return final_score

# Irrelevant dataset preparation
historical_data = [127, -53, 201, 88, -92, 145]
dummy_weights = [1.0, 0.5, 2.0, 1.5, 0.0, 3.0]

# Checksum distraction (computed but not used)
_ = validate_checksum(historical_data)

# Unused transformation
_ = dummy_transform(list(range(6)))

# Real input data
transactions = [150, -75, 200, 120, -60, 300]
weights = [2.0, 1.0, 3.0, 2.5, 1.5, 4.0]

# Key execution point
final_score = compute_aggregate(transactions, weights)

# Output the target result
print(f"Result: {final_score}")