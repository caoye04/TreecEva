def analyze_pattern(sequence, threshold):
    count = 0
    temp_sum = 0
    pattern_detected = False
    
    for i in range(len(sequence) - 1):
        diff = abs(sequence[i + 1] - sequence[i])
        temp_sum += diff
        if diff > threshold:
            count += 1
            if diff % 3 == 0:
                pattern_detected = True

    average_change = temp_sum / (len(sequence) - 1) if sequence else 0
    return count, average_change, pattern_detected


def evaluate_stability(readings):
    stable_count = 0
    total_variance = 0.0
    for reading in readings:
        variance = sum((x - sum(reading)/len(reading))**2 for x in reading)
        total_variance += variance
        if variance < 50:
            stable_count += 1
    return stable_count


def process_results(data):
    # Irrelevant tracking variables (distractors)
    debug_log = {}
    cumulative_shift = 0
    snapshot_history = []
    
    base_score = 0
    penalty_adjustment = 0
    
    for entry in data:
        phase_id = entry['phase']
        values = entry['metrics']
        
        # Real logic begins
        if phase_id % 2 == 0:
            offset = 5
        else:
            offset = 3
        
        count, avg_change, detected = analyze_pattern(values, threshold=10)
        
        # Semi-relevant transformation
        transformed = [(v * 2 + offset) % 25 for v in values]
        
        # Distractor: unused computation
        squared_chain = [x**2 for x in transformed if x > 10]
        snapshot_history.append(squared_chain)
        
        # Key scoring logic
        if avg_change > 8:
            base_score += 15
        elif detected:
            base_score += 8
        
        # Conditional expression used
        penalty_factor = 4 if count > 2 else 2
        penalty_adjustment += penalty_factor
        
        # Dictionary operation
        debug_log[f'phase_{phase_id}'] = {
            'count': count,
            'penalty': penalty_factor,
            'not_used': sum(transformed) // len(transformed)
        }
    
    # Final calculation with interdependent components
    final_score = base_score - (penalty_adjustment // 2)
    
    # Additional misleading but irrelevant calculation
    aggregate_trace = sum([len(log['not_used'].__str__()) for log in debug_log.values()])
    cumulative_shift += aggregate_trace % 100
    
    return final_score

# Simulated assessment data
assessment_data = [
    {'phase': 1, 'metrics': [12, 15, 9, 20, 18]},
    {'phase': 2, 'metrics': [5, 18, 33, 14, 6]},
    {'phase': 3, 'metrics': [10, 11, 13, 16, 25]},
    {'phase': 4, 'metrics': [8, 22, 35, 19, 7]}
]

# Evaluate stability (unused result - red herring)
evaluate_stability([[10,12,11], [9,10,11], [25,26,24]])

final_score = process_results(assessment_data)
print(f"Target result: {final_score}")