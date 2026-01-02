import math

# Simulated sensor data processing for quantum resonance analysis

def generate_waveform(base_freq, harmonics, duration=1.0, sample_rate=100):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    signal = []
    for t in timesteps:
        val = 0
        for h, amp in enumerate(harmonics, 1):
            val += amp * math.sin(2 * math.pi * base_freq * h * t)
        signal.append(val)
    return signal

# Irrelevant helper: computes statistical moments (not used in final result)
def compute_moments(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    skewness = sum((x - mean) ** 3 for x in data) / (n * variance ** 1.5) if variance > 0 else 0
    kurtosis = sum((x - mean) ** 4 for x in data) / (n * variance ** 2) - 3 if variance > 0 else 0
    return (mean, variance, skewness, kurtosis)

# Distractor function: performs bit manipulation on indices (dead end)
def scramble_indices(indices):
    scrambled = []
    for idx in indices:
        b = bin(idx ^ 0b1011)[2:]
        flipped = ''.join('1' if c == '0' else '0' for c in b)
        scrambled.append(int(flipped, 2) % 100)
    return scrambled

# Core analysis: extract dominant harmonic via power spectrum
harmonic_weights = [0.5, 1.2, 0.8, 2.1, 0.7, 1.3, 0.9]  # Relative amplitudes
base_fundamental = 440.0  # Standard A4 tuning

# Generate complex waveform with harmonics
raw_wave = generate_waveform(base_fundamental, harmonic_weights, duration=0.5, sample_rate=200)

# Extract magnitude spectrum using simplified DFT (only test relevant frequencies)
def compute_spectrum(signal, base_freq, num_harmonics=8):
    N = len(signal)
    spectrum = []
    for k in range(1, num_harmonics + 1):
        freq = base_freq * k
        real = 0.0
        imag = 0.0
        for n, s in enumerate(signal):
            angle = 2 * math.pi * freq * (n / 200)  # 200 = sample rate
            real += s * math.cos(angle)
            imag -= s * math.sin(angle)
        magnitude = math.sqrt(real**2 + imag**2) / N
        spectrum.append((k, magnitude))
    return spectrum

# Apply windowing (irrelevant to final logic but looks important)
def apply_hanning_window(signal):
    N = len(signal)
    return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (N - 1))) for i in range(N)]

windowed_data = apply_hanning_window(raw_wave)  # Unused downstream

# Real computation begins here
spectrum_peaks = compute_spectrum(raw_wave, base_fundamental)

# Find strongest harmonic by power (magnitude squared)
dominant_power = -1.0
primary_harmonic_index = 1
for harmonic_num, mag in spectrum_peaks:
    power = mag ** 2
    if power > dominant_power:
        dominant_power = power
        primary_harmonic_index = harmonic_num

# Secondary analysis: check phase coherence (distractor)
coherence_score = 0.0
for i in range(1, len(raw_wave) - 1):
    if raw_wave[i] > 0 and raw_wave[i-1] < 0:
        coherence_score += 0.1
    elif raw_wave[i] < 0 and raw_wave[i-1] > 0:
        coherence_score -= 0.05

# Critical lambda: models nonlinear response of detection apparatus
response_curve = lambda x: math.log(1 + x ** 1.8) if x > 0 else 0

# Compute weighted centroid frequency (more accurate than peak alone)
total_weighted_freq = 0.0
total_weight = 0.0
for harmonic_num, mag in spectrum_peaks:
    adjusted_mag = response_curve(mag)
    freq = base_fundamental * harmonic_num
    total_weighted_freq += freq * adjusted_mag
    total_weight += adjusted_mag

centroid_frequency = total_weighted_freq / total_weight if total_weight > 0 else base_fundamental

# Final analysis function
waveform_snapshot = raw_wave[::2]  # Every other sample — realistic subsampling

def analyze_harmonics(samples):
    # Slice analysis: focus on transient onset
    onset_slice = samples[:len(samples)//4]
    decay_slice = samples[-len(samples)//3:]
    
    # Count zero crossings in onset (distractor metric)
    zero_crossings = 0
    for i in range(1, len(onset_slice)):
        if onset_slice[i-1] * onset_slice[i] < 0:
            zero_crossings += 1
    
    # Recompute spectral peak on sliced data (redundant but plausible)
    temp_spectrum = compute_spectrum(samples, base_fundamental)
    max_mag = 0
    best_harmonic = 1
    for h, mag in temp_spectrum:
        if mag > max_mag:
            max_mag = mag
            best_harmonic = h
    
    # Use centroid from earlier full analysis, not recomputed one
    # This creates a subtle trap: code appears to recompute but uses outer scope
    refined_estimate = centroid_frequency * (1 + 0.02 * (best_harmonic - primary_harmonic_index))
    
    # Apply calibration offset based on device serial (simulated constant)
    device_id = "QRA-7842-X"
    calibration_offset = sum(ord(c) for c in device_id) % 17 - 8  # [-8, 8]
    
    # Final adjustment: only if device is even-numbered series
    if int(device_id[-1]) % 2 == 0:
        refined_estimate += calibration_offset * 0.5
    
    return refined_estimate

# Key execution point
resonance_frequency = analyze_harmonics(waveform_snapshot)

# Print result as required
print(f"Target result: {resonance_frequency}")