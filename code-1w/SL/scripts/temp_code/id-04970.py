def evaluate_stability(data, config):
    # Irrelevant function - dead code path
    temp = [x ** 2 for x in data if x < 5]
    result = sum(temp) // len(temp) if temp else 0
    return result * config.get('scale', 1)

lambda_filter = lambda seq, limit: [i for i in seq if i % limit == 0]

# Misleading intermediate variables
counter_observations = [3, 7, 2, 8, 5, 9, 1, 6, 4]
raw_readings = counter_observations[::-1]  # Slicing red herring

# Distractor data structures
diagnostics = {
    'errors': [0, 1, 1, 0, 1],
    'checksum': 23,
    'history': [(1, 'pass'), (2, 'fail')]
}

# Unused complex transformation
def transform_series(series):
    shifted = [series[i] ^ series[(i+1)%len(series)] for i in range(len(series))]
    return [x & 7 for x in shifted]

# Real computation begins here
metrics = [77, 82, 91, 65, 88, 73, 90]

# Multiple simultaneous assignments - relevant and irrelevant
baseline, offset, _ = (60, 10, 5)  # Unpacked values; only two are used

thresholds = {
    'min_pass': baseline,
    'boost_level': offset + 5,
    'decay_factor': 0.9
}

status_flags = [True, False, True, True]
flag_summary = any(status_flags) and not all(status_flags)  # Complex boolean distractor

# Core logic hidden among distractions
def analyze_performance(measures, criteria):
    # Nesting level 1
    if not measures:
        return 0
    
    passing = []
    bonus_eligible = False
    
    # Nesting level 2
    for score in measures:
        # Nesting level 3
        if score >= criteria['min_pass']:
            adjusted = score
            
            # Nested conditional - real logic branch
            if score > 85:
                # Accumulation with conditional modification
                adjusted += offset  # Uses variable from unpacking
                
                # Introduce summation and accumulation
                running_total = sum(measures[:measures.index(score)+1])
                if running_total > 300:
                    bonus_eligible = True
            
            passing.append(adjusted)
    
    # Real answer depends on this computation
    base_score = sum(passing)
    
    # Red herring: complex-looking but unused calculation
    decoy_result = sum([x**2 for x in measures if x in lambda_filter(measures, 3)])
    
    # Final decision logic with short-circuit evaluation
    final_modifier = 2 if bonus_eligible and len(passing) > 4 else 1
    
    # Critical assignment - answer determined here
    return base_score * final_modifier

# Simulate diagnostic call - irrelevant to final result
evaluate_stability([1,2,3], {'scale': 2})

# Key execution point
final_score = analyze_performance(metrics, thresholds)

# Output required format
print(f"Result: {final_score}")