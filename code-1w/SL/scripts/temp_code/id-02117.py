def analyze_component(x, threshold=5):
    return x > threshold and (x % 2 == 0 or x % 3 == 0)

# Simulate sensor array readings (distractor: not all are used)
sensor_readings = [4, 7, 12, 15, 21, 22, 8, 9]
valid_readings = [x for x in sensor_readings if analyze_component(x)]

def calculate_stability(readings):
    # Irrelevant stability metric (dead computation)
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return round(variance, 3)

stability_index = calculate_stability(sensor_readings)  # Unused later

# Core data processing pipeline
raw_metrics = [18, 25, 36, 49, 64]
processed = list(map(lambda x: x // 2 if x % 2 == 0 else x + 1, raw_metrics))

# Conditional filtering with nested logic
filtered = []
for val in processed:
    if val > 20:
        if val % 3 == 0:
            filtered.append(val * 1.1)
        elif val % 4 == 0:
            filtered.append(val * 0.9)
    else:
        filtered.append(val)

# Secondary transformation chain
transformed = [round(x + 5) for x in filtered if x != 25]  # Filter excludes non-existent 25

# Benchmark result simulation
benchmark_results = {
    'base': sum(transformed),
    'peak': max(transformed),
    'count': len(transformed)
}

# Auxiliary function with red herring parameters
def adjust_for_latency(value, factor=1.05, debug_mode=False):
    temp_log = []
    for i in range(3):  # Simulated debug logging (irrelevant)
        temp_log.append(f"Step {i} intermediate")
    if debug_mode:
        print(temp_log)
    return value * factor

# Main performance calculation
def calculate_performance(data):
    base = data['base']
    peak = data['peak']
    count = data['count']
    
    # Complex conditional scoring
    if peak > 50:
        if count >= 4:
            score = base * 1.2
        else:
            score = base * 1.1
    else:
        score = base * 0.95
    
    # Apply adjustment (debug_mode=False, so no real effect)
score = adjust_for_latency(score, debug_mode=False)
    
    # Final normalization
    normalized = score / (count or 1)
    return int(round(normalized))

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")