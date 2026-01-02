import math

# Simulated astrophysics data processing with decoy functions and red herrings
def preprocess_readings(raw):    # Irrelevant normalization    return [x * 1.05 for x in raw if x > 0]

def analyze_variance(data):    # Dead-end statistical analysis    mean = sum(data) / len(data)    variance = sum((x - mean) ** 2 for x in data) / len(data)    return variance ** 0.5

def calculate_entropy(sequence):    # Misleading complexity - not used in final result    freq_map = {}
    for item in sequence:        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0    total = len(sequence)
    for count in freq_map.values():        p = count / total
        if p > 0:            entropy -= p * math.log2(p)
    return entropy

def filter_outliers(arr, threshold=2):    # Distractor function - never called    mean = sum(arr) / len(arr)    dev = [(x - mean) ** 2 for x in arr]    std = sum(dev) / len(dev) ** 0.5    return [x for x in arr if abs(x - mean) <= threshold * std]

def compute_harmonic_series(n):    # Unused recursive red herring    if n == 1:
        return 1.0
    return 1/n + compute_harmonic_series(n-1)

def generate_phase_shifts(count):    # Creates irrelevant data    shifts = []
    for i in range(count):
        shifts.append((i * 7.1) % (2 * math.pi))
    return shifts

def extract_peaks(signal):    # Decoy signal processing    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return sorted(peaks, reverse=True)[:3]

def calculate_stellar_flux(readings, config):    # CORE FUNCTION - actual computation path    processed = [x * config['gain'] for x in readings]    # Apply temperature compensation using lambda abstraction    temp_compensate = lambda val: val * (1 + 0.002 * (config['temp'] - 25))
    compensated = list(map(temp_compensate, processed))    # Noise floor subtraction    cleaned = [max(0, x - config['noise_floor']) for x in compensated]    # Weighted integration using enumerate and zip    weights = [0.8, 1.0, 1.2, 0.9, 1.1]
    segments = cleaned[:5]
    integral = 0    for i, (seg, w) in enumerate(zip(segments, weights)):        integral += seg * w * (0.1 + i * 0.05)  # Time-weighted    # Non-linear amplification stage    flux_raw = integral * math.log(2 + integral * 0.01)
    # Final adjustment based on calibration polynomial    poly_factor = sum(config['poly_coeffs'][j] * (flux_raw * 0.001)**j for j in range(4))
    return int(flux_raw * poly_factor)  # Deterministic integer output

# Main execution block
if __name__ == '__main__':
    # Real input data
    sensor_readings = [127, 142, 135, 146, 130, 151, 128]
    
    # Configuration with misleading extra keys
    calibration = {
        'gain': 1.8,
        'temp': 22,
        'noise_floor': 10.5,
        'version': 'X27',
        'last_updated': '2023-11-05',
        'poly_coeffs': [0.95, -0.02, 0.003, -0.0001],  # 4th order correction
        'spurious_key_1': [0]*5,
        'spurious_key_2': {'nested': 'junk'}
    }
    
    # Irrelevant preprocessing chain
    norm_readings = preprocess_readings(sensor_readings)
    sample_variance = analyze_variance(norm_readings)
    phase_data = generate_phase_shifts(7)
    peak_magnitudes = extract_peaks(sensor_readings)
    
    # Core calculation embedded in distractions
    temp_buffer = [math.sin(x) for x in phase_data]
    entropy_score = calculate_entropy([1,2,2,3,3,3,4,4,5])
    harmonic_sum = compute_harmonic_series(5)  # Computed but unused
    
    # Key statement containing the actual answer
    final_flux = calculate_stellar_flux(readings=sensor_readings, calibration_data=calibration)
    
    # Output result as required
    print(f"Result: {final_flux}")