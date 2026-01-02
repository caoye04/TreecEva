def analyze_pattern(sequence, mode='compact'):
    if mode == 'compact':
        return sum(1 for x in sequence if x % 2 == 0)
    else:
        return sum(x for x in sequence if x > 0)

# Irrelevant helper (decoy)
def compute_shadow_index(data):
    shadow = 0
    for i, val in enumerate(data):
        shadow += (i * val) % 7
    return shadow  # Never used in main logic

# Misleading preprocessing block (dead path)
temp_buffer = [3, 6, 9, 12]
decoys = []
for index, item in enumerate(temp_buffer):
    if item % 3 == 0 and index < 5:
        decoys.append(item * 2 - index)

# Unused transformation map
transform_map = {k: v for k, v in zip(['a', 'b', 'c'], [10, 20, 30])}

# Core data setup
base_sequence = [x**2 - 3*x + 2 for x in range(8)]

# Distractor: fake filter that looks important
filtered_mask = []
for val in base_sequence:
    if val > 5:
        filtered_mask.append(True)
    else:
        filtered_mask.append(False)

# Real but obscured processing begins
segment_a = [x for x in base_sequence if x >= 0]
segment_b = [x for x in base_sequence if x < 10]

# Another red herring: complex-looking but unused bitwise calculation
cross_signal = 0
for i, (a, b) in enumerate(zip(segment_a, segment_b)):
    cross_signal ^= (a & b) + i

def process_segments(data_list, config):
    total = 0
    flags = [False] * len(data_list)
    
    for idx, entry in enumerate(data_list):
        if idx % 2 == 0:
            adjustment = config.get('offset', 0)
            total += entry * 2 + adjustment
        else:
            if config['active']:
                total -= sum([entry % n for n in range(2, 4)])  # Fixed range
    return total

# Decoy data structure
class DiagnosticTrace:
    def __init__(self):
        self.entries = []
        self.validated = False

    def add_entry(self, val):
        self.entries.append(val)

trace_log = DiagnosticTrace()

# Actual threshold configuration (looks configurable but is fixed)
thresholds = {
    'offset': 5,
    'active': True,
    'mode': 'strict'
}

# Data assembly with enumerate misdirection
collected_data = []
for i, val in enumerate(segment_b):
    if i % 3 != 2:  # Skips every third index
        collected_data.append(val + (i % 4))

# Hidden dependency: final_tally depends only on this call
final_tally = process_segments(collected_data, thresholds)

# Additional distraction: recursive function not involved
def trace_depth(n):
    if n <= 1:
        return 1
    return n + trace_depth(n // 2)

# Final irrelevant operation
diagnostic_sum = sum([len(str(x)) for x in decoys])

print(f"Result: {final_tally}")