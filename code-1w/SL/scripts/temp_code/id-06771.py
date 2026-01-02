from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [15, 23, 18, 47, 33, 40, 29, 54]
    metrics = defaultdict(int)
    temp_accum = 0
    
    for val in raw_data:
        if val > 30:
            metrics['high'] += 1
            temp_accum += val // 3
        elif val > 20:
            metrics['medium'] += 1
            temp_accum -= val % 7
        else:
            metrics['low'] += 1
    
    # Irrelevant transformation
    offset = sum([x for x in raw_data if x % 2 == 0]) // 8
    dummy_var = (offset ** 2) + 5  # Unused later
    
    metrics['temp_offset'] = temp_accum  # Used only once
    return metrics

# Analyze trends with side computations
def analyze_trend(data):
    trend_score = 0
    history = []
    
    for key, count in data.items():
        if 'high' in key:
            trend_score += count * 3
        elif 'medium' in key:
            trend_score += count * 2
        else:
            trend_score += count
            
        # Dead computation path (never used)
        if count < 2:
            history.append('rare')
        else:
            history.append('common')
    
    # Extra logic that doesn't influence result
    avg_hist = len(history) / len(data) if data else 0
    padding = int(avg_hist * 1.5)  # Not used
    
    return trend_score

# Main processing with bitwise manipulation and filtering
def process_performance(data, limit):
    base = analyze_trend(data)
    bonus = 0
    penalty = 0
    
    # Conditional bonuses using bitwise logic
    if data['high'] & 1:  # If odd number of high events
        bonus += 12
    
    if data['medium'] > 2:
        bonus += 8
    
    # Red herring: complex-looking but unused calculation
    shadow_calc = (data['low'] << 2) ^ (data['high'] | 5)
    temp_result = shadow_calc % 17  # Nowhere used
    
    # Penalty based on thresholds
    total_events = sum(data.values())
    if total_events > limit:
        penalty += 5
    
    # Critical line: final_score computed here
    final_score = base + bonus - penalty
    
    # Additional unrelated tracking
    stats_log = {"entries": total_events, "bonus_applied": bonus > 0}
    return final_score

# Execution flow
if __name__ == "__main__":
    collected = collect_metrics()
    threshold = 10
    final_score = process_performance(collected, threshold)
    print(f"Result: {final_score}")