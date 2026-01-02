from itertools import combinations

# Simulate sensor array readings with noise filtering
def process_readings(raw_data):
    filtered = [x for x in raw_data if 0 <= x <= 100]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    deviation = [abs(x - baseline) for x in filtered]
    clean_data = [x for i, x in enumerate(filtered) if deviation[i] < 15]
    return clean_data if clean_data else [baseline]

# Analyze pattern consistency across multiple trials
def evaluate_consistency(data_stream):
    patterns = []
    for i in range(len(data_stream) - 2):
        if data_stream[i] < data_stream[i+1] > data_stream[i+2]:
            patterns.append(1)
        elif data_stream[i] > data_stream[i+1] < data_stream[i+2]:
            patterns.append(-1)
    return len(patterns)

# Calculate system performance metric based on processed results
def calculate_performance(results):
    # Irrelevant preprocessing: sorting and reversing (distractor)
    temp_sorted = sorted(results)
    temp_reversed = temp_sorted[::-1]
    mid_value = temp_sorted[len(temp_sorted)//2]
    
    # Key computation path
    avg = sum(results) / len(results)
    variance = sum((x - avg) ** 2 for x in results) / len(results)
    std_dev = variance ** 0.5
    
    # Secondary metrics (partially relevant)
    peak_count = sum(1 for a, b, c in zip(results, results[1:], results[2:]) if b > a and b > c)
    trend_score = evaluate_consistency(results)
    
    # Distractor variables (not used in final score but look relevant)
    entropy_approx = 0.0
    for x in results:
        if x > 0:
            entropy_approx += x * __import__('math').log(x)
    
    # Final weighted performance index
    stability_factor = 1 / (std_dev + 1)
    final_score = int(
        0.4 * avg + 
        0.3 * peak_count * 10 + 
        0.2 * trend_score * 5 + 
        0.1 * stability_factor * 100
    )
    return final_score

# Simulated benchmark data from experimental run
dataset = [85, 92, 78, 63, 96, 88, 72, 81, 87, 76, 91, 83, 77, 89, 84]

# Noise injection for realism (some out-of-bounds values)
raw_input = dataset + [105, -3, 98, 110, 79]

# Processing pipeline
filtered_output = process_readings(raw_input)

# Generate all possible triplets (distractor - not used later)
triplet_combinations = list(combinations(filtered_output, 3))
total_triplets = len(triplet_combinations)

# Mean of triplets (dead code - computed but unused)
mean_of_triplets = sum(sum(t) / 3 for t in triplet_combinations) / total_triplets if total_triplets else 0

# Core evaluation
benchmark_results = filtered_output[:10]  # Truncate to standard size
final_score = calculate_performance(benchmark_results)

print(f"Result: {final_score}")