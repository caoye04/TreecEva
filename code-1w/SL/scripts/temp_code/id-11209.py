def calculate_final_score(raw_data, limits):
    # Preprocessing: clean and filter data
    cleaned = [x for x in raw_data if isinstance(x, (int, float)) and x >= 0]
    
    # Irrelevant transformation (distractor)
    normalized = list(map(lambda val: val / (max(cleaned) + 1e-9), cleaned))
    
    # Grouping by threshold bands (relevant)
    bands = {"low": [], "medium": [], "high": []}
    for item in cleaned:
        if item < limits[0]:
            bands["low"].append(item)
        elif item < limits[1]:
            bands["medium"].append(item)
        else:
            bands["high"].append(item)
    
    # Red herring computation with string methods (irrelevant)
    debug_tag = "processed_{}_items".format(len(cleaned))
    debug_checksum = sum(ord(c) for c in debug_tag) % 1000
    
    # Set operations to find overlaps (semi-relevant, but unused in final logic)
    unique_high = set(bands["high"])
    unique_medium = set(bands["medium"])
    potential_overlap = unique_high & unique_medium  # Always empty, but included for distraction
    
    # Core scoring logic (depends only on medium and high counts)
    base_points = len(bands["medium"]) * 2 + len(bands["high"]) * 5
    
    # Bonus logic: if high group has power-of-two size, add bonus
    if len(bands["high"]) > 0 and (len(bands["high"]) & (len(bands["high"]) - 1)) == 0:
        base_points += 10
    
    # Apply penalty if low group is more than twice the high group
    if len(bands["low"]) > 2 * len(bands["high"]):
        base_points -= 5
    
    # Dead code path (never executed due to data constraints)
    if debug_checksum < 0:
        base_points = -1  # unreachable
    
    return base_points

# Input data with mixed types and noise
data = [10, -5, 3.5, 'invalid', 8, 12, 6, None, 15, 9, 7, 4.2]
thresholds = (6, 10)

# Extra variables to increase cognitive load
average_value = sum(x for x in data if isinstance(x, (int, float))) / len([x for x in data if isinstance(x, (int, float))])
duplicate_count = len(data) - len(set(str(x) for x in data))

# Key execution point
final_score = calculate_final_score(data, thresholds)

# Output result
print(f"Result: {final_score}")