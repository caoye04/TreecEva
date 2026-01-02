import math

# Simulated sensor array data processing with diagnostic logic
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 0 <= x <= 1000]
    normalized = [round((val - min(filtered)) / (max(filtered) - min(filtered)) * 100) for val in filtered]
    return normalized

# Irrelevant transformation: frequency domain mock-up
def compute_harmonic_profile(signal):
    magnitude = 0
    for i in range(len(signal)):
        magnitude += signal[i] * math.sin(i * math.pi / 4)
    spectral_peak = abs(magnitude) % 77
    return spectral_peak  # Dead end, never used later

# Core pattern extraction using slicing and set operations
def extract_core_signature(data):
    segment_a = data[::2]  # Every other element
    segment_b = data[1::2]
    set_a = set(segment_a)
    set_b = set(segment_b)
    common_elements = set_a & set_b
    unique_to_a = set_a - set_b
    signature_score = len(common_elements) * 13 - len(unique_to_a) * 7
    return signature_score, common_elements

# Secondary red herring: power sequence analysis
def detect_power_sequence(values):
    powers_of_two = {2**i for i in range(10)}
    matched = [v for v in values if v in powers_of_two]
    if len(matched) > 3:
        return sum(matched) // len(matched)
    return -1  # Unused in final path

# Main pattern analyzer with conditional branching and modular arithmetic
def analyze_pattern(seq, threshold):
    if len(seq) < 5:
        return -999

    score_basis = 0
    if seq[0] > seq[-1]:
        score_basis += 23
    else:
        score_basis += 11

    # Slicing-based window analysis
    windows = [seq[i:i+4] for i in range(0, len(seq), 4)]
    valid_windows = [w for w in windows if len(w) == 4]

    for window in valid_windows:
        sorted_win = sorted(window)
        median_diff = sorted_win[2] - sorted_win[1]
        if median_diff % 2 == 0:
            score_basis += 17
        else:
            score_basis += 5

    # Set operation to identify repeated trends
    first_half = set(seq[:len(seq)//2])
    second_half = set(seq[len(seq)//2:])
    overlaps = first_half & second_half
    overlap_bonus = len(overlaps) * 12 if len(overlaps) >= 3 else -8

    # Conditional combinatorics: count ascending triples
    asc_triples = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] < seq[i+2]:
            asc_triples += 1

    combinatoric_factor = asc_triples % 5

    # Final computation with modular arithmetic and conditional adjustments
    raw_diagnostic = (score_basis + overlap_bonus) * 3 + (combinatoric_factor ** 2) * 4

    if raw_diagnostic > threshold:
        final_value = (raw_diagnostic % 997) + 100
    else:
        final_value = (raw_diagnostic % 883) - 50

    return final_value

# --- Simulated Execution ---
if __name__ == "__main__":
    # Initial sensor readings (simulated)
    primary_readings = [105, 800, 200, 450, 700, 300, 600, 250, 900, 350]
    
    # Step 1: Preprocess actual data
    processed_signal = preprocess_readings(primary_readings)
    
    # Distraction: Compute unused harmonic profile
    _ = compute_harmonic_profile(processed_signal)
    
    # Extract signature (partially relevant but not directly used)
    sig_score, common_vals = extract_core_signature(processed_signal)
    
    # Red herring: check for power sequences
    _ = detect_power_sequence(processed_signal)
    
    # Transform data via slicing manipulation
    reversed_chunks = processed_signal[::-1]
    chunk_size = 5
    split_data = [reversed_chunks[i:i+chunk_size] for i in range(0, len(reversed_chunks), chunk_size)]
    flattened = []
    for chunk in split_data:
        if len(chunk) == chunk_size:
            flattened.extend(chunk)
        else:
            flattened.extend([0]*(chunk_size - len(chunk)) + chunk)
    
    transformed_data = flattened[:len(processed_signal)]  # Same length as original
    
    # Threshold calculation with decoy intermediate steps
    base_ref = sum(transformed_data) // len(transformed_data)
    deviation = abs(transformed_data[0] - transformed_data[-1])
    noise_floor = (deviation * 2) % 40
    base_threshold = base_ref + noise_floor - 15  # Used in final call
    
    # Irrelevant list of thresholds
    alternative_thresholds = [base_ref + i*10 for i in range(-3, 4) if i != 0]
    for alt in alternative_thresholds:
        if alt % 13 == 0:
            break

    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, base_threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")