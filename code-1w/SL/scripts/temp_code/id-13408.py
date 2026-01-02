import itertools

# Simulated sensor fusion and anomaly detection system
def collect_sensor_data():
    raw_readings = [18, 22, 19, 25, 17, 23, 20, 24]
    calibration_offset = 3
    adjusted = [r + calibration_offset for r in raw_readings]
    return adjusted

# Irrelevant helper - distractor
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        neighbors = []
        for j in range(max(0, i-1), min(len(data), i+2)):
            neighbors.append(data[j])
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Unused transformation - dead code path
def frequency_shift(signal, shift=2):
    shifted = [(x << shift) % 100 for x in signal]
    return shifted

# Real processing function
def extract_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks

# Misleading diagnostic with plausible but unused logic
def legacy_diagnostic(signal):
    threshold = 22
    count = 0
    for val in signal:
        if val > threshold:
            count += 1
    score = count * 1.5  # Decoy computation
    return score  # Never used

# Core analysis logic
def generate_combinations(values):
    combs = []
    for r in range(2, 4):
        combs.extend(list(itertools.combinations(values, r)))
    return combs

def compute_entropy(combinations):
    entropy_vals = []n    for comb in combinations:
        product = 1
        for x in comb:
            product *= x
        length = len(comb)
        entropy = (product % 100) / (length + 1)
        entropy_vals.append(entropy)
    return entropy_vals

def filter_candidates(candidates, key):
    valid = []
    for val in candidates:
        if val % 2 == (key % 2):  # parity-based filtering
            valid.append(val)
    return valid

# Main diagnostic engine
def analyze_pattern(signals, system_key):
    # Step 1: Extract high points
    peak_values = extract_peaks(signals)
    
    # Distractor: smooth but don't use
    smoothed_peaks = smooth_signal(peak_values)
    
    # Step 2: Generate interaction patterns
    interaction_combs = generate_combinations(peak_values)
    
    # Step 3: Compute entropy signature
    entropies = compute_entropy(interaction_combs)
    
    # Step 4: Aggregate baseline metric
    base_metric = sum(entropies) / len(entropies)
    
    # Step 5: Apply system key modulation
    modulated = [e * (system_key % 7) for e in entropies]
    
    # Step 6: Derive candidate diagnostics
    raw_diagnostics = [int(abs(m) * 10) % 89 for m in modulated]
    
    # Step 7: Filter using key parity
    filtered_diagnostics = filter_candidates(raw_diagnostics, system_key)
    
    # Step 8: Compute final diagnostic checksum
    checksum = 0
    for i, val in enumerate(filtered_diagnostics):
        checksum += (val * (i + 1)) % 23
    
    # Final computation
    final_diagnostic = (checksum + base_metric) // 1
    
    return int(final_diagnostic)

# Irrelevant global constants - red herrings
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 15.5
DEBUG_MODE = False
SYSTEM_VERSION = "v3.7"

# Execution flow
if __name__ == "__main__":
    # Collect real data
    collected_signals = collect_sensor_data()
    
    # Fake preprocessing - distractor
    normalized_signals = [round(x / 25.0, 2) for x in collected_signals]
    categorized = {"high": [], "medium": [], "low": []}
    for x in collected_signals:
        if x > 25: categorized["high"].append(x)
        elif x > 20: categorized["medium"].append(x)
        else: categorized["low"].append(x)
    
    # System identification
    timestamp = 123456789
    system_id = (timestamp * 3) % 19
    system_key = system_id ^ 17
    
    # Critical execution point
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Output result
    print(f"Result: {final_diagnostic}")