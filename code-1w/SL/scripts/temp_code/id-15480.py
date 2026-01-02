def analyze_metrics(data, threshold=0.75):
    """
    Analyzes performance metrics from a simulation.
    This function is NOT directly related to final_score but included as distraction.
    """
    high_performers = []
    avg_latency = sum(data['latency']) / len(data['latency']) if data['latency'] else 0
    for i, val in enumerate(data['accuracy']):
        if val > threshold:
            high_performers.append((i, val))
    return {'count': len(high_performers), 'avg_latency': avg_latency}


def compute_weighted_rankings(items):
    """Computes rankings with irrelevant weighting scheme."""
    weights = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0]
    adjusted = []
    for idx, (item, weight) in enumerate(zip(items, weights * (len(items)//6 + 1))):
        adjusted.append(item * weight + idx % 3)
    return sum(adjusted) // len(adjusted)

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True
TEMP_FACTOR = -999  # Red herring used nowhere important

# Simulated assessment data with mixed types and red herrings
assessment_data = {
    'raw_scores': [88, 92, 76, 85, 94, 81],
    'weights': [0.2, 0.3, 0.1, 0.15, 0.2, 0.05],
    'penalties': [5, 0, 10, 0, 0, 3],
    'bonus_flags': [True, False, True, False, True, False],
    'meta_sequence': [1, 1, 2, 3, 5, 8],  # Fibonacci-like distraction
    'timestamps': [1634567890, 1634567902, 1634567915, 1634567920, 1634567931, 1634567945]
}

# Unused recursive function to mislead about complexity requirements
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Decoy data structure
shadow_copy = {k: v[::-1] if isinstance(v, list) else v for k, v in assessment_data.items()}

# Key processing function that actually determines final_score
def process_results(data):
    weighted_total = 0.0
    bonus_applied = 0
    
    # Primary calculation loop with meaningful nesting
    for i, score in enumerate(data['raw_scores']):
        adjusted = score - data['penalties'][i]
        
        # Conditional bonus logic (only every other flagged entry gets bonus)
        if data['bonus_flags'][i]:
            if i % 2 == 0:
                adjusted += 4
                bonus_applied += 1
        
        # Apply weight based on position
        weighted_total += adjusted * data['weights'][i]
        
        # Nested conditional with bit manipulation decoy
        if adjusted > 85:
            temp_flag = (i << 2) | 1  # Bitwise op with no real impact
            if temp_flag & 1:
                pass  # Dead code branch
    
    # Secondary adjustment using zip to align scores and weights again
    corrections = []
    for raw, w in zip(data['raw_scores'], data['weights']):
        if raw >= 90:
            corrections.append(w * 3)
    
    # Final aggregation
    aggregate_correction = sum(corrections)
    base_result = weighted_total + aggregate_correction
    
    # Tie-breaking rule based on bonus count (critical step)
    if bonus_applied >= 2:
        base_result += 2.5
    
    # Distractor: unused transformation
    normalized = [x / max(data['raw_scores']) for x in data['raw_scores']]
    
    # The actual answer derivation
    final_score = int(round(base_result * 1.07))  # Final scaling
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Misleading pre-execution analysis
prelim_analysis = analyze_metrics({
    'latency': [20, 35, 28, 40, 33],
    'accuracy': [0.81, 0.93, 0.77, 0.88, 0.91]
})

# Execute the key statement
final_score = process_results(assessment_data)