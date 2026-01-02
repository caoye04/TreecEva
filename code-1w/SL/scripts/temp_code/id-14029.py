def transform_signal(raw_values, scale_factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    transformed = []
    for v in raw_values:
        if v < 0:
            transformed.append(-1 * (abs(v) ** 0.5))
        else:
            transformed.append(v ** 0.5)
    return [round(x * scale_factor, 3) for x in transformed]


def validate_checksum(data_str):
    """Compute modular checksum for data integrity (partially relevant)"""
    total = 0
    for char in data_str:
        total += ord(char) % 7
    return total % 13


def generate_triplet_sequence(n):
    """Generate Fibonacci-like triplet sums (red herring)"""
    if n <= 0:
        return []
    seq = [1, 1, 1]
    for i in range(3, n):
        seq.append(seq[i-1] + seq[i-2] + seq[i-3])
    return seq[:n]

# Simulated sensor data from environmental monitoring array
temperature_readings = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9]
humidity_readings = [45, 48, 50, 55, 53, 49, 47]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1011, 1014]

# Irrelevant transformation path (dead code branch)
signal_data = [16, 25, 36, 49, 64]
distorted_signal = transform_signal(signal_data, 1.73)

# Data encoding metadata (distractor)
encoding_scheme = {
    'A': '00', 'B': '01', 'C': '10', 'D': '11',
    'prefix_len': 2,
    'version': '2.1-beta'
}

# Real processing begins here — subtle entry into relevant logic
data_packets = [
    'ENV2023A', 'ENV2023B', 'ENV2024A', 'ENV2024C',
    'CAL2023X', 'DBG9999Z'  # Mixed valid/invalid prefixes
]

classified_labels = set()
valid_prefixes = set()
for packet in data_packets:
    prefix = packet[:3]
    if prefix == 'ENV':
        classified_labels.add(packet[3:7])  # Extract year
    elif prefix == 'CAL':
        continue  # Ignore calibration packets
    else:
        valid_prefixes.add(prefix)

device_modes = {f'mode_{i}': i**2 for i in range(1, 6)}
mode_offset = sum(device_modes.values()) % 11  # = 55 % 11 = 0

# Core data structure initialization
processed_data = []
for i in range(len(temperature_readings)):
    entry = (
        round(temperature_readings[i] + humidity_readings[i] / 10, 2),
        (pressure_readings[i] - 1000) % 20,
        i % 4
    )
    processed_data.append(entry)

# Threshold configuration map (critical for final computation)
threshold_map = {
    'temp_hum': 28.5,
    'pressure_mod': {j: (j * 3 + mode_offset) for j in range(4)},
    'sequence_mask': generate_triplet_sequence(4),  # [1,1,1,3] — used later
    'safe_range': set(range(8, 18))  # Valid pressure deltas
}

# Auxiliary diagnostic function with mixed relevance
def evaluate_stability(metrics, config):
    score = 0
    pressure_mod_vals = config['pressure_mod']
    mask = config['sequence_mask']

    for idx, (th, pm, qtr) in enumerate(metrics):
        base_score = 0
        if th > config['temp_hum']:
            base_score += 2
        if pm in config['safe_range']:
            base_score += 1
        # Key use of tuple unpacking and conditional expression
        bonus = mask[qtr] if qtr < len(mask) else 0
        mod_adjust = pressure_mod_vals.get(qtr, 0)
        score += base_score * (1 + bonus / 10.0) + mod_adjust
    return round(score, 4)

# Secondary validation using string methods (actually irrelevant)
active_sensors = [p for p in data_packets if p.startswith('ENV') and p.endswith(('A','B'))]
status_flag = ''.join([s[-1] for s in active_sensors]).lower()
flag_checksum = sum(ord(c) - ord('a') for c in status_flag)

# Unused recursive helper (decoy)
def recursive_reduce(n, acc=0):
    if n <= 1:
        return acc
    return recursive_reduce(n - 1, acc + (n % 4))

# Final analysis function that determines the answer
def analyze_readings(data_set, limits):
    aggregate = 0.0
    sequence = limits['sequence_mask']  # [1,1,1,3]
    pressure_keyed = limits['pressure_mod']  # {0:0,1:3,2:6,3:9}

    for i, (combo_temp, press_delta, quarter) in enumerate(data_set):
        # Primary arithmetic contribution
        temp_excess = max(0, combo_temp - limits['temp_hum'])

        # Boolean logic with short-circuit and containment check
        is_critical = press_delta < 5 or (press_delta > 15 and quarter in {1, 3})

        # Bit manipulation on index (irrelevant but looks important)
        magic_factor = (i ^ 5) & 7  # Results in values like 5,4,7,2,...

        # Conditional expression with tuple-based dispatch
        fallback = (i % 2 + 1) * 1.5
        dynamic_weight = sequence[quarter] if quarter < len(sequence) else fallback

        # Core calculation — only this contributes meaningfully
        base_increment = temp_excess * dynamic_weight
        adjustment = pressure_keyed.get(quarter, 0)

        # Aggregate only this component
        aggregate += base_increment + adjustment

    # Final transformation using set operation (size determines offset)
    extra_offset = len(classified_labels.intersection({'2023', '2024'})) * 2  # = 2 * 2 = 4

    result = aggregate + extra_offset
    return round(result, 4)

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")