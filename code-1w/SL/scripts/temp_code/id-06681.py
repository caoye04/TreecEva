from collections import defaultdict
import math

def analyze_signal_strength(raw_readings):
    strength_log = defaultdict(int)
    total_power = 0
    peak_magnitude = 0

    for reading in raw_readings:
        if reading > 50:
            strength_log['high'] += 1
            total_power += reading * 1.2
        elif reading > 20:
            strength_log['medium'] += 1
            total_power += reading * 0.8
        else:
            strength_log['low'] += 1
            total_power += reading * 0.3

        if reading > peak_magnitude:
            peak_magnitude = reading

    efficiency_ratio = (total_power / len(raw_readings)) / (peak_magnitude + 1e-5)
    return total_power, efficiency_ratio


def quantize_signal(value, levels=256):
    normalized = abs(value) / 100.0
    return int(normalized * (levels - 1))


def process_phases(signals):
    phase_stack = []
    temp_correction = 0
    base_offset = math.pi / 4

    for idx, sig in enumerate(signals):
        angle = base_offset * sig
        sine_component = math.sin(angle)
        cosine_component = math.cos(angle)
        
        # Irrelevant intermediate tracking
        harmonic = 1 if idx % 2 == 0 else -1
        dummy_state = harmonic * sine_component
        
        if sine_component > 0.5:
            phase_stack.append(1)
        elif sine_component < -0.5:
            phase_stack.append(-1)
        else:
            phase_stack.append(0)

    # Actual logic affecting result
    net_phase_shift = sum(phase_stack) * 0.25

    # Distractor computation — not used later
    avg_phase = sum(phase_stack) / len(phase_stack) if phase_stack else 0
    variance = sum((p - avg_phase) ** 2 for p in phase_stack) / len(phase_stack) if phase_stack else 0

    final_adjustment = net_phase_shift + temp_correction  # temp_correction always 0

    # Misleading print that looks important
    debug_info = f'Debug: shift={net_phase_shift}, var={variance:.3f}'

    return final_adjustment

# Main execution block
raw_data = [85, 42, 67, 15, 91, 33, 74]
total_power, efficiency = analyze_signal_strength(raw_data)

# Quantize signals based on raw data
quantized_signals = [quantize_signal(x, 16) for x in raw_data]

# Introduce irrelevant transformation
inverted_signals = [15 - q for q in quantized_signals]  # unused later

# Core processing step
final_adjustment = process_phases(quantized_signals)

# Extract target variable
net_phase_shift = final_adjustment * 4  # Reverse scaling to recover internal state

# Print final result as required
print(f"Result: {net_phase_shift}")