import math

# Irrelevant helper functions (dead code paths)
def legacy_normalize(x):
    return x / (1 + abs(x))

def compute_legacy_score(data):
    return sum(d * 0.7 for d in data) % 100

def debug_snapshot(state):
    temp = [s ** 2 for s in state if s > 0]
    checksum = sum(temp) % 59
    return checksum  # Unused result

# Core processing pipeline
config = {
    'threshold': 42,
    'scaling_factor': 1.618,
    'activation': lambda x: math.log(abs(x) + 1) * 0.5,
    'filters': [lambda x: x > 0, lambda x: x % 2 == 0]
}

raw_signals = [34, -15, 67, 23, 89, 44, 13, 72]
offset_correction = 5

# Apply irrelevant transformation
shifted_data = [x - offset_correction for x in raw_signals]

# Distractor: complex but unused signal smoothing
def smooth_signal(signal, passes=3):
    buf = signal[:]
    for _ in range(passes):
        buf = [(buf[i-1] + buf[i] + buf[(i+1) % len(buf)]) / 3 for i in range(len(buf))]
    return buf

smoothed = smooth_signal(shifted_data)  # Computed but not used

# Relevant transformation path
filtered_data = [x for x in raw_signals if x > 20]
squared_magnitude = sum(x ** 2 for x in filtered_data)
scale_hint = squared_magnitude // 1000  # Used later

# Bit manipulation red herring
temp_flag = 0b101010
mask_result = temp_flag & 0b111100 ^ 0b001100  # Distractor

# Actual transformation chain
transformed_data = []
for val in filtered_data:
    if val % 3 == 0:
        transformed_data.append(math.sqrt(val))
    elif val % 5 == 0:
        transformed_data.append(val / 2.5)
    else:
        transformed_data.append(abs(math.sin(val)))

# Another decoy structure
class DataVault:
    def __init__(self, data):
        self.data = data
        self.locked = True

    def unlock(self, key):
        return [d ^ key for d in self.data]  # Never called

vault = DataVault([1, 2, 3])  # Created but unused

# Real processing function
def process_metrics(data, cfg):
    activated = list(map(cfg['activation'], data))
    valid = [v for v in activated if not math.isnan(v)]
    
    # Simulate conditional override based on scale_hint (from earlier)
    if scale_hint > 8:
        reduction = lambda x: x * 0.9
    else:
        reduction = lambda x: x * 1.1
    
    adjusted = [reduction(v) for v in valid]
    
    # Final aggregation with case-sensitive flag check
    flag_code = 'BETA'
    case_converted = ''.join([c.lower() if c in 'AEIOU' else c for c in flag_code])
    
    if case_converted == 'bETa':
        final_weight = 1.05
    else:
        final_weight = 0.98  # This branch triggers
    
    aggregate = sum(adjusted) * final_weight
    
    # Sorting distraction
    sorted_adj = sorted(adjusted, reverse=True)
    median_offset = sorted_adj[len(sorted_adj)//2] * 0.02  # Minor perturbation
    
    return math.floor(aggregate - median_offset)

# Critical execution point
final_diagnostic = process_metrics(transformed_data, config)
print(f"Result: {final_diagnostic}")