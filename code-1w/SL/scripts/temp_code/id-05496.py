import itertools

# System health monitoring simulation with signal transformation and noise filtering
def collect_signals(sources):
    raw_signals = []
    for src in sources:
        if src['type'] == 'primary':
            raw_signals.append(src['reading'] * 2.5)
        elif src['type'] == 'secondary':
            raw_signals.append(src['reading'] * 1.2)
    return raw_signals

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_normalization(signal_list):
    return [round(x / max(signal_list), 3) for x in signal_list]

# Signal transformation with combinatorial expansion
def generate_harmonics(basic_signal, depth=2):
    harmonics = []
    for i in range(1, depth + 3):
        harmonics.append(basic_signal * i)
    return harmonics

# Main pattern analysis engine
def analyze_pattern(data_sequence, mask):
    cumulative_score = 0
    temp_buffer = []

    # Real computation begins here
    for val in data_sequence:
        adjusted = int(val ^ mask)  # Bitwise XOR with mask
        if adjusted > 100:
            adjusted = adjusted // 2
        temp_buffer.append(adjusted)

    # Secondary processing: filter and accumulate
    filtered = [x for x in temp_buffer if x % 3 == 1]
    cumulative_score += sum(filtered)

    # Use of itertools: grouping by parity (meaningful but partially distracting)
    sorted_vals = sorted(filtered, key=lambda x: x % 2)
    grouped = {k: list(g) for k, g in itertools.groupby(sorted_vals, key=lambda x: x % 2)}

    if 1 in grouped:
        cumulative_score -= sum(grouped[1]) // 2  # Adjust for odd-group inflation

    # Final nonlinear transformation
    if cumulative_score > 0:
        cumulative_score = int((cumulative_score ** 0.5) * 2.718)  # Approximate e multiplier

    return cumulative_score

# Decoy function: looks important but unused
def compute_entropy(arr):
    from math import log
    total = sum(arr)
    probs = [x / total for x in arr if x > 0]
    return -sum(p * log(p) for p in probs)

# Simulated sensor network configuration
sensor_array = [
    {'id': 'S01', 'type': 'primary', 'reading': 42},
    {'id': 'S02', 'type': 'secondary', 'reading': 88},
    {'id': 'S03', 'type': 'primary', 'reading': 37},
    {'id': 'S04', 'type': 'secondary', 'reading': 91},
    {'id': 'S05', 'type': 'primary', 'reading': 63}
]

# Step 1: Collect raw signals
readings = collect_signals(sensor_array)

# Step 2: Apply harmonic generation on first reading (distraction)
harmonics_pool = []
for r in readings[:2]:
    harmonics_pool.extend(generate_harmonics(r))

# Step 3: Transform main dataset using harmonic offsets (real path)
base_value = sum(readings) // len(readings)
transformed_data = [int(base_value + h * 0.1) for h in generate_harmonics(base_value, depth=1)]

# Step 4: Initialize bit mask based on system ID checksum (relevant)
system_id = "DIAG-7XG"
checksum = 0
for ch in system_id:
    checksum ^= ord(ch)
base_mask = (checksum & 15) | 10  # Ensure non-zero lower nibble

# Step 5: Analyze pattern - KEY EXECUTION POINT
final_diagnostic = analyze_pattern(transformed_data, base_mask)

# Spurious entropy calculation (red herring)
decoy_analysis = compute_entropy([len(harmonics_pool), len(transformed_data), base_mask])

# Output the target result
print(f"Result: {final_diagnostic}")