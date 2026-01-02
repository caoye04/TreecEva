from collections import defaultdict
from itertools import cycle

# Simulate a signal processing pipeline with state tracking
def analyze_signal_sequence(raw_readings):
    reading_stats = defaultdict(int)
    total_power = 0
    spike_count = 0
    noise_floor = 0.87
    phase_offset = -3

    # Irrelevant histogram for amplitude bands (distractor)
    amplitude_bands = defaultdict(int)
    
    for val in raw_readings:
        if val > noise_floor:
            spike_count += 1
            total_power += val ** 2
        reading_stats['processed'] += 1
        if val < 0.1:
            reading_stats['near_zero'] += 1

        # Distractor: categorizing into bands not used later
        band = int(val * 10)
        amplitude_bands[band] += 1

    efficiency_ratio = (spike_count / len(raw_readings)) if raw_readings else 0

    # Core logic begins: frequency cycle analysis
    base_frequency = len(raw_readings) % 7
    cycles = cycle([1, -1, 0])
    cycle_count = 0
    for _ in range(base_frequency * 3):
        cycle_state = next(cycles)
        if cycle_state == 0:
            cycle_count += 2
    
    # Secondary path: buffer simulation (semi-relevant)
    buffer_delay = 0
    temp_buffer = [0]*5
n    for i in range(len(temp_buffer)):
        buffer_delay += (i * phase_offset) % 4
    buffer_delay = buffer_delay // 5

    # Key computation chain
    raw_baseline = sum(1 for x in raw_readings if x > 0.5)
    adjusted_base = raw_baseline ^ 5  # Bitwise adjustment
    adjusted_base = abs(adjusted_base - 3)  # Normalize

    # Critical statement
    final_flux = adjusted_base * (cycle_count + phase_offset)

    # Red herring: unused transformation
    normalized_flux = round(final_flux / (efficiency_ratio + 0.1), 2) if efficiency_ratio else 0

    # Output required result
    print(f"Result: {final_flux}")

# Input data
input_readings = [0.92, 0.15, 0.67, 0.33, 0.88, 0.04, 0.71]
analyze_signal_sequence(input_readings)