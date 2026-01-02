def calculate_performance(base, meta):
    adjustment = 1.2 if base < 100 else 0.8
    
    # Irrelevant metric tracking (distractor)
    log_entry = {
        'status': 'processed',
        'version': '2.1'
    }
    
    score = base * adjustment
    
    # Apply bonus from dictionary values
    bonus = sum(meta.values()) * 0.1
    
    # Conditional expression based on performance tier
    penalty = 5 if len(meta) > 3 else 2
    
    result = score + bonus - penalty
    
    # Case conversion as part of unrelated logging
    log_entry['status'] = log_entry['status'].upper()
    
    return int(result)

# Main execution
baseline = 95
metrics = {
    'latency': 40,
    'throughput': 60,
    'accuracy': 95,
    'reliability': 80
}

initial_check = (baseline > 0)
diagnostic_tuple = ('system', 'diagnostic', baseline // 5)

final_score = calculate_performance(baseline, metrics)
print(f"Result: {final_score}")