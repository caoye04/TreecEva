import math

def generate_frequency_bands(channels):
    bands = []
    for i in range(channels):
        bands.append(55.5 * (i + 1) + 0.7 * (i % 3))
    return bands

def analyze_harmonic_distortion(band_data):
    distortion = 0.0
    for val in band_data:
        distortion += abs(math.sin(val) * math.cos(val / 2))
    return distortion / len(band_data)

def calculate_interference_phase(frequencies, sequence):
    total_power = 0.0
    phase_accumulator = 0.0
    temp_buffer = []
    
    # Real computation path
    for idx, freq in enumerate(frequencies):
        shift = 0
        for s in sequence:
            shift += (idx + 1) * (s % 4)
        adjusted_shift = shift % 8
        if adjusted_shift % 2 == 0:
            phase_accumulator += math.pi * freq / (adjusted_shift + 1)
        else:
            phase_accumulator -= math.pi * freq / (adjusted_shift + 2)

    # Distractor: power calculation not used in final result
    for f in frequencies:
        raw_power = f ** 2 * 0.01
        thermal_loss = raw_power * 0.05
        total_power += raw_power - thermal_loss
    
    # Distractor: buffer filling with intermediate values
    for i, f in enumerate(frequencies):
        temp_buffer.append(f * (i + 1) * 0.1)
    
    # Distractor: unused combinatorial count
    combo_count = 0
    for i in range(len(frequencies)):
        for j in range(i + 1, len(frequencies)):
            if (frequencies[i] + frequencies[j]) > 100:
                combo_count += 1

    # Final phase adjustment using only phase_accumulator
    net_phase_shift = round(phase_accumulator / math.pi, 4)
    return net_phase_shift

# Main execution block
channel_count = 6
frequency_list = generate_frequency_bands(channel_count)
distortion_level = analyze_harmonic_distortion(frequency_list)

alignment_pattern = [3, 7, 2, 8, 1]
frequency_grid = []
for f in frequency_list:
    frequency_grid.append(round(f + 0.5 * math.log(f), 2))

# Secondary distractor: zipped processing with irrelevant scaling
scaling_factors = [1.1, 0.9, 1.05, 0.95, 1.0, 0.8]
scaled_grid = []
for f, s in zip(frequency_grid, scaling_factors):
    scaled_grid.append(f * s)

buffer_index = {}
for index, value in enumerate(scaled_grid):
    buffer_index[index] = value * 0.77

# Key computational step
net_phase_shift = calculate_interference_phase(frequency_grid, alignment_pattern)

# Output result as required
print(f"Result: {net_phase_shift}")