from itertools import compress, cycle

# System parameters (some are red herrings)
base_frequency = 440.0
modulation_index = 12.5
decay_constant = 0.87
threshold_limit = 987
noise_floor = -120
core_channels = [3, 5, 7, 11, 13]

# Signal transmission diagnostic data
signal_strengths = [0.21, 0.45, 0.68, 0.33, 0.77, 0.54, 0.89, 0.12]
phase_offsets = [0.1, -0.3, 0.4, -0.2, 0.6, -0.5, 0.8, -0.7]
packet_losses = [0, 1, 0, 0, 2, 1, 0, 3]

def analyze_channel_integrity(loss_log):
    # Irrelevant analysis function (dead end)
    total_loss = sum(loss_log)
    peak_loss = max(loss_log)
    loss_ratio = total_loss / (len(loss_log) * 3) if total_loss > 0 else 0
    return {'total': total_loss, 'peak': peak_loss, 'ratio': loss_ratio}

def generate_harmonic_sequence(base, count):
    # Distractor function - not used in final computation
    return [round(base * (1.5 ** i)) for i in range(count)]

def validate_transmission_window(signal_list, threshold):
    # Misleading validation that isn't actually used
    window_energy = sum([s**2 for s in signal_list])
    return window_energy > threshold

# Unused but plausible intermediate calculations
harmonics = generate_harmonic_sequence(base_frequency, 8)
validation_result = validate_transmission_window(signal_strengths, threshold_limit)
channel_metrics = analyze_channel_integrity(packet_losses)

# Critical data transformation chain
adjusted_signals = []
for i, strength in enumerate(signal_strengths):
    phase_factor = abs(phase_offsets[i])
    adjusted = strength * (1 - phase_factor * 0.5)  # Signal degradation model
    if packet_losses[i] > 0:
        adjusted *= (0.9 - packet_losses[i] * 0.1)  # Additional loss factor
    adjusted_signals.append(round(adjusted, 3))

# Data masking with itertools (relevant)
valid_indices = [s > 0.1 for s in adjusted_signals]
filtered_signals = list(compress(adjusted_signals, valid_indices))

# Complex weighting using cycling pattern (core logic)
weight_pattern = cycle([0.8, 1.0, 1.2])
weighted_sum = 0.0
for i, sig in enumerate(filtered_signals):
    weight = next(weight_pattern)
    weighted_sum += sig * weight

# Secondary processing on core channels (partially relevant)
effective_bandwidth = 0
for channel in core_channels:
    if channel in [3, 5, 7]:  # Only first three matter
        effective_bandwidth += channel * 10

# Composite transmission chain (key structure)
transmission_chain = {
    'nodes': len(filtered_signals),
    'amplitude': max(filtered_signals),
    'stability': min(filtered_signals),
    'bandwidth': effective_bandwidth,
    'variance': weighted_sum
}

def calculate_efficiency(chain):
    # Multi-step efficiency calculation with embedded logic
    node_factor = chain['nodes'] * 2.5
    amplitude_contribution = chain['amplitude'] * 100
    stability_penalty = 50 * (1 - chain['stability'])
    
    # Bandwidth scaling with diminishing returns
    if chain['bandwidth'] > 100:
        bandwidth_factor = 100 + (chain['bandwidth'] - 100) * 0.25
    else:
        bandwidth_factor = chain['bandwidth'] * 0.8
    
    # Variance bonus (higher is better in this context)
    variance_bonus = chain['variance'] * 1.5
    
    # Final efficiency score - this is the answer
    efficiency = (node_factor + amplitude_contribution - stability_penalty + 
                bandwidth_factor + variance_bonus)
    
    # Red herring: this adjustment is never applied
    if efficiency > 1000:
        efficiency = efficiency * 0.95  # hypothetical compression
    
    return round(efficiency, 4)

# Execution point of interest
efficiency_score = calculate_efficiency(transmission_chain)

# Distraction: unused performance matrix
performance_matrix = [
    [base_frequency, modulation_index], 
    [decay_constant, noise_floor]
]

# Final output
print(f"Result: {efficiency_score}")