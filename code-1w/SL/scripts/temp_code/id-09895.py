def analyze_efficiency(values):
    weighted = [v * (i + 1) for i, v in enumerate(values)]
    avg = sum(weighted) / len(weighted)
    return avg

metrics = [85, 90, 78, 92]
bonuses = [5, 3, 10]

def adjust_bonus(bonuses, factor=1.1):
    temp_result = [round(b * factor, 2) for b in bonuses]
    total_adjusted = sum(temp_result)
    dummy_shift = [b << 1 for b in bonuses]  # Irrelevant bit-shift
    return temp_result

def compute_base(metric):
    base = metric * 0.1
    offset = 5
    return base + offset

def process_performance(metrics, bonuses):
    base_scores = [compute_base(m) for m in metrics]
    efficiency = analyze_efficiency(base_scores)
    adjusted_bonuses = adjust_bonus(bonuses)
    bonus_sum = sum(adjusted_bonuses[:len(metrics)])  # Truncate to metric length
    
    # Misleading string manipulation distraction
    status_str = "Performance_Review_Complete"
    check_flag = len(status_str.split('_')) > 2 and 'Complete' in status_str
    
    # Dummy list processing with itertools
    from itertools import cycle
    cyclic_iter = cycle([1, 0])
    pattern_mask = [next(cyclic_iter) for _ in range(len(metrics))]
    masked_effect = sum(p * bonus_sum for p in pattern_mask) / len(pattern_mask) if pattern_mask else 0
    
    final_score = efficiency + masked_effect
    return final_score

# Key execution point
target_metrics = [85, 90, 78, 92]
final_score = process_performance(metrics, bonuses)
print(f"Result: {final_score}")