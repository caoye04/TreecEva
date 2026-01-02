def process_readings(data, threshold=5.0):
    temp_cache = []
    cumulative = 0
    for i, val in enumerate(data):
        if val < 0:
            temp_cache.append(abs(val) ** 0.5)
        elif val > threshold:
            temp_cache.append(val * 1.2)
        else:
            temp_cache.append(val + 0.1)
    return [round(x, 3) for x in temp_cache]


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

# Irrelevant helper: computes bit weight (unused in final path)
def bit_weight(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count

# Decoy function: looks important but not used
def validate_checksum(arr):
    total = 0
    for idx, val in enumerate(arr):
        total += val * (idx % 7 + 1)
    return total % 101

# Another red herring: complex string parsing with no downstream use
def parse_metadata(meta_str):
    segments = meta_str.split('|')
    result_map = {}
    for seg in segments:
        if ':' in seg:
            k, v = seg.split(':', 1)
            result_map[k.strip()] = v.strip()
    # Some fake transformations
    if 'version' in result_map:
        result_map['version'] = result_map['version'].replace('.', '_')
    return result_map

# Core logic buried among distractions
def transform_signal(signal, factor):
    shifted = []
    for i, s in enumerate(signal):
        if i % 3 == 0:
            shifted.append(s * factor + 2)
        elif i % 4 == 0:
            shifted.append(s - 1)
        else:
            shifted.append(s * 0.9)
    return shifted

# Unused recursive accumulator
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] + recursive_sum(lst, idx + 1)

# Real data processing chain begins here
raw_data = [2.1, 7.3, -4.4, 3.0, 8.1, -9.2, 1.5]
base_offset = 4

# Step 1: Process raw readings
filtered_data = process_readings(raw_data, threshold=5.0)

# Step 2: Generate auxiliary sequence (used only partially)
aux_seq = generate_sequence(7)

# Step 3: Transform using signal logic
modulated = transform_signal(filtered_data, 1.5)

# Step 4: Create log structure with metadata (some fields irrelevant)
temp_log = []
for i, (m, a) in enumerate(zip(modulated, aux_seq)):
    entry = {
        'index': i,
        'value': m,
        'aux': a,
        'flag': (i % 2 == 0),
        'checksum': m * a + base_offset  # unused field
    }
    temp_log.append(entry)

# Step 5: Aggregate only specific entries — key logic
# Only even-indexed entries where 'value' > 6.0 contribute
contributing = []
dummy_accumulator = 0  # distractor
for record in temp_log:
    dummy_accumulator += record['checksum'] * 0.1  # meaningless accumulation
    if record['index'] % 2 == 0 and record['value'] > 6.0:
        contributing.append(record['value'] * record['aux'])

# Step 6: Compute average of contributions, fallback to 0 if none
if contributing:
    avg_contribution = sum(contributing) / len(contributing)
else:
    avg_contribution = 0

# Final computation — target result
final_diagnostic = 0
scaling_factor = base_offset * 0.25  # evaluates to 1.0
interim = avg_contribution * scaling_factor
final_diagnostic = int(round(interim + 100))  # final answer derived here

print(f"Result: {final_diagnostic}")