import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return sum([i * 2 for i in x if i % 3 == 0])

# Decoy transformation chain
def misleading_normalization(data):
    temp = [d + 1.5 for d in data]
    scaled = [t * 0.9 for t in temp]
    return [round(s, 2) for s in scaled]  # Never actually used

# Core logic disguised among distractions
def apply_filter(sequence, mode='A'):
    if mode == 'A':
        return [x for x in sequence if x > 0 and x % 2 == 1]  # Only odd positives
    else:
        return [x for x in sequence if x < 0]

# Lambda-based dynamic operation
transform = lambda z: z ** 2 - 3 * z + 2

# Dummy statistical red herring
def compute_misleading_stats(values):
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    return {'mean': round(mean_val, 4), 'variance': round(variance, 4)}  # Computed but unused

# String processing decoy
tainted_header = "ErrOneous::DaTaStReAm::v2"
header_parts = tainted_header.lower().split("::")
version_flag = header_parts[-1] if len(header_parts) > 2 else 'v1'

class DataStreamProcessor:
    def __init__(self):
        self.buffer = []
        self.checksum = 0
        self.counter = 0

    def ingest(self, raw):
        # Simulate bit manipulation distraction
        processed = []
        for num in raw:
            flipped = num ^ 7  # Bitwise XOR red herring
            shifted = (flipped << 1) & 0xFF  # More bit noise
            processed.append(shifted if shifted != 0 else 1)
        self.buffer = processed

    def integrate(self):
        # Real filtering happens here, masked by complexity
        stage1 = apply_filter(self.buffer, mode='A')
        stage2 = [transform(x) for x in stage1]
        
        # Conditional branch with misleading appearance
        if len(stage2) > 3:
            reduced = stage2[:3]  # Truncate to first three
        else:
            reduced = stage2 + [0]*(3 - len(stage2))
        
        # Dictionary-based dispatch (only one case matters)
        operations = {
            'A': lambda x: x * 2,
            'B': lambda x: x + 5,
            'C': lambda x: int(math.sqrt(abs(x)))
        }
        applied = [operations['A'](n) for n in reduced]  # Only 'A' is used
        
        # Final aggregation with hidden key step
        raw_total = sum(applied)
        adjustment = len(self.buffer) % 4  # Modular arithmetic twist
        final = raw_total - adjustment * 3
        
        # Critical execution point
        final_result = final + 1000  # Offset to avoid small numbers
        return final_result

# Setup with decoys
raw_stream = [-5, -2, 0, 3, 6, 7, 8, 9, 11]
metadata_tags = ['type:B', 'mode:diag', 'level=7']

# Unused combinatorics distraction
def generate_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs  # Computed but not used

all_combinations = generate_pairs(raw_stream)  # Dead computation

# Real processing begins
stream_processor = DataStreamProcessor()
stream_processor.ingest(raw_stream)

# Key statement
final_output = stream_processor.integrate()

# Additional irrelevant string manipulation
formatted_log = "Execution-{}-Complete".format("PASS")
split_log = formatted_log.split('-')
clean_log = ''.join([part.lower() for part in split_log if part.isalpha()])

# Output the answer as required
print(f"Result: {final_output}")