def analyze_metrics(data):
    # Irrelevant transformation (distractor)
    temp_normalized = [x * 1.05 for x in data if x > 0]
    offset = sum(temp_normalized) / len(temp_normalized) if temp_normalized else 0

    # Semi-relevant pre-processing
    adjusted = [max(0, x - 2) for x in data]
    
    # Core logic: count how many are above threshold
    valid_count = sum(1 for x in adjusted if x >= 8)
    return valid_count

# Simulated sensor benchmark readings
dataset = [7, 9, -1, 10, 3, 8, 0, 9]

# Distractor variables and computations
scaling_factor = 1.2
baseline_shift = -0.5
dummy_calc = [round(x * scaling_factor + baseline_shift) for x in dataset]
buffer_zone = tuple(sorted(set(dummy_calc)))

# Secondary metric (not used in final answer but looks important)
outlier_flags = [x for x in dummy_calc if x < 5 or x > 12]
flag_count = len(outlier_flags)

# Key preprocessing with string-based tagging (required feature)
status_tags = ["valid" if x >= 8 else "review" for x in dataset]
tagged_count = status_tags.count("valid")

# Another distraction: average of modified values
shifted_avg = sum([x + 0.1 for x in dataset]) / len(dataset)

# Helper function that appears critical but only uses part of the data
def calculate_performance(raw_input):
    # Extract high-priority entries
    filtered = [x for x in raw_input if x > 0]
    
    # Apply non-linear weighting (important)
    weighted = [x ** 2 for x in filtered]
    
    # Use of tuple unpacking (suggested paradigm)
    total_energy = sum(weighted)
    sample_size = len(filtered)
    avg_weighted, _remainder = divmod(total_energy, sample_size) if sample_size else (0, 0)
    
    # String method used to simulate log tagging (required python feature)
    log_entry = f"Processed {sample_size} items"
    word_list = log_entry.split()
    item_count_str = word_list[-2]  # Just to use string methods
    
    # Additional intermediate calculation (distraction)
    peak_value = max(weighted) // 3
    decay_adjustment = peak_value * 0.1
    
    # Actual score computation
    base_metric = analyze_metrics(raw_input)
    bonus = 1 if len(raw_input) >= 6 else 0
    penalty = 1 if min(raw_input) < 0 else 0
    performance_index = base_metric + bonus - penalty
    
    # Final formula
    result = (avg_weighted + performance_index) * 1.5
    return int(result)

# Main execution
benchmark_data = dataset.copy()

# Dead code path (distractor)
if False:
    benchmark_data = [x * 2 for x in benchmark_data]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")