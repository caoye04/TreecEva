from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated system telemetry data
current_voltage = [3.28, 3.31, 3.29, 3.33, 3.30]
phase_shifts = [0.12, 0.15, 0.10, 0.14, 0.11]
packet_sequence = [101, 205, 303, 409, 502]

# Irrelevant signal processing (red herring)
def process_harmonics(data):
    harmonics = []
    for x in data:
        harmonics.append(x * 2 + 0.5)
    return [h % 1.0 for h in harmonics]

harmonic_noise = process_harmonics(phase_shifts)  # Dead-end computation

# System log with diagnostic flags
event_codes = ['OK', 'WARN', 'OK', 'ERROR', 'OK', 'WARN']
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800, 1623456805]
log_entries = list(zip(timestamps, event_codes))

# Misleading auxiliary function (not used in final calculation)
def compute_signal_quality(voltages, shifts):
    avg_v = sum(voltages) / len(voltages)
    coherence = 1 / (sum(shifts) + 1)
    return avg_v * coherence

# Unused but plausible-looking analysis
dummy_metric = compute_signal_quality(current_voltage, phase_shifts)

# System flags from various subsystems
power_flags = [True, False, True, True, False]
thermal_warnings = [0, 1, 0, 2, 1]
checksum_valid = [True, True, False, True, True]

# Aggregation using defaultdict (relevant)
system_flags = defaultdict(int)
for i, flag in enumerate(power_flags):
    system_flags['power'] += int(flag)
for temp in thermal_warnings:
    system_flags['thermal'] += temp
for chk in checksum_valid:
    system_flags['integrity'] += int(chk)

# Complex distractor: nested unused transformation
def deep_evaluate(seq, voltages):
    acc = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            acc += val ^ int(voltages[i % len(voltages)] * 100)
        else:
            acc -= (val >> 2)
    return acc % 1000

phantom_score = deep_evaluate(packet_sequence, current_voltage)  # Red herring value

# Core diagnostic logic with tuple unpacking and enumeration
status_weights = {'OK': 1, 'WARN': -2, 'ERROR': -5}

def analyze_log_severity(entries, weights):
    total = 0
    for ts, status in entries:
        total += weights.get(status, 0)
    return total

severity_index = analyze_log_severity(log_entries, status_weights)

# Data alignment using zip_longest (relevant usage)
aligned_data = list(zip_longest(current_voltage, phase_shifts, fillvalue=0.0))
vector_sum = sum(v * (1 + p) for v, p in aligned_data)

# Primary analysis function combining multiple concepts
def analyze_system_state(entries, flags):
    # Step 1: Base severity from logs
    base_risk = analyze_log_severity(entries, {'OK': 1, 'WARN': -2, 'ERROR': -5})
    
    # Step 2: Adjust by flag intensities
    power_factor = flags['power'] * 3
    thermal_factor = flags['thermal'] ** 2
    integrity_bonus = flags['integrity'] if flags['integrity'] > 3 else -4
    
    # Step 3: Apply nonlinear transformation
    risk_amplifier = abs(base_risk) ** 0.5 if base_risk != 0 else 1
    
    # Step 4: Combine all factors
    intermediate = (power_factor + thermal_factor) * risk_amplifier
    final = intermediate + integrity_bonus - vector_sum
    
    # Step 5: Corrective threshold clamp
    if final < -100:
        final = -100
    elif final > 1000:
        final = 999 + (final % 10)  # Subtle trap avoided
    
    # Final adjustment using character count from status messages (hidden relevance)
    status_text = ''.join([code for _, code in entries])
    char_count = Counter(status_text)
    final += char_count['R'] * 7  # Only 'R' matters
    
    return int(round(final))

# Execute main analysis
final_diagnostic = analyze_system_state(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")