import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [384, 257, 512, 193, 446]
filter_threshold = 200
smoothing_factor = 0.85

# Irrelevant transformation - red herring
adjusted_metrics = [math.log(x + 1) * smoothing_factor for x in raw_readings if x > filter_threshold]

# Core signal extraction (relevant)
valid_sensors = set()
for idx, val in enumerate(raw_readings):
    if val % 2 == 1:
        valid_sensors.add(idx)

dropped_sensors = {0, 2, 4}  # Hardcoded drop (decoy)
active_sensors = valid_sensors - dropped_sensors

# Misleading statistical summary
mean_adjusted = sum(adjusted_metrics) / len(adjusted_metrics)
variance_proxy = sum((x - mean_adjusted) ** 2 for x in adjusted_metrics) / len(adjusted_metrics)

# Data transformation pipeline
bit_shifted = []
for val in raw_readings:
    processed = (val ^ 255) & 511  # XOR and mask
    bit_shifted.append((processed << 1) % 1024)

def apply_window(data, window_size=3):
    """Simple moving average window - not actually used in final path"""
    result = []
    for i in range(len(data) - window_size + 1):
        result.append(sum(data[i:i+window_size]) // window_size)
    return result

# Actual relevant transformation chain
def transform_signal(seq, mode='dual'):
    temp_buffer = []
    for item in seq:
        if mode == 'dual':
            phase_a = (item + 7) % 31
            phase_b = (phase_a ^ 15) | 4
            temp_buffer.append(phase_b)
        else:
            temp_buffer.append(item * 2)
    return [x for x in temp_buffer if x % 2 == 0]  # Filter even only

def generate_checksum(values):
    """Irrelevant checksum function - dead code path"""
    chk = 0
    for v in values:
        chk = (chk * 13 + v) % 10007
    return chk

def encrypt_sequence(keys, seed=11):
    """Unused encryption routine - distractor"""
    encrypted = []
    key_state = seed
    for k in keys:
        key_state = (key_state * 7 + k) % 1024
        encrypted.append(key_state ^ k)
    return encrypted

transformed_data = transform_signal(bit_shifted)

# Configuration structure with misleading fields
class Config:
    def __init__(self):
        self.debug_mode = True
        self.max_iterations = 100
        self.threshold = 42.5
        self.flags = [True, False, True]
        self.payload_limit = 2048
        self.algorithm_variant = 'v3'
        self.mask_bits = 0b1101

config = Config()

# Secondary decoy computation
if config.debug_mode:
    debug_snapshot = []
    for i in range(5):
        snapshot_val = (i ** 3 + 17) % 100
        debug_snapshot.append(snapshot_val)

# Unused nested structure
temp_analysis = {
    'stage1': {'status': 'complete', 'code': 200},
    'stage2': {'status': 'skipped', 'code': 404},
    'final': {'status': 'pending', 'code': None}
}

# Real analysis logic (buried among distractions)
def evaluate_entropy(sequence):
    total = 0
    for i, val in enumerate(sequence):
        contribution = (val * (i + 1)) % 19
        total += contribution
    return total % 1000

def analyze_pattern(data, cfg):
    base_score = evaluate_entropy(data)
    
    # Conditional manipulation based on config (only one field matters)
    modifier = 1
    if hasattr(cfg, 'algorithm_variant'):
        if cfg.algorithm_variant == 'v3':
            modifier = 3
    
    intermediate = base_score * modifier
    
    # Bit manipulation layer
    shifted_intermediate = (intermediate << 2) & 0xFFFF
    masked = shifted_intermediate ^ 0x5A5A
    folded = (masked >> 8) ^ (masked & 0xFF)
    
    # Final adjustment using modular arithmetic
    final_value = (folded * 7 + 13) % 50000
    
    # Dead code branch - looks important but unused
    if final_value > 10000:
        fallback = 0
        for b in bin(final_value).count('1'):
            fallback += b * 2
        final_value = fallback  # Never reached
    
    return final_value

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, config)
print(f"Target result: {final_diagnostic}")