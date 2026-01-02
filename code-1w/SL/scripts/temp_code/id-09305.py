import math

# Simulated agricultural yield dataset across regions and seasons
def generate_region_signals():
    return {
        'north': [87, 93, 72, 88, 65],
        'south': [64, 77, 82, 71, 91],
        'east': [55, 60, 63, 68, 73],
        'west': [81, 85, 87, 84, 89]
    }

# Irrelevant signal processing function (distractor)
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        left = max(0, i - 1)
        right = min(len(data), i + 2)
        smoothed.append(sum(data[left:right]) / (right - left))
    return smoothed

# Misleading transformation: looks important but unused later
def transform_readings(readings):
    processed = []
    for val in readings:
        if val > 80:
            processed.append(int(math.log(val) * 10))
        else:
            processed.append(val // 3)
    return processed

# Decoy accumulator with plausible name
def accumulate_metrics(data_dict):
    total_score = 0
    for region, values in data_dict.items():
        for v in values:
            total_score += (v % 17) * 2
    return total_score  # Never actually used

# Real threshold logic disguised among noise
def filter_by_condition(lst, func):
    return [x for x in lst if func(x)]

# High-level aggregation that appears complex but has a clear path
# This is where the real computation happens, buried in abstraction
def calculate_harvest(data_regions, threshold_strategy):
    
    # Step 1: Extract all values above regional baseline (logic step 1)
    merged_values = []
    for key in data_regions:
        merged_values.extend(data_regions[key])
    
    # Step 2: Apply dynamic threshold based on median (logic step 2)
    sorted_vals = sorted(merged_values)
    median_val = sorted_vals[len(sorted_vals) // 2]
    
    # Step 3: Create adaptive lambda filter (logic step 3)
    adaptive_threshold = lambda x: x > (median_val - 5)
    
    # Step 4: Filter values using strategy (logic step 4)
    qualified = filter_by_condition(merged_values, threshold_strategy)
    
    # Step 5: Remove duplicates via set operation (logic step 5)
    unique_qualifiers = list(set(qualified))
    
    # Step 6: Sort and take top 10% slice (round up) (logic step 6)
    unique_qualifiers.sort(reverse=True)
    slice_end = max(1, len(unique_qualifiers) * 10 // 100)
    top_slice = unique_qualifiers[:slice_end]  # slicing operation
    
    # Step 7: Apply non-linear yield transformation (logic step 7)
    adjusted_yields = list(map(lambda y: (y ** 1.1) / 4.3, top_slice))
    
    # Step 8: Summation and final adjustment (logic step 8)
    base_yield = sum(adjusted_yields)
    
    # Step 9: Correct for seasonal drift factor (logic step 9)
    drift_factor = 0.97
    corrected = base_yield * drift_factor
    
    # Step 10: Round to two decimal places (logic step 10)
    final_result = round(corrected, 2)
    
    # Red herring: this variable is assigned but irrelevant
    diagnostic_flag = any([len(v) < 4 for k, v in data_regions.items() if 's' in k])
    
    # Another decoy calculation
    _ = [transform_readings(region) for region in data_regions.values()]
    
    return final_result

# --- Main Execution ---

# Generate real data
regional_data = generate_region_signals()

# Unused smoothing (dead code path - distractor)
for region_name in regional_data:
    smoothed = smooth_signal(regional_data[region_name])  # computed but unused

# Irrelevant accumulation call (misleading intermediate result)
total_diagnostic_score = accumulate_metrics(regional_data)

# Define filtering strategy as lambda (required feature)
threshold_func = lambda x: x > 75

# Critical execution point
final_yield = calculate_harvest(regional_data, threshold_func)

# Output result as required
print(f"Result: {final_yield}")