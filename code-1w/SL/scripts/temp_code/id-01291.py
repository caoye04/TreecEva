from itertools import combinations

def analyze_patterns(values):
    pattern_sum = 0
    temp_result = []
    for i in range(2, len(values) + 1):
        for combo in combinations(values, i):
            if sum(combo) % 3 == 0:
                pattern_sum += len(combo)
    return pattern_sum

def compute_metrics(data):
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    threshold_flag = avg > 15
    dummy_counter = 0
    for val in data:
        if val % 4 == 0:
            dummy_counter += 1
    return avg, variance, threshold_flag

def calculate_final_score(data, thresholds):
    raw_score = 0
    secondary_tally = 0
    
    # Relevant computation: count elements above global threshold
    global_threshold = thresholds['main']
    high_values = [x for x in data if x > global_threshold]
    raw_score += len(high_values) * 2
    
    # Distractor: unused combination analysis
    ignore_combinations = list(combinations(data, 3))
    combination_count = len(ignore_combinations)
    temp_weight = combination_count // 100  # Not used later
    
    # Semi-relevant: use flag from metrics
    _, _, flag = compute_metrics(data)
    if flag:
        raw_score += 5
    
    # Linear search for first value exceeding secondary threshold
    secondary_threshold = thresholds['bonus']
    found = False
    index = 0
    while index < len(data) and not found:
        if data[index] > secondary_threshold:
            secondary_tally += data[index] // 10
            found = True
        index += 1
    
    # Another distractor: complex but irrelevant dictionary transformation
    stats_map = {i: {'val': data[i], 'sq': data[i]**2, 'cube_root': abs(data[i])**(1/3)} for i in range(len(data))}
    unused_total = sum(stats_map[k]['sq'] for k in stats_map if k % 2 == 0)
    
    # Final adjustment using secondary tally
    final_score = raw_score + secondary_tally
    
    # Key statement: final_score assignment
    return final_score

data = [8, 12, 17, 22, 25, 30]
thresholds = {'main': 20, 'bonus': 24}

# Execution point of interest
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")