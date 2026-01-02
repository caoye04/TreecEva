from itertools import cycle, islice

def generate_reference(signal_length, noise_factor=0.1):
    return [((i % 7) + 1) * noise_factor for i in range(signal_length)]

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) / (mean_val + 1e-5) < threshold]

def apply_mask(sequence, pattern):
    masked = []
    for val, mask in zip(sequence, cycle(pattern)):
        masked.append(val ^ mask if mask > 0 else val)
    return masked

def integrate_signals(primary, secondary):
    integrated = 0
    for a, b in zip(primary, secondary):
        integrated += int(a + b) % 5
    return integrated

def adjust_phase(seq, offset):
    shifted = list(islice(cycle(seq), offset, offset + len(seq)))
    base_score = sum(shifted[i] * (i + 1) for i in range(len(shifted)))
    
    # Irrelevant preprocessing branch
    temp_buffer = [x * 1.5 for x in shifted if x % 2 == 0]
    buffer_sum = sum(temp_buffer)  # Used nowhere critical
    
    # Dummy state tracking
    state_log = []
    accumulator = 0
    for idx, val in enumerate(shifted):
        if idx % 3 == 0:
            accumulator += val
        elif idx % 4 == 0:
            accumulator -= val // 2
        state_log.append(accumulator % 100)  # Distractor log
    
    # Core logic
    magnitude = sum(abs(x) for x in shifted)
    parity_check = magnitude % 2
    phase_adjustment = (base_score // 10) + parity_check
    
    # Secondary irrelevant computation
    histogram = {i: 0 for i in range(10)}
    for v in shifted:
        bin_idx = min(v // 2, 9)
        histogram[bin_idx] += 1
    
    # Final result influenced only by base_score and parity
    final_phase = phase_adjustment * 3 + (1 if parity_check else -1)
    
    return final_phase

# Main execution flow
reference_noise = generate_reference(12, 0.25)
clean_signal = filter_outliers(reference_noise, threshold=1.8)
mask_pattern = [1, 0, 3, 2]
processed_data = apply_mask(clean_signal, mask_pattern)
sync_pulse = [int(x * 4) for x in processed_data]

# Dummy integration to create interference
dummy_integration = integrate_signals(processed_data, sync_pulse)
baseline_shift = sum(sync_pulse) // len(sync_pulse)

# Key variables
base_sequence = [int(x * 2) for x in processed_data if x > 0.5]
calibration_offset = len(base_sequence) % 11

# Critical statement
final_phase = adjust_phase(base_sequence, calibration_offset)

print(f"Result: {final_phase}")