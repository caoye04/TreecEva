import itertools

# Simulated sensor data processing pipeline with multiple phases
# Real computational core embedded within extensive pre/post-processing

def generate_harmonic_sequence(base_freq, harmonics):
    return [base_freq * (i + 1) for i in range(harmonics)]

def apply_window(signal, window_type='hann'):
    n = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 * (1 - __import__('math').cos(2 * __import__('math').pi * i / (n - 1)))) for i in range(n)]
    return signal

def compute_magnitude_spectrum(signal):
    # Simplified magnitude calculation (simulates FFT-like behavior)
    return [abs(sum(signal[j] * __import__('math').cos(2 * __import__('math').pi * k * j / len(signal)) for j in range(len(signal)))) for k in range(len(signal)//2)]

def classify_band_energy(magnitudes, threshold=150):
    energy = sum(m for m in magnitudes if m > threshold)
    return 'high' if energy > 400 else 'low'

def shift_register_update(register, new_val, size=8):
    register.append(new_val)
    return register[-size:]

def evaluate_signal_purity(spectrum):
    peaks = [i for i in range(1, len(spectrum)-1) if spectrum[i] > spectrum[i-1] and spectrum[i] > spectrum[i+1]]
    return len(peaks) <= 3

# Irrelevant helper functions (dead code paths)
def legacy_calibration():
    return sum(i * 0.97**i for i in range(100))

def deprecated_filter(x):
    return [val for val in x if val % 2 == 0]

def unused_diagnostic(data):
    return {"length": len(data), "unique": len(set(data)), "entropy": 0.0}

def dummy_normalization(arr):
    max_val = max(arr)
    return [x / max_val for x in arr] if max_val > 0 else arr

def obsolete_checksum(sequence):
    return sum(sequence[i] * (i+1) for i in range(len(sequence))) % 256

# Distractor global variables
CALIBRATION_OFFSET = 0.872
TEMPORAL_DAMPING_FACTOR = 0.91
MAX_ITERATIONS = 500
WINDOW_SIZE = 128
BUFFER_OVERFLOW_LIMIT = 1024
REFERENCE_PHASE = [0.1, 0.3, 0.5, 0.7, 0.9]
BASELINE_DRIFT = [0.01 * i for i in range(20)]

# Signal processing configuration (some fields irrelevant)
processing_config = {
    "sample_rate": 1024,
    "frame_size": 256,
    "overlap_ratio": 0.5,
    "harmonic_count": 8,
    "noise_floor_db": -80,
    "temporal_smoothing": True,
    "spatial_filtering": False,  # Unused
    "channel_count": 1
}

band_config = {
    "type": "gamma",
    "lower_bound": 30,
    "upper_bound": 100,
    "notch_filter": None,
    "gain": 2.0,
    "enable_envelope": False
}

# Initialize buffers with decoy data
auxiliary_buffer = [0] * 64
shift_register = [0] * 8
historical_metrics = []
diagnostic_log = []

# Primary signal buffer constructed from harmonic synthesis
base_frequency = 42
harmonic_sequence = generate_harmonic_sequence(base_frequency, processing_config["harmonic_count"])
signal_buffer = [sum(__import__('math').sin(2 * __import__('math').pi * f * t / 100) for f in harmonic_sequence) for t in range(200)]
signal_buffer = [int(x * 100) / 100 for x in signal_buffer]  # Quantize

# Apply real windowing function (relevant)
signal_buffer = apply_window(signal_buffer, 'hann')

# Inject irrelevant transformations
for _ in range(3):
    auxiliary_buffer = shift_register_update(auxiliary_buffer, sum(signal_buffer[:16]) % 100)

temp_snapshot = signal_buffer[::4][:16]
dummy_normalized = dummy_normalization(temp_snapshot)
legacy_offset = legacy_calibration()

# Main processing function with conditional logic
valid_bandwidth = False
total_power = 0
peak_frequency = 0
phase_shift_accumulator = 0.0

if len(signal_buffer) >= processing_config["frame_size"] // 2:
    # Compute spectral characteristics
    magnitude_spectrum = compute_magnitude_spectrum(signal_buffer)
    
    # Determine frequency band limits based on config
    nyquist = processing_config["sample_rate"] // 2
    lower_idx = int(band_config["lower_bound"] * len(magnitude_spectrum) / nyquist)
    upper_idx = min(int(band_config["upper_bound"] * len(magnitude_spectrum) / nyquist), len(magnitude_spectrum) - 1)
    
    if lower_idx < upper_idx:
        valid_bandwidth = True
        band_magnitudes = magnitude_spectrum[lower_idx:upper_idx]
        total_power = sum(band_magnitudes)
        peak_idx = lower_idx + band_magnitudes.index(max(band_magnitudes))
        peak_frequency = peak_idx * nyquist / len(magnitude_spectrum)
        
        # Process phase characteristics using set operations on indices
        strong_bins = {i for i, m in enumerate(magnitude_spectrum) if m > 100}
        gamma_bins = {i for i in range(lower_idx, upper_idx)}
        overlap_bins = strong_bins & gamma_bins
        
        if len(overlap_bins) >= 3:
            phase_components = []
            for idx in sorted(overlap_bins):
                phase_val = __import__('math').atan2(
                    __import__('math').sin(2 * __import__('math').pi * idx / len(magnitude_spectrum)),
                    __import__('math').cos(2 * __import__('math').pi * idx / len(magnitude_spectrum))
                )
                phase_components.append(phase_val)
            
            # Apply circular statistics
            phase_shift_accumulator = sum(__import__('math').cos(pc) for pc in phase_components)

# Decoy multi-stage filter chain
envelope = []
carry_forward = 0
for i, x in enumerate(signal_buffer):
    carry_forward = 0.7 * carry_forward + 0.3 * abs(x)
    if i % 8 == 0:
        envelope.append(carry_forward)

# Linear search for dominant periodicity (irrelevant to final answer)
dominant_period = 0
max_corr = 0
for period in range(10, 100):
    corr = sum(signal_buffer[i] * signal_buffer[i + period] for i in range(len(signal_buffer) - period))
    if corr > max_corr:
        max_corr = corr
        dominant_period = period

# String-based metadata tagging (uses string methods)
signal_tags = []
freq_label = f"{int(peak_frequency)}Hz"
if "gamma" in band_config["type"]:
    signal_tags.append("high_freq")
if classify_band_energy(magnitude_spectrum) == 'high':
    signal_tags.append("high_energy")
signal_tags_str = ",".join(signal_tags).upper().replace("_", "-")
summary_line = f"Signal analysis: {freq_label} | Tags: {signal_tags_str}".strip()
word_count = len(summary_line.split())

# Core computation path reactivation
buffer_clone = signal_buffer.copy()
processed_segments = []

for segment in itertools.batched(buffer_clone, 32):  # Uses itertools
    if len(segment) == 32:
        seg_spectrum = compute_magnitude_spectrum(segment)
        seg_lower = int(30 * len(seg_spectrum) / 512)
        seg_upper = int(100 * len(seg_spectrum) / 512)
        if seg_lower < seg_upper:
            filtered_mags = [m for m in seg_spectrum[seg_lower:seg_upper] if m > 50]
            if filtered_mags:
                processed_segments.append(sum(filtered_mags))

aggregated_energy = sum(processed_segments)

# Final processing function that determines the answer
def process_frequency_band(signal_data, config):
    mag_spectrum = compute_magnitude_spectrum(signal_data)
    nyq = 512  # Assumed half-sample rate
    low_bin = int(config["lower_bound"] * len(mag_spectrum) / nyq)
    high_bin = int(config["upper_bound"] * len(mag_spectrum) / nyq)
    high_bin = min(high_bin, len(mag_spectrum) - 1)
    
    if low_bin >= high_bin:
        return 0
        
    target_magnitudes = mag_spectrum[low_bin:high_bin]
    filtered_peaks = [m for m in target_magnitudes if m > 75]
    
    if not filtered_peaks:
        return 10
        
    # Key computational step
    base_result = sum(filtered_peaks)
    purity_flag = evaluate_signal_purity(mag_spectrum)
    
    adjustment_factor = 1.0
    if purity_flag:
        adjustment_factor *= 0.85
    
    # Use of set difference as distractor
    all_indices = set(range(len(mag_spectrum)))
    peak_indices = {i for i, m in enumerate(mag_spectrum) if m > 200}
    residual_indices = all_indices - peak_indices
    
    # Final adjustment based on phase accumulator from earlier
    global phase_shift_accumulator
    adjusted_result = base_result * adjustment_factor + phase_shift_accumulator * 10
    
    # String method distraction
    flag_str = "purity_ok" if purity_flag else "noisy"
    log_entry = f"BAND_PROC: {flag_str.zfill(8)}".replace("_", "_").split(':')[1].strip()
    
    return int(round(adjusted_result))

# Execute key statement
filtered_phase_result = process_frequency_band(signal_buffer, band_config)

# Print result in required format
print(f"Target result: {filtered_phase_result}")