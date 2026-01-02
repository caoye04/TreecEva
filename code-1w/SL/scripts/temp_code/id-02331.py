import itertools

# Simulated telemetry data from satellite subsystems
telemetry_streams = [
    [0.85, 0.91, 0.76, 0.88, 0.90],
    [0.67, 0.72, 0.65, 0.70, 0.68],
    [0.95, 0.93, 0.97, 0.96, 0.94]
]

# Irrelevant auxiliary data (distractor)
spectrum_analysis = {
    'band_a': [0.12, 0.15, 0.11],
    'band_b': [0.08, 0.09, 0.10],
    'band_c': [0.05, 0.04, 0.06]
}

# System health thresholds (used later)
thresholds = {
    'critical': 0.70,
    'warning': 0.85,
    'optimal': 0.90
}

# Simulated log entries with diagnostic codes (core input)
log_entries = [
    {'timestamp': 1001, 'code': 200, 'power': 0.88},
    {'timestamp': 1002, 'code': 201, 'power': 0.82},
    {'timestamp': 1003, 'code': 404, 'power': 0.76},
    {'timestamp': 1004, 'code': 200, 'power': 0.91},
    {'timestamp': 1005, 'code': 503, 'power': 0.69}
]

# System flags indicating component status (core input)
system_flags = {
    'comms': True,
    'propulsion': False,
    'solar': True,
    'cooling': True
}

# Decoy function – appears important but unused in critical path
def analyze_spectrum(data):
    total = 0
    for band in data.values():
        for val in band:
            total += val ** 2
    return total * 1000

# Auxiliary transformation – looks relevant but not used in final calculation
temporal_weights = [0.1, 0.2, 0.3, 0.4, 0.5]
weighted_telemetry = []
for stream in telemetry_streams:
    weighted = [stream[i] * temporal_weights[i] for i in range(len(stream))]
    weighted_telemetry.append(sum(weighted))

# Red herring: complex-looking but irrelevant computation
aggregated_signal = 0
for i, w in enumerate(weighted_telemetry):
    aggregated_signal += w * (1.5 ** i)
aggregated_signal = round(aggregated_signal, 3)  # Dead end

# Real processing begins here — hidden among distractions
def evaluate_power_stability(entries):
    stable_count = 0
    for entry in entries:
        if entry['power'] >= thresholds['optimal']:
            stable_count += 1
    return stable_count > 2

# Another real function — determines fault severity
def count_errors(entries):
    errors = 0
    for entry in entries:
        if entry['code'] != 200:  # Assume 200 = healthy
            errors += 1
    return errors

# Bit manipulation decoy (looks sophisticated but unused)
def encode_status(flags):
    encoded = 0
    encoded |= (1 if flags['comms'] else 0)
    encoded |= (2 if flags['propulsion'] else 0)
    encoded |= (4 if flags['solar'] else 0)
    encoded |= (8 if flags['cooling'] else 0)
    return encoded << 2  # Unused return

# Real logic: assess redundancy from telemetry (not actually used in final path)
redundant_systems = 0
for t_stream in telemetry_streams:
    high_performers = [x for x in t_stream if x >= thresholds['optimal']]
    if len(high_performers) >= 3:
        redundant_systems += 1

# Critical path starts here — well-hidden
operational_modes = list(itertools.product([0, 1], repeat=3))  # Mode combinations
active_mode = operational_modes[len(log_entries) % len(operational_modes)]  # Deterministic selection

# Core diagnostic processor
mode_score = 0
if active_mode[0]:
    mode_score += 10
if not active_mode[1]:
    mode_score += 15
if active_mode[2] and system_flags['comms']:
    mode_score += 25
else:
    mode_score += 5

# Actual answer derivation chain
error_count = count_errors(log_entries)
is_stable = evaluate_power_stability(log_entries)

# Secondary distraction: fake fusion algorithm
fusion_data = []
for a, b in itertools.combinations_with_replacement([1, 2, 3], 2):
    fusion_data.append((a * b) + 1)
fusion_score = sum(fusion_data) // 3  # Looks important, unused

# Final computation — depends on error count, stability, and mode
base_diagnostic = 100
if error_count == 0:
    base_diagnostic += 50
elif error_count <= 2:
    base_diagnostic -= 20 * error_count
else:
    base_diagnostic -= 50

if is_stable:
    base_diagnostic += 30

# Mode adjustment only if propulsion is offline
if not system_flags['propulsion']:
    base_diagnostic += mode_score
else:
    base_diagnostic -= 10

# Key assignment statement
final_diagnostic = process_metrics(log_entries, system_flags)

# Wrapper to simulate modular design (distraction)
def process_metrics(entries, flags):
    # Recompute inside function to obscure flow
    err = 0
    for e in entries:
        if e['code'] != 200:
            err += 1
    stable = True
    high_count = 0
    for e in entries:
        if e['power'] >= 0.90:
            high_count += 1
    if high_count < 3:
        stable = False
    
    score = 100
    if err == 0:
        score += 50
    elif err <= 2:
        score -= 20 * err
    else:
        score -= 50
    
    if stable:
        score += 30
    
    if not flags['propulsion']:
        internal_mode = operational_modes[len(entries) % len(operational_modes)]
        add = 0
        if internal_mode[0]:
            add += 10
        if not internal_mode[1]:
            add += 15
        if internal_mode[2] and flags['comms']:
            add += 25
        else:
            add += 5
        score += add
    else:
        score -= 10
    
    return score

# Print final result as required
Target result: {final_diagnostic}