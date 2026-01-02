def evaluate_performance(metrics):
    base_score = 75
    total_score = base_score
    adjustments = [-5, 10, 0, 15, -2]
    statuses = ['inactive', 'active', 'pending', 'active', 'inactive']
    extra_bonus = 0

    for i, (metric, status) in enumerate(zip(metrics, statuses)):
        if metric < 80 and status == 'active':
            adjustment = adjustments[i] + 3
        elif metric >= 90:
            adjustment = adjustments[i] + 5
        else:
            adjustment = adjustments[i]
        
        if status == 'pending':
            adjustment = max(adjustment, 0)
            
        total_score += adjustment

    final_multiplier = 1.1
    total_score = int(total_score * final_multiplier)
    
    # Irrelevant logging
    log_entry = f'Processed {len(metrics)} entries'
    debug_flag = False

    print(f"Result: {total_score}")

# Input data
data_metrics = [78, 92, 85, 95, 70]
evaluate_performance(data_metrics)