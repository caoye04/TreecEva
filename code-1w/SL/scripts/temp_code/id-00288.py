import math

def analyze_frequency(data):
    # Irrelevant frequency analysis (distractor)
    magnitude = sum([abs(x) for x in data])
    avg_magnitude = magnitude / len(data) if data else 0
    spectral_peak = max(data) ** 2 if data else 0
    return avg_magnitude  # Not used in final result

def validate_checksum(sequence):
    # Dead function: looks important but not part of logic chain
    checksum = 0
    for item in sequence:
        checksum ^= item
    return checksum == 0xFF

def transform_entry(val, mode):
    if mode == 'hex':
        return val ^ (val << 2) & 0xFF
    elif mode == 'bin':
        return val | (val >> 1)
    return val

def process_signals(data, cfg):
    temp_cache = {}
    state_log = []
    accumulator = 0
    flag_tracker = {'active': False, 'count': 0}

    # Initialize processing pipeline
    filtered = [x for x in data if x > cfg['threshold']]
    
    # Distractor: complex-looking but unused transformation
    transformed = [transform_entry(y, 'hex') for y in filtered]
    normalized = [z / 10.0 for z in transformed if z > 0]  # Unused

    # Real logic begins
    stats = {
        'sum': sum(filtered),
        'len': len(filtered),
        'max': max(filtered) if filtered else 0
    }

    # Bit manipulation chain
    raw_value = stats['sum'] ^ 0x5A5A
    shifted = (raw_value >> 3) & 0xFFFF
    adjusted = shifted + stats['len'] * 2

    # Conditional path with early return red herring
    if adjusted > 1000:
        dummy = math.log(adjusted, 2)
        state_log.append('high_range')
        # But we don't return here — misleading!

    # Actual key computation
    intermediate = adjusted
    for i in range(stats['len']):
        if i % 2 == 0:
            intermediate += i * 3
        else:
            intermediate -= i

    # Dictionary-based routing (relevant)
    mode_map = {'A': 10, 'B': 20, 'C': 30}
    mode_bonus = mode_map.get(cfg['mode'], 5)

    # Final composition
    candidate_1 = intermediate + mode_bonus
    candidate_2 = stats['max'] * 5 + 17

    # Critical decision point
    if stats['sum'] % 2 == 0:
        final_choice = candidate_1
    else:
        final_choice = candidate_2

    # One last adjustment
    final_output = (final_choice + 1) // 2  # Integer division

    # Dead branch: never reached due to logic
    if False and flag_tracker['active']:
        final_output = -1

    return final_output

# Main execution
if __name__ == '__main__':
    signal_data = [12, 45, 23, 67, 34, 89, 21]
    config = {
        'threshold': 20,
        'mode': 'B',
        'version': '2.1',
        'debug': True
    }

    # Spurious pre-computations (distractors)
    baseline = sum(signal_data) / len(signal_data)
    deviation = [abs(x - baseline) for x in signal_data]
    entropy = math.fsum([d * d for d in deviation]) / len(deviation) if deviation else 0

    # Trigger analysis (unused)
    _ = analyze_frequency(signal_data)

    # Key execution point
    final_output = process_signals(signal_data, config)

    # Output result
    print(f"Result: {final_output}")