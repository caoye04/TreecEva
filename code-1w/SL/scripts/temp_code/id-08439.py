from itertools import combinations, cycle

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: analyze oscillations (not used in final result)
    oscillations = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1] and trend[j] != 0:
            oscillations += 1

    # Relevant computation: sum of positive trends
    positive_trend_sum = sum(1 for t in trend if t == 1)
    return positive_trend_sum

def extract_features(raw_data):
    normalized = [x % 17 for x in raw_data if x > 0]  # Some filtering and mod
    shifted = [n << 1 for n in normalized]  # Bit shift distraction
    squared_residuals = [(n - 5)**2 for n in normalized]  # Unused metric
    base_energy = sum(normalized) / len(normalized) if normalized else 0
    return base_energy

def calculate_final_score(stream):
    chunk_size = 4
    scores = []n    temp_buffer = []
    debug_stats = {}  # Unused tracking
    
    # Simulate sliding window processing
    for idx in range(0, len(stream) - chunk_size + 1, 2):
        window = stream[idx:idx + chunk_size]
        
        # Real signal: detect increasing triplets
        increasing_triplets = 0
        for i in range(len(window) - 2):
            if window[i] < window[i+1] < window[i+2]:
                increasing_triplets += 1
        
        # Distractor: compute all pairs (never used)
        _ = list(combinations(window, 2))
        
        # Energy feature extraction
        energy = extract_features(window)
        pattern_strength = analyze_pattern(window)
        
        # Core scoring logic
        window_score = energy + pattern_strength * 2
        if increasing_triplets >= 1:
            window_score *= 1.5  # Boost if triplet detected
        
        scores.append(window_score)
        
        # Dead code branch: only triggers on impossible condition
        if len(scores) > 100 and False:
            reset_flag = True

    # Final aggregation
    raw_total = sum(scores)
    penalty = len(scores) * 0.1
    final_score = int(raw_total - penalty) if raw_total > penalty else 0
    
    # Auxiliary irrelevant cycle
    cycling_weights = cycle([1, -1])
    for _ in range(len(scores)):
        next(cycling_weights)
    
    return final_score

# Main execution
sensor_readings = [12, 3, 7, 9, 4, 6, 8, 11, 2, 5, 10, 13]
data_stream = sensor_readings + [x * 2 for x in sensor_readings[:3]]
intermediate_metric = sum(x ** 0.5 for x in data_stream if x % 2 == 0)  # Red herring calc

final_score = calculate_final_score(data_stream)
print(f"Result: {final_score}")