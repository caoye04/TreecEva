def analyze_redundancy(items):
    redundant = set()
    seen = set()
    for item in items:
        if item in seen:
            redundant.add(item)
        else:
            seen.add(item)
    return redundant


def adjust_tolerance(base, factor=0.75):
    # Irrelevant computation - distractor
    return int(base * factor + 2) % 5

def filter_critical(stock, limits):
    result = []
    for level in stock:
        if level < limits[0] or level > limits[1]:
            result.append(level)
    return result  # Unused in final logic

def optimize_distribution(inventory, safety_set):
    temp_result = 0
    shift_factor = len(safety_set) % 3
    
    for i, amount in enumerate(inventory):
        if i % 2 == 0 and amount not in safety_set:
            temp_result += amount // (i + 1)
        elif i % 2 == 1:
            temp_result -= (amount % (i + 2))
    
    # Secondary adjustment with partial relevance
    if shift_factor > 0:
        temp_result = abs(temp_result) + shift_factor

    # Dead code path - misleading
    if temp_result < 0:
        backup = sum(inventory) // len(inventory)
        temp_result = backup  # Never reached due to abs()

    return temp_result

# Main execution
inventory_levels = [48, 15, 22, 9, 36, 13]
threshold_set = {10, 15, 20, 25}

# Distractor variables and operations
redundant_units = analyze_redundancy([5, 3, 5, 7, 8, 7])
tolerance_band = adjust_tolerance(100)
ignored_outliers = filter_critical(inventory_levels, (10, 30))
placeholder_sum = sum(redundant_units) * 2  # Unused

# Key computation step
final_capacity = optimize_distribution(inventory_levels, threshold_set)

Result: final_capacity