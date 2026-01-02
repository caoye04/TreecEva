import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.9, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 35, 30, 40, 45, 38, 33]  # unused in final calculation
light_intensity = [800, 820, 780, 850, 900, 870, 830]  # never accessed

# Preprocessing: Normalize and filter relevant signals
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) for x in signal]

def detect_outliers(values, threshold=1.5):
    normalized = normalize_signal(values)
    return [i for i, v in enumerate(normalized) if abs(v) > threshold]

def pack_data(temps, hums, press):
    # Misleading transformation - not used in final path
    packed = []
    for t, h, p in zip(temps, hums, press):
        packed.append((t * 100) + (h * 10) + (p % 100))
    return packed

def encrypt_sequence(seq):
    # Decoy function: looks important but unused
    encrypted = 0
    for val in seq:
        encrypted ^= int(val * 7) & 0xFFFF
    return encrypted

def phase_shift_correction(data, shift=1):
    # Unused signal processing red herring
    return data[shift:] + data[:shift]

def calculate_entropy(data):
    # Looks scientific but irrelevant to final result
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0.0
    probs = [abs(x)/total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Signal fusion and weighting (core logic begins)
baseline_temp = sum(temperature_readings) / len(temperature_readings)
baseline_hum = sum(humidity_readings) / len(humidity_readings)
baseline_press = sum(pressure_readings) / len(pressure_readings)

# Apply dynamic correction factors based on time index
adjusted_temps = []
for i, t in enumerate(temperature_readings):
    correction = (i % 3 - 1) * 0.3  # oscillating correction
    adjusted_temps.append(t + correction)

# Generate composite index using bitwise blending (relevant)
composite_indices = []
for i in range(len(adjusted_temps)):
    temp_code = int((adjusted_temps[i] - 20) * 10)  # scale temperature
    hum_code = int(humidity_readings[i] / 5)         # quantize humidity
    press_code = pressure_readings[i] % 32          # extract low bits of pressure
    
    # Bit-blend: use XOR and shifts to combine
    fused = (temp_code << 5) ^ (hum_code << 2) ^ press_code
    composite_indices.append(fused)

# Filter using set operations to remove unstable readings (KEY CONCEPT)
stable_threshold_set = set(range(200, 800))  # valid fused code range
valid_indices = [x for x in composite_indices if x in stable_threshold_set]

# Secondary filtering: exclude values with high bit parity (distraction)
def has_high_bit_parity(n):
    return bin(n).count('1') > 6

# But actually we don't use this filter — red herring
parity_filtered = [x for x in valid_indices if not has_high_bit_parity(x)]

# Real processing continues: map to diagnostic space
mapped_diagnostics = []
for val in valid_indices:
    # Non-linear transformation
    transformed = int((val ** 0.5) * 3.7)
    mapped_diagnostics.append(transformed)

# Remove duplicates while preserving order (set-based deduplication)
seen = set()
deduped_diagnostics = []
for d in mapped_diagnostics:
    if d not in seen:
        seen.add(d)
        deduped_diagnostics.append(d)

# Compute rolling window average of last three (if possible)
window_averages = []
for i in range(len(deduped_diagnostics)):
    if i >= 2:
        window_avg = sum(deduped_diagnostics[i-2:i+1]) / 3
        window_averages.append(int(window_avg))
    else:
        # Padding logic - not used later
        window_averages.append(deduped_diagnostics[i] // 2)

# Core diagnostic algorithm (never called in this path — decoy)
class DiagnosticEngine:
    def __init__(self):
        self.calibration = 0.95
    
    def run_full_analysis(self, data):
        return sum(data) * self.calibration  # misleading

# Actual analysis function that will be called
def analyze_readings(readings):
    base_score = sum(readings) & 0xFFFF  # limit to 16 bits
    
    # Add entropy-like measure using set size
    unique_count = len(set(readings))
    diversity_bonus = unique_count * 17
    
    # Apply secret offset known only to system
    SECRET_OFFSET = 582
    
    # Final computation
    result = (base_score + diversity_bonus) - SECRET_OFFSET
    
    # Dead code branch - compiler can't optimize it away due to side effect check
    if False and sum(readings) > 1e6:
        result = int(math.sqrt(result))
    
    return result

# Processing pipeline
raw_fusion = [a ^ b for a, b in zip(temperature_readings, humidity_readings)]  # unused
checksum = 0
for p in pressure_readings:
    checksum = (checksum + p) * 101 % 97  # irrelevant integrity check

# Main processing step
processed_signals = deduped_diagnostics  # key assignment

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Print final answer as required
print(f"Target result: {final_diagnostic}")