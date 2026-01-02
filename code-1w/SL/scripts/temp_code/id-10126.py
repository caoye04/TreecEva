from collections import defaultdict, Counter
import math

# Simulated sensor node network with redundant diagnostics
def simulate_node_diagnostics(raw_readings):
    diagnostics = defaultdict(int)
    temp_stats = [x for x in raw_readings if x > 0]
    avg_temp = sum(temp_stats) / len(temp_stats) if temp_stats else 0
    
    # Irrelevant diagnostic flags (red herring)
    diagnostics['voltage_stable'] = True
    diagnostics['humidity_alert'] = False
    diagnostics['calibration_offset'] = avg_temp * 0.17
    
    return int(avg_temp)

# Legacy function for deprecated system (dead code path)
def legacy_capacity_calc(nodes, threshold=32):
    count = 0
    for n in nodes:
        if n > threshold:
            count += 1
    return count * 0.85  # Not used in current logic

def analyze_pattern_sequencing(data_stream):
    pattern_counter = Counter()
    sequence_peaks = []
    
    for i, val in enumerate(data_stream):
        if val % 7 == 0 and val > 0:
            pattern_counter['divisible_by_7'] += 1
        if val > 50:
            sequence_peaks.append(i)
    
    # Misleading metric
    false_peak_density = len(sequence_peaks) / (len(data_stream) or 1)
    
    # Actual relevant result disguised among noise
    return pattern_counter['divisible_by_7']

# Core thermal modeling engine
def evaluate_thermal_load(matrix, factor):
    base_load = 0
    adjustment = 0
    
    for row in matrix:
        row_sum = 0
        for elem in row:
            if elem < 0:
                continue
            row_sum += math.sqrt(elem) + (elem * 0.3)
        
        if row_sum > 100:
            adjustment += 12.5
        elif row_sum > 50:
            adjustment += 5.0
        
        base_load += row_sum
    
    # Apply non-linear efficiency scaling
    final_load = (base_load + adjustment) * factor
    
    # Decoy operations
    final_load += math.sin(math.pi / 6)  # Constant addition: 0.5
    final_load *= 1.0  # No-op multiplier
    
    return int(final_load)

# --- Main Execution ---
if __name__ == "__main__":
    # Sensor data from geothermal array
    readings = [45, -12, 67, 23, 89, 0, 121, 54, 78, 33, 91]
    
    # Irrelevant preprocessing step
    processed_nodes = [x for x in readings if x % 2 == 1]  # Odd values only
    node_diagnostic = simulate_node_diagnostics(readings)
    
    # Construct cluster matrix (core input)
    cluster_matrix = [
        [16, 25, 36],
        [49, 64, 81],
        [100, 121, 144]
    ]
    
    # Efficiency derived from pattern analysis
    efficiency_factor = (analyze_pattern_sequencing(readings) + node_diagnostic) / 100.0
    
    # Secondary decoy calculation
    phantom_load = 0
    for i in range(len(cluster_matrix)):
        phantom_load += sum(cluster_matrix[i]) * 0.01  # Minor distraction
    
    # Key assignment - target intervention point
    thermal_capacity = evaluate_thermal_load(cluster_matrix, efficiency_factor)
    
    # Additional misleading computation
    capacity_margin = thermal_capacity * 0.02
    compliance_status = capacity_margin < 5
    
    # Final output
    print(f"Result: {thermal_capacity}")