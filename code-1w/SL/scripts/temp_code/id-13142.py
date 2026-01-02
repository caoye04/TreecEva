import math

# Simulated sensor data processing with red herrings and complex flow
def fetch_raw_readings():
    return [2.1, 4.5, -1.2, 7.8, 3.3, 9.0, -0.5, 6.4, 5.1]

def compute_checksum(data):
    # Irrelevant checksum computation (dead-end)
    return sum(int(x) for x in data if x > 0) % 17

def filter_outliers(stream, limit=8.0):
    # Real filtering used later
    return [x for x in stream if abs(x) <= limit]

def apply_calibration(readings, factor=1.05):
    # Meaningful transformation
    return [round(x * factor, 3) for x in readings]

def generate_moment_indices(signal):
    # Distractor: computes indices but not used in final path
    indices = []
    for i in range(1, len(signal)):
        if signal[i] > signal[i-1] and signal[i] > 0:
            indices.append(i * 2)
    return sorted(indices, reverse=True)

def rolling_window_avg(seq, size=3):
    # Red herring function – looks important but unused
    averages = []
    for i in range(len(seq) - size + 1):
        averages.append(sum(seq[i:i+size]) / size)
    return averages

def evaluate_stability(rhythm):
    # Unused recursive stability check (distractor)
    if len(rhythm) <= 1:
        return True
    mid = len(rhythm) // 2
    return (evaluate_stability(rhythm[:mid]) and 
            abs(rhythm[mid] - rhythm[mid-1]) < 3.0)

def extract_peaks(trace):
    # Another distractor list comprehension
    return [i for i in trace if i == max(trace)]

def shift_phase(signal, steps=1):
    # Bit manipulation red herring
    n = len(signal)
    if n == 0:
        return signal
    steps = steps % n
    # Logical XOR-based index scrambling (unused)
    scrambled = [(i ^ steps) % n for i in range(n)]
    restored = [0] * n
    for i in range(n):
        restored[scrambled[i]] = signal[i]
    return restored  # Never actually used in correct path

def normalize_signal(wave):
    max_val = max(abs(x) for x in wave)
    if max_val == 0:
        return wave
    return [round(x / max_val, 4) for x in wave]

def integrate_series(values):
    # Relevant cumulative integration
    integral = 0.0
    integrated = []
    for v in values:
        integral += v
        integrated.append(round(integral, 4))
    return integrated

def derive_pattern(sequence):
    # Compute differences between consecutive elements
    if len(sequence) < 2:
        return [0]
    diffs = [round(sequence[i+1] - sequence[i], 3) for i in range(len(sequence)-1)]
    return diffs

def aggregate_metrics(changes):
    # Compute statistical decoy metrics
    avg = sum(changes) / len(changes)
    peak = max(changes)
    trough = min(changes)
    volatility = round((peak - trough) * avg, 4)
    return {"average": avg, "volatility": volatility}  # Partially misleading

def analyze_pattern(dynamic_trace, cutoff):
    # Core analysis logic
    segment = dynamic_trace[:len(dynamic_trace)//2 + 1]  # Use first half + middle
    smoothed = [x for x in segment if x >= cutoff]  # Filtering based on threshold
    if not smoothed:
        smoothed = [0.0]
    # Final diagnostic computed via layered transforms
    base_sum = sum(smoothed)
    adjustment = len(smoothed) ** 0.5
    raw_diagnostic = base_sum * adjustment
    final_score = int(round(raw_diagnostic * 100))
    return final_score

# Begin main execution pipeline
raw_data = fetch_raw_readings()
cleaned_data = filter_outliers(raw_data)
calibrated_data = apply_calibration(cleaned_data)

# Apply normalization
normalized_data = normalize_signal(calibrated_data)

# Integrate over time
integrated_data = integrate_series(normalized_data)

diff_sequence = derive_pattern(integrated_data)

# Irrelevant branching based on decoy logic
if len(diff_sequence) > 5:
    temp_analysis = extract_peaks(diff_sequence)
    phase_shifted = shift_phase(diff_sequence, steps=2)

# Generate unused checksum
checksum = compute_checksum(integrated_data)

# Another irrelevant operation
moment_keys = generate_moment_indices(integrated_data)

# Real transformation that feeds into final step
transformed_data = integrate_series(derive_pattern(normalized_data))

threshold = 0.5

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")