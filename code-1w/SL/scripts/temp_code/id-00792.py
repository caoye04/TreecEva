def analyze_growth_rate(data):
    # Irrelevant helper function with dead logic
    cumulative = 0
    for x in data:
        if x > 5:
            cumulative += x * 0.1
    return cumulative  # Never used in main logic

def preprocess_sensors(sensor_logs):
    # Distractor: processes sensor data that isn't actually needed
    cleaned = []
    for i, log in enumerate(sensor_logs):
        if i % 2 == 0 and sum(log) < 100:
            cleaned.append(sum(log) / len(log))
    return [x * 1.5 for x in cleaned]  # Computation goes nowhere

def calculate_optimal_yield(crop_data):
    # Core logic embedded in noise
    base_yield = 0
    adjustments = []
    threshold = 85
    
    # Real logic starts here — hidden among red herrings
    for day, readings in enumerate(crop_data['readings'], start=1):
        avg_temp = sum(readings) / len(readings)
        growth_factor = 1.0
        
        # Meaningful conditional branch
        if avg_temp > 30:
            growth_factor *= 0.8
        elif 20 <= avg_temp <= 30:
            growth_factor *= 1.2  # Optimal range
        else:
            growth_factor *= 0.6
        
        # Another relevant transformation
        adjusted_yield = crop_data['base_production'][day-1] * growth_factor
        adjustments.append(adjusted_yield)
    
    # Critical calculation
    total_adjusted = sum(adjustments)
    peak_day = max(enumerate(crop_data['base_production']), key=lambda x: x[1])[0]
    
    # Decoy variables and misleading computations
    fake_projection = total_adjusted * 0.9 + 123.45
    dummy_offset = sum([i for i in range(len(crop_data['readings']))]) * 0.01
    
    # Red herring with zip and enumerate (looks important but isn't)
    for idx, (a, b) in enumerate(zip(crop_data['readings'][::-1], adjustments)):
        if idx % 3 == 0:
            dummy_offset += a[0] * b * 0.001  # Noise
    
    # Actual answer computation
    final_yield = int(total_adjusted) + (peak_day * 10)
    
    # Unused dictionary operations — distractors
    stats = {f'day_{i}': val for i, val in enumerate(adjustments)}
    stats.update({'max': max(adjustments), 'min': min(adjustments)})
    stats.pop('day_0', None)
    
    return final_yield

# Simulated agricultural sensor input (irrelevant part)
sensor_logs = [[23,25,27],[95,12],[45,50],[30,32],[88,12]]
preprocess_sensors(sensor_logs)  # Called but result ignored

# Main dataset with meaningful structure
harvest_data = {
    'readings': [
        [22, 24, 26],      # Day 1 temps
        [28, 30, 32],      # Day 2
        [18, 20, 22],      # Day 3
        [34, 36, 33]       # Day 4
    ],
    'base_production': [150, 180, 140, 160]
}

# Dead variable assignments — distraction
baseline_score = 78.5
evaluation_flag = True
interim_result = analyze_growth_rate([10, 20, 30])

# Key execution point
final_yield = calculate_optimal_yield(harvest_data)

# Output required format
print(f"Target result: {final_yield}")