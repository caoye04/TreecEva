def calculate_performance(data):
    total = 0
    count = 0
    adjustments = [0.5, -0.2, 0.3, 0.0, 0.1]
    
    for i, (name, base) in enumerate(zip(data.keys(), data.values())):
        if len(name.strip()) == 0:
            continue
        modifier = adjustments[i % len(adjustments)]
        adjusted = base * (1 + modifier)
        total += adjusted
        count += 1
    
    average = total / count if count else 0
    max_base = max(data.values())
    min_base = min(data.values())
    range_bonus = (max_base - min_base) * 0.1
    final_score = average + range_bonus
    
    temp_debug = [x for x in data.keys() if 'temp' in x]  # irrelevant tracking
    return final_score

# Benchmark dataset
dataset = {
    "module_A": 88,
    "module_B": 92,
    "core_engine": 76,
    "network_io": 81,
    "temp_debug_module": 0  # not used in logic
}

final_score = calculate_performance(dataset)
print(f"Result: {final_score}")