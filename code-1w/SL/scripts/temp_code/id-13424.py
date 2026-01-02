from collections import defaultdict

# Simulate system metrics over time
def collect_metrics():
    raw_data = [15, 20, 25, 30, 35, 40, 45, 50]
    processed = []
    temp_offset = 0
    
    for val in raw_data:
        if val % 2 == 0:
            processed.append(val + temp_offset)
        else:
            temp_offset += 1  # Only affects even values indirectly
    
    # Misleading transformation
    shifted = [x * 1.1 for x in processed]
    return processed  # Original processed data returned

# Analyze trend with irrelevant helper
def calculate_trend(data):
    trend_values = []
    avg_change = 0
    total_change = 0
    
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        total_change += diff
        trend_values.append(diff)
    
    if len(data) > 1:
        avg_change = total_change / (len(data) - 1)
    
    # Dead code path - never used
    if avg_change < 0:
        return 'decreasing'
    
    return avg_change

# Evaluate performance against baseline
def evaluate_performance(metrics, base):
    score = 0
    penalty = 0
    bonus = 0
    
    # Count occurrences above baseline
    above_count = 0
    for m in metrics:
        if m > base:
            above_count += 1
    
    # Apply conditional scoring
    if above_count >= 5:
        score += 100
    elif above_count >= 3:
        score += 60
    else:
        score += 30
    
    # Irrelevant bonus calculation (never applied due to logic)
    consecutive = 0
    max_consecutive = 0
    for m in metrics:
        if m > base:
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 0
    
    if max_consecutive >= 6:
        bonus += 25
    
    # Another distraction: frequency tracking
    freq = defaultdict(int)
    for m in metrics:
        freq[m] += 1
    
    unique_values = len(freq)
    if unique_values > 6:
        penalty += 10
    
    final_score = score + bonus - penalty
    return final_score

# Main execution
metrics = collect_metrics()
trend = calculate_trend(metrics)
baseline = 28
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")