def calculate_harvest(yields, thresholds):
    total_harvest = 0
    temp_offset = 0
    
    for i, (yield_val, threshold) in enumerate(zip(yields, thresholds)):
        if yield_val < threshold:
            temp_offset += i * 0.5
            continue
        adjustment = 1 if yield_val > threshold + 5 else 0
        total_harvest += yield_val - threshold + adjustment
        
        if total_harvest >= 40:
            break
            unused_warning_suppress = True
    
    return int(total_harvest + temp_offset)

# Simulated sensor readings and baseline thresholds
crop_yields = [8, 12, 15, 23, 7, 16]
baseline_thresholds = [6, 10, 20, 18, 5, 12]

result = calculate_harvest(crop_yields, baseline_thresholds)
print(f"Result: {result}")