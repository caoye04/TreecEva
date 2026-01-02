import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_samples(base_freq, duration, sample_rate):
    time_steps = [i / sample_rate for i in range(int(duration * sample_rate))]
    raw_samples = [math.sin(2 * math.pi * base_freq * t) + \
                   0.5 * math.cos(2 * math.pi * 3 * base_freq * t) \
                   for t in time_steps]
    return raw_samples


def apply_filter(samples, filter_mode='low_pass'):
    # Irrelevant complex filter setup (distractor)
    alpha = 0.1 if filter_mode == 'low_pass' else 0.9
    filtered = [samples[0]]
    for x in samples[1:]:
        filtered.append(alpha * x + (1 - alpha) * filtered[-1])
    return filtered


def compute_entropy(data):
    # Dummy entropy calculation (misleading path)
    mean_val = sum(data) / len(data)
    deviations = [abs(x - mean_val) for x in data]
    if not any(deviations):  # Avoid log(0)
        return 0.0
    normalized = [d / max(deviations) for d in deviations if d > 0]
    return -sum(p * math.log(p) for p in normalized if p > 0)


def extract_peaks(signal, threshold=0.7):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append((i, signal[i]))
    return peaks[:10]  # Limit to first 10 peaks


def shift_phase(signal, phase_angle):
    # Unused function - red herring
    rotated = [x * math.cos(phase_angle) - math.sin(phase_angle) for x in signal]
    return rotated


def generate_noise(length, seed=42):
    # Dead code path - never actually used in main flow
    import random
    random.seed(seed)
    return [random.gauss(0, 0.1) for _ in range(length)]


def integrate_signal(signal):
    # Trapezoidal integration
    integral = 0.0
    for i in range(1, len(signal)):
        integral += (signal[i] + signal[i-1]) * 0.5
    return integral


def analyze_signal(processed):
    # Key logic hidden among distractions
    peak_list = extract_peaks(processed, threshold=0.65)
    total_energy = sum(x**2 for idx, x in peak_list)
    peak_count = len(peak_list)
    
    # Decoy computation
    dummy_metric = compute_entropy(processed)
    temp_result = math.sqrt(total_energy) if peak_count > 0 else 0
    
    # Critical intermediate step
    adjusted_count = peak_count + (1 if temp_result > 2.0 else 0)
    
    # Secondary validation
    integral_value = integrate_signal(processed)
    validation_score = 1 if abs(integral_value) < 10 else -1
    
    # Final diagnostic depends on multiple derived values
    final_diagnostic = (adjusted_count * 1000) + (validation_score * 50) + int(temp_result)
    
    # Misleading alternate path
    if final_diagnostic > 5000:
        final_diagnostic -= 250  # Never reached due to input constraints
    
    return final_diagnostic

# === MAIN EXECUTION WITH DISTRACTORS ===

def main():
    # Real parameters
    frequency = 2.5
    duration = 4.0
    rate = 50
    
    # Irrelevant auxiliary variables
    calibration_offset = 0.003
    max_theoretical_peaks = int(duration * frequency * 2)  # unused
    system_diagnostics = {'status': 'nominal', 'voltage': 3.3}
    
    # Core signal acquisition
    raw_data = collect_samples(frequency, duration, rate)
    processed_samples = apply_filter(raw_data, 'low_pass')
    
    # Dummy parallel processing chain (dead end)
    alt_processed = [x * 1.05 for x in raw_data]
    alt_peaks = extract_peaks(alt_processed, threshold=0.8)
    alternative_diagnostic = len(alt_peaks) * 77  # decoy result
    
    # Actual target computation
    final_diagnostic = analyze_signal(processed_samples)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()