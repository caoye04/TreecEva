def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count


def shift_elements(arr, offset=2):
    offset = offset % len(arr) if arr else 0
    return arr[offset:] + arr[:offset]


def evaluate_threshold(values, limit=15):
    total = sum(v for v in values if v < limit)
    return total if total % 2 == 0 else total + 1


def extract_features(data_str):
    cleaned = data_str.strip().lower().replace("_", "")
    parts = [int(c, 16) for c in cleaned if c.isalnum()]
    return sorted(parts, reverse=True)


def merge_chunks(a, b):
    result = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        result.append(a[i] ^ b[i])
    result.extend(a[min_len:])
    result.extend(b[min_len:])
    return result

# Irrelevant helper (dead function)
def format_report(code, version="A1"):
    header = f"REPORT-{version}:\n"
    body = "\n".join([f"Line {i}: {line}" for i, line in enumerate(code.split(';'))])
    return header + body

# Misleading intermediate processing
raw_signal = [7, 2, 9, 1, 5, 8, 3]
decoy_state = {k: v**2 for k, v in enumerate(raw_signal)}
baseline = sum(raw_signal) // len(raw_signal)
adjusted_signal = [x - baseline for x in raw_signal]
sorted_signal = sorted(adjusted_signal)

# Distractor: complex string transformation with no impact
data_blob = "a3c7b2d9e1"
feature_vector = extract_features(data_blob)

# Real computation begins
primary_chunk = [x * 2 for x in raw_signal if x % 2 == 1]
secondary_chunk = shift_elements(primary_chunk, 3)

# Conditional expression used
mode_flag = 'advanced' if sum(primary_chunk) > 30 else 'basic'
config_mask = [1, 0, 1, 1] if mode_flag == 'advanced' else [0, 1, 0, 1]

# Another decoy structure
temp_log = {
    'status': 'processed',
    'items': len(feature_vector),
    'checksum': sum(f * (i+1) for i, f in enumerate(feature_vector)) % 100
}

# Actual relevant logic
transformed_chunk = []
for i, val in enumerate(secondary_chunk):
    if i % 2 == 0:
        transformed_chunk.append(val + config_mask[i % len(config_mask)])
    else:
        transformed_chunk.append(val - config_mask[i % len(config_mask)])

# Nested conditional with early exit potential
def process_data(chunk):
    if not chunk:
        return -1
    
    temp_val = 0
    for idx, num in enumerate(chunk):
        if idx == 0 and num < 0:
            return 0
        elif idx == 2:
            temp_val = temp_val * num if num != 0 else temp_val + 5
        else:
            temp_val += (num ** 2) % 7
    
    # Final adjustment using modular arithmetic
    final_val = (temp_val + len(chunk)) % 1331
    return final_val

# Critical execution point
final_output = process_data(transformed_chunk)

# Unused but misleading variables
correlation_map = {i: transformed_chunk[i] * transformed_chunk[-i-1] for i in range(len(transformed_chunk))}
aggregated_score = evaluate_threshold(transformed_chunk)
peak_count = analyze_pattern(transformed_chunk)

# Output target result
print(f"Result: {final_output}")