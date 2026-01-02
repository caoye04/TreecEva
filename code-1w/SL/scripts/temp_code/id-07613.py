from collections import defaultdict
import math

def preprocess_readings(sensor_data):
    filtered = [x for x in sensor_data if x > -273.15]
    avg = sum(filtered) / len(filtered)
    return [round(x - avg, 2) for x in filtered]

def generate_fusion_key(temp_profile):
    key_sequence = []
    for i, t in enumerate(temp_profile):
        if i % 3 == 0:
            key_sequence.append(int(t ** 0.5) if t >= 0 else 0)
        elif i % 3 == 1:
            key_sequence.append(int(abs(t) % 7))
        else:
            key_sequence.append(int(t // 4))
    return key_sequence

def calculate_thermal_capacity(fusion_matrix):
    # Core logic starts here
    rows = len(fusion_matrix)
    cols = len(fusion_matrix[0])
    capacity = 0
    
    # Heat distribution coefficients (irrelevant to final result but adds distraction)
    dummy_coeffs = [math.sin(i * 0.1) for i in range(rows)]
    normalization_factor = sum(abs(c) for c in dummy_coeffs) or 1
    adjusted_values = []
    
    for r in fusion_matrix:
        adjusted_row = [val * 1.05 for val in r]  # Distractor transformation
        adjusted_values.append(adjusted_row)
    
    # Real computation begins
    temp_aggregate = defaultdict(int)
    for i in range(rows):
        for j in range(cols):
            cell_val = fusion_matrix[i][j]
            if cell_val > 0:
                temp_aggregate['positive'] += cell_val
            elif cell_val < 0:
                temp_aggregate['negative'] += abs(cell_val)
    
    net_energy = temp_aggregate['positive'] - temp_aggregate['negative']
    
    # Secondary distractor: unused signal analysis
    signal_peaks = []
    for row in fusion_matrix:
        for k in range(1, len(row) - 1):
            if row[k-1] < row[k] > row[k+1]:
                signal_peaks.append(row[k])
    peak_avg = sum(signal_peaks) / len(signal_peaks) if signal_peaks else 0
    
    # Final capacity calculation with slicing distraction
    edge_sum = 0
    for i in range(rows):
        if len(fusion_matrix[i]) >= 3:
            left_slice = fusion_matrix[i][:2]
            right_slice = fusion_matrix[i][-2:]
            edge_sum += sum(left_slice) + sum(right_slice)
    
    # Actual answer depends only on net_energy and fixed offset
    thermal_capacity = abs(net_energy) + 17  # Final deterministic result
    
    # Print required output
    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Simulated experimental data (real input)
sensor_readings = [32.5, -10.0, 45.0, -273.15, 18.3, 0.0, 99.9, -5.2]
processed = preprocess_readings(sensor_readings)
profile_matrix = [
    [processed[i] + processed[j] for j in range(4)] 
    for i in range(4)
]
fusion_key = generate_fusion_key(processed)
fusion_matrix = [
    [profile_matrix[i][j] + (fusion_key[i] if i < len(fusion_key) else 0) for j in range(4)]
    for i in range(4)
]

# Key execution point
thermal_capacity = calculate_thermal_capacity(fusion_matrix)