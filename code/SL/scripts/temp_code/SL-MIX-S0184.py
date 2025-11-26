import itertools

def process_inventory_data(raw_data):
    # Irrelevant processing that won't be used
    temp_sum = sum(x * 2 for x in raw_data[:3])
    filtered_data = [x for x in raw_data if x % 3 == 0]
    return filtered_data

def calculate_inventory_turnover(periods):
    # Misleading intermediate calculation
    avg_period = sum(periods) / len(periods) if periods else 0
    cycle_count = len(list(itertools.combinations(periods, 2)))
    return cycle_count, avg_period

def adjust_for_seasonality(base_value, seasonal_factors):
    # Dead code path - seasonal adjustment won't be applied
    if len(seasonal_factors) > 4:
        adjustment = sum(seasonal_factors) * 0.1
        return base_value + adjustment
    return base_value

def compute_final_value(data):
    # Main logic with multiple steps
    processed = process_inventory_data(data)
    
    # Relevant processing
    if len(processed) >= 2:
        core_pairs = list(itertools.combinations(processed, 2))
        valid_pairs = [(a, b) for a, b in core_pairs if abs(a - b) <= 15]
        
        if valid_pairs:
            pair_sums = [a + b for a, b in valid_pairs]
            min_sum = min(pair_sums) if pair_sums else 0
            max_sum = max(pair_sums) if pair_sums else 0
            
            # Critical calculation
            turnover_metric = (max_sum - min_sum) * len(valid_pairs)
            
            # Additional processing that affects final result
            inventory_cycles, _ = calculate_inventory_turnover(processed)
            final_result = turnover_metric // (inventory_cycles + 1) if inventory_cycles > 0 else turnover_metric
            
            # Apply modular arithmetic
            seasonal_factors = [2, 5, 8, 11]
            adjusted = adjust_for_seasonality(final_result, seasonal_factors)
            
            return adjusted % 47
    
    return 0

# Main execution
inventory_data = [12, 8, 25, 18, 7, 22, 14, 30, 5]
seasonal_adjustments = [3, 7, 11]  # Unused seasonal data
backup_data = [x * 2 for x in inventory_data[:4]]  # Irrelevant backup calculation

final_output = compute_final_value(inventory_data)
print(f"Result: {final_output}")