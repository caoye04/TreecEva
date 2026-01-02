from collections import defaultdict
import math

# Simulate wave interference patterns in a sensor grid
def analyze_sensor_readings(readings):
    frequency_bins = defaultdict(int)
    phase_offsets = []
    temp_magnitude = 0

    for idx, (signal, freq, phase) in enumerate(readings):
        frequency_bins[freq] += 1
        if freq > 15:
            adjusted_phase = (phase + idx * 0.5) % (2 * math.pi)
            phase_offsets.append(adjusted_phase)
            temp_magnitude += abs(math.sin(adjusted_phase))

    # Irrelevant magnitude accumulation (distractor)
    total_energy = sum([x[0]**2 for x in readings])
    normalized_energy = total_energy / len(readings) if readings else 0

    return frequency_bins, phase_offsets, normalized_energy


def generate_phase_mapping(phases):
    # Create coordinate-phase map using enumerate and zip
    coords = list(enumerate(['A', 'B', 'C', 'D', 'E']))
    labeled_phases = [p % (math.pi) for p in phases]
    
    # Misleading data transformation
    temp_map = {label: (idx + 1) * phase for idx, label in coords for phase in labeled_phases[:1]}
    
    # Actual useful mapping
    phase_dict = {}
    for i, p in enumerate(labeled_phases):
        key = chr(65 + i % 5)  # A-E labels
        phase_dict[key] = phase_dict.get(key, 0) + p
    
    return phase_dict


def calculate_interference(phase_map, signal_grid):
    net_phase_shift = 0
    interference_count = 0
    
    # Nested loop with distractors
    for row_idx, row in enumerate(signal_grid):
        for col_idx, cell in enumerate(row):
            char_key = chr(65 + (row_idx + col_idx) % 5)
            if char_key in phase_map:
                base_shift = phase_map[char_key]
                # Real contribution to answer
                net_phase_shift += math.cos(base_shift) * (row_idx + 1)
                
                # Distractor computation (never used)
                local_entropy = -sum([
                    p * math.log(p) for p in [0.1, 0.2, 0.7] if p > 0
                ])
                interference_count += 1
    
    # Final adjustment
    net_phase_shift = int(abs(net_phase_shift * 100)) % 97
    return net_phase_shift

# Main execution
if __name__ == "__main__":
    raw_readings = [
        (2.3, 20, 0.8), (1.7, 10, 1.2), (3.1, 25, 2.1),
        (2.9, 30, 0.9), (1.8, 12, 1.8), (3.5, 40, 2.3)
    ]
    
    bins, phases, energy = analyze_sensor_readings(raw_readings)
    
    # Use enumerate and zip to create synthetic grid
    phase_cycle = [phases[i] if i < len(phases) else 0.5 for i in range(4)]
    row_labels = ['R1', 'R2', 'R3', 'R4']
    col_labels = ['C1', 'C2', 'C3', 'C4']
    signal_grid = [
        [a ^ b for b in [1, 0, 1, 0]] 
        for a in [0, 1, 0, 1]
    ]
    
    # Construct phase map
    phase_map = generate_phase_mapping(phase_cycle)
    
    # Introduce dead code path (distractor)
    if False:
        backup_shift = 0
        for k, v in phase_map.items():
            backup_shift += ord(k) ^ int(v)

    # Key statement
    net_phase_shift = calculate_interference(phase_map, signal_grid)
    
    print(f"Result: {net_phase_shift}")