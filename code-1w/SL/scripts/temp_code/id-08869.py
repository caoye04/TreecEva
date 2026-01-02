from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and calibration factors
def fetch_sensor_data():
    raw_data = [127, 255, 0, 191, 63, 178, 42, 210, 88, 150]
    calibration_offset = 1.05
    return [x * calibration_offset for x in raw_data]

def filter_noise(readings):
    # Apply moving average filter (window size 3)
    smoothed = []
    for i in range(len(readings)):
        if i == 0:
            smoothed.append(round(readings[i], 2))
        elif i == len(readings) - 1:
            prev_avg = (readings[i-1] + readings[i]) / 2
            smoothed.append(round(prev_avg, 2))
        else:
            window_avg = (readings[i-1] + readings[i] + readings[i+1]) / 3
            smoothed.append(round(window_avg, 2))
    return smoothed

def categorize_signal_strength(val):
    if val > 200:
        return 'strong'
    elif val > 100:
        return 'moderate'
    elif val > 30:
        return 'weak'
    else:
        return 'critical'

def compute_checksum(data_list):
    # Irrelevant checksum computation (red herring)
    chk = 0
    for item in data_list:
        chk = (chk + int(item)) * 7 % 97
    return chk

def generate_frequency_map(signal_list):
    # Count frequency of categorized signal strengths
    categories = [categorize_signal_strength(x) for x in signal_list]
    freq_map = defaultdict(int)
    for cat in categories:
        freq_map[cat] += 1
    return freq_map

def extract_peaks_and_troughs(data):
    # Find local maxima and minima (mostly irrelevant to final result)
    peaks = []
    troughs = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            troughs.append(data[i])
    return peaks[:3], troughs[:3]  # Return at most 3 each

def calculate_entropy(values):
    # Calculate Shannon entropy of distribution (distractor)
    count = Counter(values)
    total = len(values)
    entropy = 0.0
    for freq in count.values():
        p = freq / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def phase_shift_correction(signal_list):
    # Simulate phase correction (no real effect on outcome)
    corrected = []
    for x in signal_list:
        corr_val = x * math.cos(math.pi / 8) + 5
        corrected.append(round(corr_val, 2))
    return corrected

def normalize_data(seq):
    # Normalize values between 0 and 1 (unused path)
    min_val, max_val = min(seq), max(seq)
    if max_val == min_val:
        return [0.5] * len(seq)
    return [(x - min_val) / (max_val - min_val) for x in seq]

def analyze_readings(clean_signals):
    # Core logic hidden among distractions
    category_freq = defaultdict(int)
    for val in clean_signals:
        if val > 200:
            category_freq['high'] += 1
        elif val > 100:
            category_freq['med'] += 1
        else:
            category_freq['low'] += 1
    
    # Key calculation: weighted diagnostic score
    base_score = 0
    base_score += category_freq['high'] * 17
    base_score += category_freq['med'] * 11
    base_score -= category_freq['low'] * 5
    
    # Secondary adjustment based on exact pattern
    sorted_vals = sorted([int(x) for x in clean_signals])
    median_int = sorted_vals[len(sorted_vals)//2]
    adjustment = (median_int % 13) - 6  # Range: -6 to 6
    
    final_score = base_score + adjustment
    return final_score

def main():
    # Step 1: Fetch raw sensor data
    raw_signals = fetch_sensor_data()
    
    # Step 2: Filter out noise
    filtered_signals = filter_noise(raw_signals)
    
    # Step 3: Generate various irrelevant diagnostics
    checksum = compute_checksum(filtered_signals)  # Red herring
    peaks, troughs = extract_peaks_and_troughs(filtered_signals)  # Misleading
    entropy = calculate_entropy(filtered_signals)  # Distractor metric
    shifted_signals = phase_shift_correction(filtered_signals)  # Dead path
    normalized = normalize_data(filtered_signals)  # Unused normalization
    freq_distribution = generate_frequency_map(filtered_signals)  # Partially relevant but not used
    
    # Step 4: Process signals for actual analysis
    processed_signals = []
    for s in filtered_signals:
        if s < 10:
            processed_signals.append(30)  # Safety floor
        else:
            processed_signals.append(s)
    
    # Step 5: Analyze readings (contains key statement)
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

if __name__ == "__main__":
    main()