import itertools

def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (dead code path)"""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count / len(data)

def transform_sequence(seq):
    """Another decoy transformation with bit manipulation"""
    transformed = []
    for i, s in enumerate(seq):
        if i % 2 == 0:
            # Bitwise distraction
            transformed.append(ord(s) ^ 255)
        else:
            transformed.append(ord(s) << 2)
    return transformed

def compute_entropy(values):
    """Unused entropy calculation to mislead"""
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 6)

def evaluate_performance(metrics, weights):
    # Core logic starts here
    weighted_sum = 0
    adjustment_factor = 0.9
    
    # Simulate performance tiers
    tiers = ['basic', 'intermediate', 'advanced', 'expert']
    tier_multiplier = {'basic': 1.0, 'intermediate': 1.5, 'advanced': 2.2, 'expert': 3.1}
    
    # Irrelevant mapping
    status_flags = {t: False for t in tiers}
    status_flags['expert'] = True  # misleading flag
    
    # Real computation begins
    base_scores = []
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        temp_score = metric * weight
        if i % 3 == 0:
            temp_score += 0.5
        elif i % 3 == 1:
            temp_score -= 0.2
        else:
            temp_score *= 0.95
        base_scores.append(temp_score)
    
    # Distractor: string processing with no effect
    labels = ['A', 'B', 'C', 'D']
    label_data = ''.join(labels)
    rotated = label_data[2:] + label_data[:2]  # unused rotation
    
    # Conditional expression chain
    bonus = 10 if sum(base_scores) > 25 else (5 if sum(base_scores) > 15 else 0)
    
    # Use of enumerate and zip together (required feature)
    for idx, (score, weight) in enumerate(zip(base_scores, weights)):
        if idx > 0 and weights[idx] != weights[idx-1]:
            base_scores[idx] = (base_scores[idx] + base_scores[idx-1]) / 2
    
    # Another red herring: set operations with no impact
    unique_weights = set(weights)
    redundant_set = set(itertools.permutations([1, 2], 2))  # unused
    
    # Key recursive helper (simple recursion)
    def apply_decay(val, depth):
        if depth <= 0 or val < 1:
            return val
        return apply_decay(val * 0.92, depth - 1)
    
    adjusted_scores = [apply_decay(score, 3) for score in base_scores]
    
    # Final aggregation
    raw_total = sum(adjusted_scores)
    
    # Apply tier logic based on raw_total
    performance_tier = 'basic'
    if raw_total > 30:
        performance_tier = 'expert'
    elif raw_total > 20:
        performance_tier = 'advanced'
    elif raw_total > 10:
        performance_tier = 'intermediate'
    
    # This multiplier is critical
    final_score = raw_total * tier_multiplier[performance_tier]
    
    # Dead code: modifying unused variables
    for _ in range(2):
        adjustment_factor **= 0.5  # irrelevant
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data
    metrics = [4.2, 3.8, 5.0, 4.5, 3.9]
    weights = [2.0, 1.8, 2.5, 2.2, 1.9]
    
    # Unused but distracting transformations
    encoded_metrics = transform_sequence('ABCDE')
    efficiency = analyze_efficiency([0.8, 0.6, 0.9, 0.7])
    
    # Critical execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Output result as required
    print(f"Target result: {final_score}")