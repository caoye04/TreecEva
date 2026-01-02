import math

# Simulated system telemetry and diagnostic processing
# with extensive red herrings and irrelevant transformations
timing_log = [127, 255, 193, 64, 240, 111, 89, 176]
system_flags = [True, False, True, True, False]

# Irrelevant data structures (distractors)
user_cache = {'temp': 42, 'debug_mode': False, 'retry_count': 7}
error_stack = [(500, 'timeout'), (404, 'not_found')]
metadata_map = {k: k * 2 for k in range(10)}

# Decoy functions that are never called
def decrypt_payload(data):
    return [d ^ 255 for d in data]

def validate_checksum(seq):
    return sum(seq) % 256 == 0

# Unused transformation pipelines
transform_chain = [
    lambda x: x + 10,
    lambda x: x * 2 if x < 100 else x // 3,
    lambda x: abs(x - 50)
]

# Fake signal processor (dead code path)
class SignalProcessor:
    def __init__(self):
        self.buffer = []
    def process(self, data):
        return [d & 0x7F for d in data]

# Misleading intermediate calculations
shadow_copy = [x for x in timing_log if x > 100]
mask_sequence = [int(math.log2(x)) if x > 0 else 0 for x in shadow_copy]
checksum_probe = sum(mask_sequence) % 16

# Dummy state tracker with no real effect
state_tracker = []
for idx, val in enumerate(timing_log):
    if val % 16 == 0:
        state_tracker.append((idx, val // 16))

# Real logic buried under distractions
filter_threshold = 192
filtered_peaks = list(filter(lambda x: x > filter_threshold, timing_log))

# Bit manipulation red herring
bit_analysis = 0
for p in filtered_peaks:
    bit_analysis ^= (p << 2) | (p >> 6)

# Conditional data routing (partially relevant)
if len(system_flags) > 3 and system_flags[0]:
    scale_factor = 3
else:
    scale_factor = 5

# Core calculation obscured by context
baseline = sum(filtered_peaks) // len(filtered_peaks) if filtered_peaks else 0
adjustment = sum(1 for f in system_flags if f) * scale_factor

# Multiple assignments with one key variable
intermediate_a = baseline * adjustment
intermediate_b = 14  # magic constant from config
hybrid_metric = intermediate_a + (intermediate_b << 1)

# Tuple unpacking distraction
dummy_vals = (100, 200, 300)
x, y, z = dummy_vals

# String-based decoy processing
log_signature = ''.join([chr(val % 97 + 33) for val in timing_log[:4]])
encoded_sig = ''.join(sorted(log_signature))

# Actual answer computation deeply nested
reference_key = 7
for item in timing_log:
    if item > reference_key:
        reference_key = (reference_key + item) % 50

# Critical statement buried in noise
final_diagnostic = hybrid_metric - reference_key

# Additional red herring: unused list comprehension
snapshot_diff = [timing_log[i] - timing_log[i-1] for i in range(1, len(timing_log))]

# Output the target result
print(f"Target result: {final_diagnostic}")