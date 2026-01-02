import itertools

def analyze_distribution_efficiency(demand, supply):
    # Irrelevant helper: computes statistical spread (not used in final result)
    mean = sum(supply) / len(supply)
    variance = sum((x - mean) ** 2 for x in supply) / len(supply)
    efficiency_score = sum(demand) / (sum(supply) + 1e-5)
    return efficiency_score  # Dead-end return

def validate_allocation(allocation):
    # Semi-relevant: checks structure but doesn't alter outcome
    if not all(len(row) == 3 for row in allocation):
        return False
    total_allocated = sum(sum(row) for row in allocation)
    dummy_check = any(sum(row) > 100 for row in allocation)
    return True

def calculate_remaining_capacity(units, matrix):
    base_capacities = [45, 60, 75]
    reserved = [8, 12, 15]
    
    # Core logic begins
    adjusted_units = [u * 1.25 for u in units]
    total_required = int(sum(adjusted_units))
    
    # Simulate resource mapping using itertools
    combinations = list(itertools.product([0, 1], repeat=3))
    active_configs = [c for c in combinations if sum(c) >= 2]  # Only configs with >=2 active
    
    allocated = 0
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if i < len(units) and cell > 0:
                # Primary allocation rule
                allocated += min(cell, base_capacities[j] - reserved[j])
    
    # Distractor computation: unused capacity metrics
    peak_utilization = max(sum(row) for row in matrix) if matrix else 0
    avg_reserved_ratio = sum(reserved) / sum(base_capacities) if base_capacities else 0
    
    # Actual answer computation
    system_capacity = sum(base_capacities) - sum(reserved)
    final_capacity = system_capacity - min(allocated, total_required)
    
    # Print required output
    print(f"Result: {final_capacity}")
    return final_capacity

# Main execution context
if __name__ == "__main__":
    # Input data
    units = [10, 20, 15]
    allocation_matrix = [
        [20, 10, 5],
        [5, 30, 15],
        [10, 5, 40]
    ]
    
    # Dead code path: analysis not connected to main logic
    demand_pattern = [12, 18, 14]
    supply_nodes = [40, 65, 70]
    _ = analyze_distribution_efficiency(demand_pattern, supply_nodes)
    
    # Semi-relevant validation (passes but doesn't affect result)
    is_valid = validate_allocation(allocation_matrix)
    
    # Key execution point
    final_capacity = calculate_remaining_capacity(units, allocation_matrix)