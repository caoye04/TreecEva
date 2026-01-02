import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Misleading transformation chain
def transform_signal(data):
    temp = [d * 1.5 for d in data]
    shifted = [t + 7 for t in temp]  # Distractor: not used later
    return [round(t % 10) for t in temp]

# Unused state tracker
class StateMonitor:
    def __init__(self):
        self.log = []
        self.count = 0

    def update(self, val):
        self.log.append(val)
        self.count += 1

# Core processing logic
def process_data(buffer, cfg):
    # Extract parameters
    scale = cfg.get('scale', 1)
    offset = cfg.get('offset', 0)
    mode = cfg.get('mode')

    # Irrelevant bit manipulation (misleading intermediate)
    magic_key = 0x1F
    mask = (magic_key << 2) ^ 0xA
    dummy_hash = (len(buffer) + scale) & mask

    # Real computation begins
    filtered = [x for x in buffer if x > 0]  # Only positive values
    adjusted = [x * scale + offset for x in filtered]

    # Lambda-based conditional boost
    booster = lambda v: v * 1.1 if v < 50 else v
    boosted = [booster(val) for val in adjusted]

    # Slicing to extract working segment
    working_slice = boosted[1:-1] if len(boosted) > 4 else boosted

    # Accumulation with min/max guardrails
    capped = [min(max(w, 10), 90) for w in working_slice]
    total = sum(capped)

    # Final adjustment using trigonometric red herring
    angle = math.pi / 6
    fake_weight = math.sin(angle)  # Looks important, not actually used

    # Actual final step
    if mode == 'secure':
        final_value = int(total // 1.8)
    else:
        final_value = int(total // 1.2)

    return final_value

# Simulated sensor data (mixture of relevant and irrelevant)
raw_stream = [-5, 12, 18, -3, 27, 45, 53, -1, 39, 8]
noise_floor = 0.7
baseline_shift = noise_floor * 10

# Apply meaningless pre-processing
shifted_raw = [r + baseline_shift for r in raw_stream]
transformed = transform_signal(shifted_raw)

# Define configuration
config = {
    'scale': 2,
    'offset': 5,
    'mode': 'normal',
    'debug': True,
    'timeout': 300
}

# Main buffer after fake transformations
stream_buffer = [int(x) for x in shifted_raw]  # Revert to integers

# Tracking variables (unused)
monitor = StateMonitor()
for val in stream_buffer:
    if val % 2 == 0:
        monitor.update(val)

# Key execution point
final_output = process_data(stream_buffer, config)

# Output result
print(f"Result: {final_output}")