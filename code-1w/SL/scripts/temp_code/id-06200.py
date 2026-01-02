from collections import defaultdict

def calculate_performance(base, data):
    stats = defaultdict(float)
    adjustment = 0.85
    
    for reading in data:
        if reading > base:
            stats['positive'] += (reading - base) * adjustment
        elif reading < base:
            stats['negative'] += (base - reading) * 0.5
    
    raw_score = stats['positive'] - stats['negative']
    penalty = len([x for x in data if x < base * 0.75]) * 2.5
    final_score = raw_score - penalty
    
    # Irrelevant logging
    log_entry = f"Processed {len(data)} entries"
    unused_value = [1 for _ in range(5)]  # Distractor list comprehension
    
    return int(final_score)

# Main execution
baseline = 72
readings = [75, 68, 80, 70, 95, 60]
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")