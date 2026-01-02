from collections import defaultdict
import math

def calculate_phase(buffer, limit):
    stats = defaultdict(int)
    total_power = 0
    
    for val in buffer:
        if val > limit:
            stats['strong'] += 1
            total_power += val ** 2
        elif val == limit:
            stats['neutral'] += 1
        else:
            stats['weak'] += 1

    avg_power = total_power / stats['strong'] if stats['strong'] else 0
    
    # Irrelevant debug counter (minimal distraction)
    debug_count = 0
    for k in stats:
        debug_count += len(k)

    normalized = math.sqrt(avg_power) if avg_power > 0 else 0
    phase_shift = int(normalized % 7) * 3
    return phase_shift

# Signal data from sensor array
signal_buffer = [1.5, 3.0, 4.5, 2.0, 5.5, 6.0, 4.0]
threshold = 3.5

# Extra unused variable (low interference)
baseline_offset = 2.1

phase_shift = calculate_phase(signal_buffer, threshold)
print(f"Result: {phase_shift}")