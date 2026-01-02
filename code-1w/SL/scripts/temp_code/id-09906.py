def analyze_performance(metrics):
    trend = []
    for i in range(1, len(metrics)):
        if metrics[i] > metrics[i-1]:
            trend.append(1)
        elif metrics[i] < metrics[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Simulate system diagnostics (distractor block - not used in final result)
def run_diagnostics():
    status_codes = [200, 201, 404, 500, 301]
    error_count = 0
    for code in status_codes:
        if code >= 400:
            error_count += 1
    return error_count

diag_result = run_diagnostics()  # Irrelevant to final_score

# Core data processing
base_weights = [0.1, 0.2, 0.3, 0.4]
adjustment_factors = [1.1, 0.9, 1.0, 1.2]

# Combine weights with adjustments (semi-relevant but overridden later)
weighted_adjustments = []
for w, a in zip(base_weights, adjustment_factors):
    weighted_adjustments.append(w * a)

rankings = [88, 92, 76, 85, 90]
raw_performance = [85, 88, 80, 93, 87]

# Normalize rankings using min-max scaling (distraction computation)
norm_rankings = []
min_r, max_r = min(rankings), max(rankings)
for val in rankings:
    norm_rankings.append((val - min_r) / (max_r - min_r) if max_r != min_r else 0)

# Calculate moving average of performance (semi-relevant preprocessing)
moving_avg = []
window_size = 3
for i in range(len(raw_performance) - window_size + 1):
    avg = sum(raw_performance[i:i+window_size]) / window_size
    moving_avg.append(round(avg, 2))

performance_trend = analyze_performance(raw_performance)

# Auxiliary calculation: peak consistency index (unused red herring)
total_peaks = 0
for i in range(1, len(raw_performance)-1):
    if raw_performance[i] > raw_performance[i-1] and raw_performance[i] > raw_performance[i+1]:
        total_peaks += 1
peak_consistency = total_peaks / len(raw_performance)

# Key function combining multiple concepts: logic, lists, arithmetic, control flow
def calculate_final_score(ranks, trend):
    score = 0
    bonus_applied = False
    
    for idx, (rank, direction) in enumerate(zip(ranks, trend)):
        base_points = rank * 0.8
        
        # Logical condition with short-circuit evaluation
        if direction == 1 and not bonus_applied and base_points > 75:
            score += base_points * 1.2
            bonus_applied = True
        elif direction == 0:
            score += base_points * 0.95
        else:
            score += base_points * 0.85
            
        # Additional arithmetic adjustment
        if idx % 2 == 0:
            score = round(score + 2.5, 2)
    
    # Final threshold adjustment
    if score > 300:
        score *= 0.95
    
    return int(score)

# Execute key statement
temp_debug = [x * 2 for x in moving_avg]  # Dead code path
final_score = calculate_final_score(rankings, performance_trend)
print(f"Result: {final_score}")