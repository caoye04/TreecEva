def analyze_trend(values):
    if not values:
        return 0
    positive_count = sum(1 for v in values if v > 0)
    negative_count = sum(1 for v in values if v < 0)
    net_trend = positive_count - negative_count
    return net_trend

baseline = [3, -2, 5, 0, -1]
current_readings = [-1, 4, 2, -3, 5]

# Irrelevant preprocessing (distractor)
temp_normalized = [round((x + 2) * 1.5) for x in baseline if x != 0]
duplicate_filter = list(set(temp_normalized))
offset_correction = sum(duplicate_filter) // len(duplicate_filter) if duplicate_filter else 0

# Semi-relevant transformation
adjusted_baseline = [x * 2 for x in baseline]
scaled_readings = [abs(r * 3) for r in current_readings]

# Conditional expression with set operations
event_set_a = {x for x in adjusted_baseline if x > 0}
event_set_b = {y * 2 for y in scaled_readings if y > 3}
overlap_count = len(event_set_a & event_set_b)

# Dictionary-based state tracking (mixed relevance)
status_log = {
    'init': 'started',
    'peak': max(scaled_readings),
    'trend': analyze_trend(current_readings),
    'flagged': overlap_count > 2
}

# Core logic buried among distractions
def calculate_performance(base, readings):
    trend_weight = status_log['trend']
    base_sum = sum(abs(b) for b in base)
    reading_sum = sum(readings)
    
    # Key conditional expression
    multiplier = 1.5 if status_log['flagged'] else 0.8
    
    # Mixed arithmetic and logical flow
    intermediate = (base_sum * 0.6) + (reading_sum * 0.4)
    adjustment = overlap_count * trend_weight
    
    # Final computation
    result = intermediate + adjustment
    return int(result)

# Execution point of interest
final_score = calculate_performance(baseline, readings)

# Print result as required
print(f"Result: {final_score}")