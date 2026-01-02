from collections import defaultdict
import math

# Simulate a power grid diagnostic system with efficiency mapping and load balancing

def analyze_redundancy(nodes):
    # Irrelevant function: analyzes node redundancy but not used in main logic
    redundant = 0
    for n in nodes:
        if n % 3 == 0 and n > 10:
            redundant += 1
    return redundant

def validate_phase_shift(signal):
    # Dead code path: never called
    return sum([abs(math.sin(x)) for x in signal])

def adjust_threshold(base, mode='dynamic'):
    # Distractor function: looks important but unused
    return base * 0.85 if mode == 'dynamic' else base * 1.1

def transform_matrix(mtx):
    # Unused transformation: decoy for complexity
    return [[mtx[i][j] * (i + j + 1) for j in range(len(mtx[0]))] for i in range(len(mtx))]

def recursive_efficiency(n):
    # Relevant helper: computes efficiency decay using recursion
    if n <= 1:
        return 1.0
    return recursive_efficiency(n - 1) * (0.9 + 0.05 * (n % 2))

def build_efficiency_map(levels):
    # Constructs map of recursive efficiency values
    return {lvl: recursive_efficiency(lvl) for lvl in range(1, levels + 1)}

def simulate_failover(primary, backup, threshold=750):
    # Misleading intermediate calculation
    load_diff = abs(primary - backup)
    if load_diff > threshold:
        return primary * 0.6
    return primary  # Never actually affects final result

def calculate_peak(load_profile, efficiency_lookup):
    # Core logic: compute peak adjusted capacity
    temp_storage = []
    accumulator = defaultdict(lambda: 0)
    
    for idx, load in enumerate(load_profile):
        tier = (idx // 4) + 1
        tier = min(tier, 5)
        raw_power = load * 1.05
        
        # Apply efficiency based on tier level
        if tier in efficiency_lookup:
            adjusted = raw_power * efficiency_lookup[tier]
        else:
            adjusted = raw_power * 0.5
        
        # Conditional expression with filtering
        status_flag = 'nominal' if adjusted > 400 else 'low'
        accumulator[status_flag] += 1
        
        temp_storage.append(adjusted)
    
    # Real computation path
    sorted_vals = sorted(temp_storage, reverse=True)
    top_three_avg = sum(sorted_vals[:3]) / 3
    
    # Final peak capacity with safety margin
    final_peak = int(top_three_avg * 0.92)
    
    # Decoy operation: does not affect output
    _ = [x * 1.1 for x in sorted_vals if x < 300]
    
    return final_peak

# Main execution block
if __name__ == '__main__':
    # Simulated grid load data (in megawatts)
    grid_load = [480, 520, 490, 410, 550, 530, 470, 500, 510, 460]
    
    # Irrelevant data structures
    node_topology = [12, 15, 18, 22, 25]
    phase_signal = [0.1, 0.7, 1.3, 2.2, 3.1]
    threshold_base = 950
    
    # Build efficiency model
    efficiency_map = build_efficiency_map(5)
    
    # Simulate failover scenarios (results discarded)
    _ = simulate_failover(800, 600)
    _ = simulate_failover(700, 900)
    
    # Transform dummy matrix (no effect)
    dummy_grid = [[1, 2], [3, 4]]
    _ = transform_matrix(dummy_grid)
    
    # Key statement: calculate peak capacity
    peak_capacity = calculate_peak(grid_load, efficiency_map)
    
    # Print result as required
    print(f"Result: {peak_capacity}")