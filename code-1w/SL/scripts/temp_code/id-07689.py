from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_frequency(data):
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1
    return freq

# Unused transformation map (red herring)
transform_map = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'X': 99, 'Y': 100, 'Z': 101  # Distracting high values
}

# Misleading signal weights (not used in final computation)
signal_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
weight_offsets = [w * 1.5 for w in signal_weights]

# Dummy encryption round (dead code path)
def dummy_encrypt(block, rounds=3):
    for _ in range(rounds):
        block = (block ^ 0xABCDEF) % 10007
    return block

# Actual core logic: signal processor
def generate_sequence(seed, length):
    seq = []
    val = seed
    for i in range(length):
        val = (val * 7 + 13) % 101
        seq.append(val)
    return seq

def modulate_phase(signal, phase_shift):
    return [(s * phase_shift) % 97 for s in signal]

def apply_mask(signal, mask):
    return [s ^ mask[i % len(mask)] for i, s in enumerate(signal)]

def compute_checksum(data):
    chk = 0
    for d in data:
        chk = (chk + d * 31) % 1009
    return chk

# Complex nested processing chain
def process_transmission(signals, schedule):
    temp_debug_log = []  # Logged but unused
    intermediate_results = []
    
    # Layer 1: Generate base sequence
    base = generate_sequence(schedule[0], len(signals))
    
    # Layer 2: Modulate with dynamic phase
    phase_val = (schedule[1] + schedule[2]) % 89
    modulated = modulate_phase(base, phase_val)
    
    # Layer 3: Apply XOR mask derived from schedule
    mask_key = compute_checksum(schedule) % 256
    masked = apply_mask(modulated, [mask_key ^ i for i in range(10)])
    
    # Layer 4: Cross-correlate with input signals
    correlated = []
    for i in range(len(signals)):
        corr_val = (masked[i] + signals[i]) % 100
        if corr_val > 50:
            # Conditional bit manipulation
            corr_val = (corr_val << 1) ^ 0b1101
        else:
            corr_val = (corr_val >> 1) | 0b1010
        correlated.append(corr_val)
    
    # Layer 5: Accumulate with modular reduction
    accumulator = 0
    for idx, val in enumerate(correlated):
        if idx % 2 == 0:
            accumulator += val * 2
        else:
            accumulator -= val
        accumulator = accumulator % 5000  # Keep bounded
    
    # Final checksum fusion
    final_integrity = compute_checksum(correlated)
    final_signal = (accumulator + final_integrity) % 10000
    
    # DEAD-END DEBUG BLOCK (distractor)
    debug_dump = {
        'raw_signals': signals[:3],
        'base_seq_sample': base[:3],
        'temp_check': compute_checksum(base),
        'phantom_metric': sum(weight_offsets) * 100  # Misleading metric
    }
    
    return final_signal

# Orchestration block
if __name__ == '__main__':
    # Input setup
    transmission_data = [12, 45, 67, 23, 89, 14]
    encryption_schedule = [17, 23, 41]
    
    # Unused string analysis (irrelevant)
    raw_header = "HDR|PRIO|CHKSUM|MODE4"
    header_parts = raw_header.split('|')
    header_length = len(header_parts)
    priority_flag = header_parts[1] == 'PRIO'
    
    # Another decoy list comprehension
    [math.sqrt(x) for x in range(1, 5)]  # No side effect
    
    # Key execution point
    final_signal = process_transmission(transmission_data, encryption_schedule)
    
    # Output result as required
    print(f"Result: {final_signal}")