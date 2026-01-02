import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [127, 255, 192, 64, 223, 95, 111, 240]
    scale_factor = 0.75
    adjusted = [r * scale_factor for r in raw_readings]
    return adjusted

def generate_frequency_bins():
    # Irrelevant function: generates unused frequency spectrum
    bins = {}
    for i in range(8):
        bins[f'band_{i}'] = int(440 * (2 ** (i / 12)))
    return bins

def calculate_checksum(data):
    # Unused checksum calculation (red herring)
    chk = 0
    for d in data:
        chk ^= int(d) & 0xFF
    return chk

def extract_peaks(signal):
    # Extract values above empirical peak threshold (150)
    peaks = []
    for val in signal:
        if val > 150:
            peaks.append(val)
    return peaks

def build_threshold_map(config_level=3):
    # Create hierarchical threshold map with decoy entries
    base = {'low': 50, 'medium': 100, 'high': 150}
    extended = {
        'debug_mode': False,
        'version': '2.1a',
        'sensitivity': {'level1': 20, 'level2': 75, 'level3': 120},
        'legacy_flag': True
    }
    extended.update(base)
    return extended

def filter_anomalies(dataset, method='quartile'):
    # Advanced filtering using IQR logic (some relevant, some not)
    sorted_vals = sorted(dataset)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    filtered = [v for v in dataset if lower_bound <= v <= upper_bound]
    
    # Decoy operations
    outlier_count = len(dataset) - len(filtered)
    confidence_score = math.exp(-0.1 * outlier_count) if outlier_count else 1.0
    
    # Unused metrics
    mean_val = sum(dataset) / len(dataset)
    stdev = (sum((x - mean_val)**2 for x in dataset) / len(dataset))**0.5
    
    return filtered

def merge_diagnostic_flags(*flags):
    # Dead code path — never invoked
    combined = set()
    for f in flags:
        combined |= set(f)
    return list(combined)

def analyze_signal(data, thresholds):
    # Core analysis logic
    high_intensity = [d for d in data if d > thresholds['high']]
    medium_intensity = [d for d in data if thresholds['medium'] < d <= thresholds['high']]
    
    # Bit manipulation on count hashes (relevant)
    h_count = len(high_intensity)
    m_count = len(medium_intensity)
    
    # Key transformation: hash fusion via bit ops
    fused_hash = (h_count << 3) ^ (m_count << 1) ^ 0xAA
    
    # Set-based uniqueness check on rounded magnitudes
    unique_levels = set([round(d) for d in data])
    reference_set = set(range(75, 200, 5))
    deviation_set = unique_levels - reference_set
    
    # Final diagnostic derived from multiple sources
    base_score = len(deviation_set) * 17
    adjustment = fused_hash & 0xFF  # Use lower byte
    final_diagnostic = base_score - adjustment
    
    # Red herring: unused conditional branch
    if len(deviation_set) > 10:
        final_diagnostic += 1000  # Never reached in this case
    
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    readings = collect_sensor_readings()
    
    # Step 2: Generate irrelevant frequency bins
    freq_bins = generate_frequency_bins()  # Unused
    
    # Step 3: Filter anomalies from readings
    cleaned = filter_anomalies(readings)
    
    # Step 4: Extract peaks (computed but not fully used)
    peak_values = extract_peaks(cleaned)
    
    # Step 5: Build threshold configuration
    threshold_map = build_threshold_map(config_level=3)
    
    # Step 6: Calculate unused checksum
    checksum = calculate_checksum([int(x) for x in cleaned])  # Distractor
    
    # Step 7: Perform final diagnostic analysis
    final_diagnostic = analyze_signal(cleaned, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")