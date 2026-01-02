from collections import defaultdict
import math

# Irrelevant helper function (dead code path)
def calculate_noise_floor(signal_strength):
    return math.log(signal_strength + 1e-9, 2) if signal_strength > 0 else -float('inf')

# Misleading utility with decoy logic
def analyze_packet_jitter(timestamps):
    jitter_sum = 0
    for i in range(1, len(timestamps)):
        diff = abs(timestamps[i] - timestamps[i-1])
        jitter_sum += diff * 1.5  # Red herring calculation
    normalized_jitter = jitter_sum / (len(timestamps) + 1)
    return normalized_jitter  # Not used in main logic

# Unused data structure (distractor)
legacy_system_data = {
    'nodes': [0x1A, 0x2B, 0x3C],
    'checksum': lambda x: sum(x) ^ 0xFF,
    'version': 'deprecated'
}

# Simulated transmission dataset with realistic naming
transmissions = [
    {'id': 'T001', 'power': 85, 'phase': 0.3, 'encoded': True},
    {'id': 'T002', 'power': 92, 'phase': 1.2, 'encoded': False},
    {'id': 'T003', 'power': 76, 'phase': 0.8, 'encoded': True},
    {'id': 'T004', 'power': 88, 'phase': 1.6, 'encoded': True}
]

# Frequency mapping with nested structure (relevant and distractor keys)
frequency_map = defaultdict(lambda: 'unknown')
frequency_map.update({
    'band_a': {'freq': 2.4e9, 'mod': 'QAM16', 'active': True},
    'band_b': {'freq': 5.8e9, 'mod': 'OFDM', 'active': True},
    'backup_c': {'freq': 900e6, 'mod': 'FSK', 'active': False}  # Inactive band
})

# Extraneous list processing (irrelevant computation)
temp_phases = []
for t in transmissions:
    adjusted_phase = t['phase'] * 180 / math.pi
    temp_phases.append(adjusted_phase + 45)  # Fake transformation

# Decoy counter (looks important but unused in final result)
decoded_packet_count = 0
for packet in transmissions:
    if packet['encoded']:
        decoded_packet_count += 1  # Distraction

# Real processing begins here — deeply nested and mixed with prior noise
active_bands = []
for key, config in frequency_map.items():
    if config['active']:
        active_bands.append(config['freq'])

# Core signal integration logic (correct path)
signal_base = 0
for entry in transmissions:
    if entry['power'] > 80:
        signal_base += int(entry['power'] * entry['phase'])

# Bit manipulation red herring
obfuscation_key = 0xABCDEF
masked_signal = signal_base ^ obfuscation_key
shifted_mask = (masked_signal >> 4) & 0xFFFF

# Dictionary-based correction factor (uses enumerate and zip)
correction_factors = [0.95, 1.05, 1.1, 0.9]
indexed_transmissions = list(enumerate([t for t in transmissions if t['power'] > 80]))
adjusted_signals = []
for idx, tx in indexed_transmissions:
    raw_contribution = tx['power'] * tx['phase']
    corrected = raw_contribution * correction_factors[idx % len(correction_factors)]
    adjusted_signals.append(corrected)

# Final aggregation using zip and sum
weights = [1.0, 0.8, 1.2]  # Weighting scheme
combined_weighted = 0
for adj, wt in zip(adjusted_signals, weights):
    combined_weighted += adj * wt

# Key state variable built from multiple sources
intermediate_result = int(combined_weighted) & 0xFFFF  # Mask to 16 bits

# Final processing step with conditional override (critical execution point)
final_signal = intermediate_result
if len(active_bands) > 1:
    final_signal = (intermediate_result * 2) // 3
else:
    final_signal = intermediate_result + 1000  # Dead branch due to two active bands

# Print required output
print(f"Result: {final_signal}")