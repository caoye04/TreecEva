from collections import defaultdict
import statistics

def process_waveform(amplitude_data):
    # Stage 1: Group amplitudes by their magnitude categories
    magnitude_groups = defaultdict(list)
    for amp in amplitude_data:
        category = amp // 10
        magnitude_groups[category].append(amp)
    
    # Stage 2: Calculate statistical signatures for each group
    signatures = {}
    for category, values in magnitude_groups.items():
        if len(values) > 1:
            mean_val = int(statistics.mean(values))
            variance_val = int(statistics.variance(values))
            # Combine using bitwise operations
            signatures[category] = (mean_val << 4) ^ variance_val
        else:
            signatures[category] = values[0] << 2
    
    # Stage 3: Aggregate signatures with weighted combination
    aggregate = 0
    for i, (category, sig) in enumerate(sorted(signatures.items())):
        weight = (i + 1) & 0b111  # Bitwise AND with 7
        adjusted_sig = sig >> (i & 0b11)  # Right shift by 0-3 positions
        aggregate ^= (adjusted_sig * weight)
    
    return aggregate

# Input waveform data
waveform_measurements = [12, 18, 25, 22, 31, 37, 45, 42, 58, 63, 66, 71]

# Execute processing pipeline
processed_signature = process_waveform(waveform_measurements)
print(f"Result: {processed_signature}")