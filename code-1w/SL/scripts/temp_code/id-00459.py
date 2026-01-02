import math

# Simulate a phase-shifted signal processing pipeline
def generate_wave(frequency, duration, sample_rate):
    return [math.sin(2 * math.pi * frequency * (i / sample_rate)) for i in range(int(duration * sample_rate))]

# Apply amplitude modulation with carrier frequency
def modulate_am(signal, carrier_freq, sample_rate):
    carrier = [math.cos(2 * math.pi * carrier_freq * (i / sample_rate)) for i in range(len(signal))]
    return [s * c for s, c in zip(signal, carrier)]

# Thresholding using lambda-based dynamic threshold
def detect_peaks(signal, threshold_ratio=0.7):
    max_val = max(abs(x) for x in signal)
    threshold = threshold_ratio * max_val
    above_threshold = list(filter(lambda x: abs(x) > threshold, signal))
    return len(above_threshold)

# Core calculation function combining modular arithmetic and signal logic
def calculate_signal(modulated_signal, threshold_func):
    peak_count = threshold_func(modulated_signal)
    # Use modular arithmetic to simulate cyclic phase behavior
    base_phase = 360 / (peak_count % 7 or 1)  # Avoid division by zero
    adjusted_phase = (base_phase * 2) % 180
    return round(adjusted_phase + math.sqrt(peak_count), 2)

# Parameters for simulation
SAMPLE_RATE = 100
DURATION = 1
FREQUENCY = 5
CARRIER_FREQ = 20

# Generate base signal
raw_signal = generate_wave(FREQUENCY, DURATION, SAMPLE_RATE)

# Modulate signal
modulated = modulate_am(raw_signal, CARRIER_FREQ, SAMPLE_RATE)

# Define threshold function using lambda
threshold_func = lambda sig: detect_peaks(sig, 0.6)

# Compute final phase result
final_phase = calculate_signal(modulated, threshold_func)

print(f"Result: {final_phase}")