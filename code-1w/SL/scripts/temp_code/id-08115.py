def compute_order_integrity(orders, thresholds):
    total_weight = 0
    checksum = 0
    temp_accum = 0
    safety_factor = sum(thresholds) // len(thresholds)
    
    for index, (order_id, weight, priority) in enumerate(orders):
        if priority < thresholds[index % len(thresholds)]:
            adjustment = (weight // 4) + 1
            total_weight += weight - adjustment
            temp_accum += adjustment * 2
        else:
            total_weight += weight
            
        # Irrelevant intermediate tracking
        status_flag = (priority ^ order_id) & 1
        if status_flag:
            temp_accum -= 1

        # Key computation with distractors around
        checksum ^= order_id ^ (index + 1)
        
        # Dead code path - never impacts result
        if False:
            dummy = (order_id + index) % 997
            checksum += dummy

    # Post-processing unrelated to final answer
    final_ratio = total_weight / (len(orders) + 1e-5)
    adjusted_checksum = checksum + int(final_ratio % 10)
    
    return checksum

# Input data
order_list = [
    (1001, 24, 3),
    (1002, 15, 1),
    (1003, 40, 4),
    (1004, 10, 2)
]
threshold_settings = [2, 3, 1]

result = compute_order_integrity(order_list, threshold_settings)
print(f'Result: {result}')