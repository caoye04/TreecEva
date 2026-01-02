import math

def analyze_growth_pattern(data, threshold):
    # Irrelevant helper function (dead code path)
    return sum(x > threshold for x in data) * 0.5

def normalize_readings(readings):
    # Unused normalization function (distractor)
    mean_val = sum(readings) / len(readings)
    return [round((x - mean_val) / mean_val * 100, 2) for x in readings]

def evaluate_resilience_factor(x, y):
    # Decoy computation with bit manipulation red herring
    temp_a = (x ^ y) << 2
    temp_b = (x & 0xFF) | (y >> 3)
    return (temp_a - temp_b) % 7

def compute_root_density(sequence):
    # Distracting scientific-looking calculation
    if len(sequence) == 0:
        return 0
    base = sum(math.sqrt(abs(val)) for val in sequence if val > 0)
    penalty = len([v for v in sequence if v < -5])
    return round(base - penalty, 3)

def calculate_harvest_efficiency(metrics, cycles):
    total_efficiency = 0.0
    adjustment_factor = 1.0
    
    # Real logic begins: process each cycle's cluster data
    for i, record in enumerate(cycles):
        phase_weight = record['weight']
        growth_rate = record['rate']
        stress_index = record.get('stress', 0)
        
        # Core accumulation logic
        if growth_rate > 0:
            contribution = phase_weight * math.log(growth_rate + 1)
            total_efficiency += contribution
        
        # Conditional adjustment using ternary-like expression
        adjustment_factor *= 0.95 if stress_index > 3 else 1.02
    
    # Combine with metric score (only one key metric matters)
    key_metric = metrics['photosynthetic_yield']  # Critical value
    secondary_metric = metrics['root_depth_score']  # Irrelevant
    decoy_metric = metrics['leaf_width_variance']  # Red herring
    
    # Final formula - only photosynthetic_yield is actually used
    raw_result = total_efficiency * key_metric
    final_score = raw_result * adjustment_factor
    
    # Apply rounding to match expected precision
    return round(final_score, 4)

# Main execution block
if __name__ == "__main__":
    # Distractor dataset - includes unused fields and misleading names
    cluster_metrics = {
        'photosynthetic_yield': 8.7,
        'root_depth_score': 6.4,
        'leaf_width_variance': 12.3,
        'stomatal_conductance': 4.1,
        'transpiration_ratio': 9.8
    }

    # Growth cycle data - relevant input
    growth_cycles = [
        {'weight': 0.3, 'rate': 2.1, 'stress': 2},
        {'weight': 0.4, 'rate': 3.5, 'stress': 4},
        {'weight': 0.3, 'rate': 4.2, 'stress': 5}
    ]

    # Irrelevant pre-processing (distractor chain)
    sensor_readings = [102, 98, 110, 95, 105]
    normalized = [x * 1.02 for x in sensor_readings]  # Unused
    resilience = evaluate_resilience_factor(150, 78)  # Computed but unused

    # Simulated root analysis (dead end)
    test_sequence = [4.2, -1.0, 8.5, -6.3, 3.1]
    density = compute_root_density(test_sequence)

    # Actual key computation
    final_yield = calculate_harvest_efficiency(cluster_metrics, growth_cycles)

    # Print result as required
    print(f"Target result: {final_yield}")