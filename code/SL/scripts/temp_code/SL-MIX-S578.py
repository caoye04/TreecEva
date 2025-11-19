import re
from functools import reduce

def process_batch_quality(base_scores, defect_log):
    # Apply pattern matching to identify critical defects
    critical_defects = len(re.findall(r'(MISS|TEAR|STAIN)', defect_log))
    
    # Greedy optimization: subtract penalty for each critical defect
    optimized_base = [score - (critical_defects * 2) for score in base_scores]
    
    # Filter out negative scores using functional approach
    valid_scores = list(filter(lambda x: x > 0, optimized_base))
    
    # If no valid scores remain, return zero
    if not valid_scores:
        return 0
    
    # Divide and conquer approach to calculate aggregate score
    def divide_scores(scores):
        if len(scores) <= 1:
            return scores[0] if scores else 0
        mid = len(scores) // 2
        left = divide_scores(scores[:mid])
        right = divide_scores(scores[mid:])
        return left + right
    
    return divide_scores(valid_scores)

def update_station_state(current_state, batch_result):
    # State machine logic for station status
    if batch_result >= 80:
        return 'EXCELLENT'
    elif batch_result >= 60:
        return 'GOOD'
    elif batch_result >= 40:
        return 'FAIR'
    else:
        return 'POOR'

# Production line configuration
fabric_batches = [
    ([85, 90, 78], "NORMAL"),
    ([92, 88, 84], "MISS DETECTED"),
    ([76, 81, 73], "TEAR STAIN"),
    ([95, 91, 89], "NORMAL")
]

station_status = 'IDLE'
accumulated_score = 0

for scores, log in fabric_batches:
    batch_quality = process_batch_quality(scores, log)
    
    # Conditional branching based on quality results
    if batch_quality > 0:
        accumulated_score += batch_quality
        station_status = update_station_state(station_status, batch_quality)
    else:
        # In case of failed batch, apply penalty
        accumulated_score -= 10
        station_status = 'ERROR'

# Final adjustment based on overall performance
if station_status in ['EXCELLENT', 'GOOD']:
    optimized_score = accumulated_score * 1.1
else:
    optimized_score = accumulated_score * 0.95

print(f"Result: {int(optimized_score)}")