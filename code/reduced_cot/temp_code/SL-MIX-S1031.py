from collections import namedtuple

# Define a configuration for our digital signal processing
SignalConfig = namedtuple('SignalConfig', ['base_freq', 'amplitude_mod'])
config = SignalConfig(base_freq=42, amplitude_mod=7)

# Simulate incoming signals with their properties
incoming_signals = [
    {'id': 'SIG_A', 'phase': 3, 'strength': 120},
    {'id': 'SIG_B', 'phase': 5, 'strength': 95},
    {'id': 'SIG_C', 'phase': 2, 'strength': 150}
]

# Process signals through a series of logical and arithmetic operations
processed_signals = {
    sig['id']: ((sig['strength'] ^ config.base_freq) & 0xFF) + (sig['phase'] << 2)
    for sig in incoming_signals
}

# Apply further modifications based on conditions
adjusted_signals = {
    k: v | (config.amplitude_mod << 4) if v > 100 else v & ~(0xF)
    for k, v in processed_signals.items()
}

# Calculate aggregate metrics
signal_sum = sum(adjusted_signals.values())
peak_signal = max(adjusted_signals.values())

# Final adjustment using short-circuit evaluation and compound operations
final_signal_strength = (
    (signal_sum + peak_signal) >> 1
) if signal_sum and peak_signal > 100 else 0

print(f'Result: {final_signal_strength}')