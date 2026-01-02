from collections import defaultdict
import math

# Simulate wave interference in a sensor array with phase correction

def generate_frequency_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            # Real signal component with spatial modulation
            base_freq = (i + 1) * (j + 1)
            modulated = base_freq * 0.7 + math.sin(i * 0.5) * math.cos(j * 0.3)
            row.append(round(modulated, 6))
        grid.append(row)
    return grid


def calculate_phase_correction(sensor_id, ambient_temp, humidity):
    # Complex environmental compensation (only partially relevant)
    temp_factor = (ambient_temp - 20) * 0.03
    humid_factor = (humidity - 50) * 0.002
    base_shift = math.atan2(sensor_id + 1, 4.0)
    return base_shift + temp_factor - humid_factor


def detect_edge_peaks(signal_sequence):
    # Find local maxima (used to mask certain frequencies)
    peaks = []
    seq_len = len(signal_sequence)
    for i in range(1, seq_len - 1):
        if signal_sequence[i] > signal_sequence[i-1] and signal_sequence[i] > signal_sequence[i+1]:
            peaks.append(i)
    return peaks


def calculate_interference_pattern(grid, phase_offsets):
    size = len(grid)
    cumulative = 0.0
    phase_map = defaultdict(float)
    
    # Apply phase offsets using enumerate
    for idx, offset in enumerate(phase_offsets):
        phase_map[idx] = offset * (idx % 3 + 1)
    
    # Mask selection based on peak detection (creates red herring)
    sample_signal = [sum(row) / len(row) for row in grid]
    significant_peaks = detect_edge_peaks(sample_signal)
    masked_indices = set(significant_peaks)  # Not actually used in final calculation
    
    # Introduce distractor variables
    temp_amplitude_log = []
    total_elements_processed = 0
    energy_sum = 0.0
    
    for i, row in enumerate(grid):
        row_contribution = 0.0
        for j, freq in enumerate(row):
            weight = math.cos(math.pi * i / size) * math.sin(math.pi * j / size)
            adjusted_freq = freq * (1 + math.sin(phase_map.get(j, 0)))
            row_contribution += adjusted_freq * weight
            
            # Distractor computation (not affecting final result)
            instant_power = adjusted_freq ** 2 * (i + j + 1)
            energy_sum += instant_power
            
        cumulative += row_contribution * (i + 1)
        total_elements_processed += len(row)
    
    # Secondary distractor: combinatorial coefficient unrelated to main logic
    combo_factor = 0
    for i in range(1, min(size, 6)):
        combo_factor += math.comb(8, i) // (i + 1)  # Dead-end calculation
    
    # Final interference metric
    raw_interference = cumulative * 0.85
    
    # Normalize by virtual path count (distractor division)
    normalization_proxy = math.log(total_elements_processed + 1) or 1
    normalized_result = raw_interference / normalization_proxy
    
    # Final answer variable
    net_phase_shift = int(round(normalized_result))
    
    # Irrelevant print (simulates debugging)
    debug_flag = False
    if debug_flag:
        print(f'Combo factor: {combo_factor}, Energy: {energy_sum}')
    
    return net_phase_shift

# Main execution
if __name__ == '__main__':
    sensor_array_size = 5
    environment_temp = 22.5
    air_humidity = 58
    
    frequency_grid = generate_frequency_grid(sensor_array_size)
    
    # Generate phase offsets per channel
    phase_offsets = [
        calculate_phase_correction(i, environment_temp, air_humidity)
        for i in range(sensor_array_size)
    ]
    
    # Critical statement
    net_phase_shift = calculate_interference_pattern(frequency_grid, phase_offsets)
    
    # Output target result
    print(f"Result: {net_phase_shift}")