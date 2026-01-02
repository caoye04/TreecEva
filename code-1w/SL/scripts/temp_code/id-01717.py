from itertools import combinations
from functools import reduce
import math

# Simulated system metrics (some are red herrings)
def collect_diagnostics():
    return {
        'latency_ms': 45,
        'cpu_load': 78,
        'mem_usage_mb': 2048,
        'disk_iops': 120,
        'temp_c': 67,
        'packet_loss': 0.003,
        'fan_speed_rpm': 2400,
        'power_draw_w': 135
    }

def normalize(value, min_val, max_val):
    # Normalizes value to [0,1] range
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))

def compute_entropy(data_list):
    # Irrelevant function - distractor
    total = sum(data_list)
    if total == 0:
        return 0.0
    probs = [x / total for x in data_list]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def analyze_redundancy(config_matrix):
    # Dead code path - never used
    rows, cols = len(config_matrix), len(config_matrix[0])
    redundant = 0
    for i in range(rows - 1):
        for j in range(cols):
            if config_matrix[i][j] == config_matrix[i+1][j]:
                redundant += 1
    return redundant

def filter_outliers(data, threshold=1.5):
    # Computes IQR but not actually used in final score
    sorted_vals = sorted(data.values())
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    filtered = {k: v for k, v in data.items() if lower_bound <= v <= upper_bound}
    return filtered  # Not used

def generate_weight_combinations(n):
    # Creates unused weight sets - misleading complexity
    base_weights = [0.1, 0.15, 0.2, 0.25, 0.3]
    return list(combinations(base_weights, n))

def calculate_efficiency_index(x, y, z):
    # Unused helper - red herring
    return (x * y**2) / (z + 1e-8)

def adjust_for_temperature(raw_score, temp):
    # Not actually applied in main logic
    if temp > 60:
        return raw_score * 0.92
    return raw_score

def evaluate_performance(metrics, weights_override=None):
    # Core logic embedded within distractions
    
    # Relevant metric extraction
    raw_latency = metrics['latency_ms']
    raw_cpu = metrics['cpu_load']
    raw_mem = metrics['mem_usage_mb']
    raw_disk = metrics['disk_iops']
    
    # Normalize relevant metrics
    norm_latency = 1 - normalize(raw_latency, 10, 100)  # Inverted: lower latency = better
    norm_cpu = 1 - normalize(raw_cpu, 0, 100)
    norm_mem = 1 - normalize(raw_mem, 512, 4096)
    norm_disk = normalize(raw_disk, 50, 200)
    
    # Weighted scoring
    default_weights = [0.3, 0.25, 0.25, 0.2]  # latency, cpu, mem, disk
    weights = weights_override or default_weights
    
    # Apply weights using lambda and reduce for functional style (actual use)
    scores = [norm_latency, norm_cpu, norm_mem, norm_disk]
    weighted_sum = reduce(lambda acc, pair: acc + pair[0]*pair[1], zip(scores, weights), 0.0)
    
    # Additional adjustment based on hidden rule: penalize if any normalized score < 0.4
    penalty_factor = 0.95 if any(s < 0.4 for s in scores) else 1.0
    adjusted_score = weighted_sum * penalty_factor
    
    # Bit manipulation check: if CPU load is odd, flip last bit of integer part
    int_part = int(adjusted_score * 100)
    fractional = adjusted_score * 100 - int_part
    if metrics['cpu_load'] % 2 == 1:
        int_part ^= 1  # XOR with 1 toggles least significant bit
    
    final_normalized = (int_part + fractional) / 100.0
    
    # Irrelevant transformations below
    _ = math.sin(metrics['temp_c']) * 100  # unused
    _ = set(metrics.keys()) - {'fan_speed_rpm', 'power_draw_w'}  # unused set op
    
    # Final output
    return round(final_normalized, 6)

# --- Main Execution ---
if __name__ == '__main__':
    
    # Collect system diagnostics (many fields irrelevant)
    system_data = collect_diagnostics()
    
    # Generate unused combinatorial weights
    _ = generate_weight_combinations(4)
    
    # Filter outliers (result ignored)
    _ = filter_outliers(system_data)
    
    # Compute entropy on arbitrary values (not used)
    _ = compute_entropy([system_data['disk_iops'], system_data['fan_speed_rpm']])
    
    # Create decoy matrix for redundancy analysis (dead code)
    decoy_config = [[1, 0, 1], [1, 0, 1], [0, 1, 0]]
    _ = analyze_redundancy(decoy_config)
    
    # Real processing begins here
    performance_metrics = {
        'latency_ms': system_data['latency_ms'],
        'cpu_load': system_data['cpu_load'],
        'mem_usage_mb': system_data['mem_usage_mb'],
        'disk_iops': system_data['disk_iops']
    }
    
    weights = [0.3, 0.25, 0.25, 0.2]
    
    # Key statement
    final_score = evaluate_performance(performance_metrics, weights)
    
    print(f"Target result: {final_score}")