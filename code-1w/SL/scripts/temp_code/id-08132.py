import math

# Simulated sensor data from environmental monitoring array
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [45, 48, 52, 58, 61, 57, 54, 50]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.014
REFERENCE_VOLTAGE = 3.3
NOISE_FLOOR_DB = 42.5

# Preprocess function with red herring logic
def preprocess(signal, gain=1.0, offset=0.0):
    # This function is overcomplicated with unused parameters
    adjusted = [gain * (x + offset) for x in signal]
    normalized = [x / max(adjusted) for x in adjusted]  # Only normalization matters
    filtered = [x for x in normalized if x > 0.5]  # Filtering out low values (misleading)
    return normalized  # Returns full list despite filtering (decoy path)

# Signal processing pipeline
raw_signal = [t * 1.2 + h * 0.3 for t, h in zip(temperature_readings, humidity_readings)]
boosted_signal = preprocess(raw_signal, gain=1.1, offset=0.5)

# Apply windowing (partially relevant but obfuscated)
def apply_hamming_window(data):
    N = len(data)
    return [data[i] * (0.54 - 0.46 * math.cos(2 * math.pi * i / (N - 1))) for i in range(N)]

windowed_signal = apply_hamming_window(boosted_signal)

# Decoy transformation chain (dead code path)
def spectral_analysis(sig):
    fft_magnitude = [abs(complex(x, 0)) for x in sig]  # Trivial identity
    power_spectrum = [mag ** 2 for mag in fft_magnitude]
    return sum(power_spectrum) / len(power_spectrum)

# Unused analysis (irrelevant computation)
spectral_power = spectral_analysis(windowed_signal)
baseline_shift = sum(humidity_readings) / len(humidity_readings) - 50
phantom_correction = baseline_shift * CALIBRATION_FACTOR_A

# Actual processing path begins here (non-obvious due to distractions)
processed_signals = []
for val in windowed_signal:
    if val > 0.7:
        processed_signals.append(int(val * 100) % 13)
    elif val > 0.5:
        processed_signals.append(int(val * 80) % 11)
    else:
        processed_signals.append(0)

# Redundant structure with misleading comments
class DiagnosticEngine:
    @staticmethod
    def compute_entropy(data):
        # Not actually used in final calculation
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        probs = [f / len(data) for f in freq.values()]
        return -sum(p * math.log2(p) for p in probs)
    
    @staticmethod
    def analyze_readings(readings):
        # Key logic hidden among distractions
        total = 0
        for i, r in enumerate(readings):
            if i % 3 == 0:
                total += r * 2
            elif i % 3 == 1:
                total += r
            else:
                total -= r  # Subtraction on every third element
        
        # Secondary transformation (appears complex but deterministic)
        temp_result = (total * 7) ^ 0b1101  # Bitwise XOR with binary constant
        
        # Modular arithmetic with large modulus (looks cryptographic)
        final_value = (temp_result + 10007) % 98765
        
        # Conditional expression (required language feature)
        adjustment = 5 if final_value < 5000 else (-3 if final_value > 90000 else 0)
        
        return final_value + adjustment

# Execute main analysis
diag_engine = DiagnosticEngine()
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")