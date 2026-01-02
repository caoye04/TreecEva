import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_freq, duration):
    samples = []
    for t in range(duration * 10):
        noise = math.sin(t * 0.1) * 0.3
        signal = math.cos(base_freq * t * 0.05) + noise
        samples.append(round(signal, 3))
    return samples

# Irrelevant helper: computes harmonic mean (not used in final path)
def harmonic_mean(vals):
    if not vals or any(v == 0 for v in vals):
        return 0
    return len(vals) / sum(1/v for v in vals)

# Data transformation pipeline
def apply_filter(data, mode='smooth'):
    filtered = []
    for i in range(len(data)):
        if mode == 'smooth' and 5 < i < len(data) - 5:
            window = data[i-5:i+5]
            avg = sum(window) / len(window)
            filtered.append(round(avg, 3))
        else:
            filtered.append(data[i])
    return filtered

# Character frequency analysis - red herring function
def analyze_characters(text_string):
    freq_map = {}
    for ch in text_string:
        if ch.isalpha():
            freq_map[ch] = freq_map.get(ch, 0) + 1
    sorted_chars = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_chars[:3]]

# Core pattern analyzer: counts zero-crossings and peaks
def count_zero_crossings(series):
    crossings = 0
    for i in range(1, len(series)):
        if series[i-1] < 0 <= series[i] or series[i-1] > 0 >= series[i]:
            crossings += 1
    return crossings

# Peak detection using lambda-based thresholding
def detect_peaks(series, threshold_factor=0.7):
    if not series:
        return []
    threshold = threshold_factor * max(abs(x) for x in series)
    is_peak = lambda val, prev, next_val: prev < val > next_val and abs(val) > threshold
    peaks = []
    for i in range(1, len(series) - 1):
        if is_peak(series[i], series[i-1], series[i+1]):
            peaks.append(i)
    return peaks

# Secondary transformation - bit manipulation red herring
def scramble_index(index_list):
    scrambled = []
    for idx in index_list:
        # Bitwise shuffle that isn't actually used
        transformed = ((idx << 2) & 0xFF) ^ 0x5A
        back = (transformed ^ 0x5A) >> 2
        scrambled.append(back)
    return scrambled

# Main analysis function combining multiple concepts
def analyze_pattern(cleaned_signal):
    zero_cross_count = count_zero_crossings(cleaned_signal)
    
    # Compute statistical moments - some irrelevant
    mean_val = sum(cleaned_signal) / len(cleaned_signal)
    variance = sum((x - mean_val)**2 for x in cleaned_signal) / len(cleaned_signal)
    std_dev = math.sqrt(variance)
    
    # Real work: detect significant peaks
    significant_peaks = detect_peaks(cleaned_signal, threshold_factor=0.65)
    peak_magnitude_sum = sum(abs(cleaned_signal[i]) for i in significant_peaks)
    
    # Dummy combinatorics calculation - distraction
    def calculate_combinations(n, r):
        if r > n or r < 0:
            return 0
        r = min(r, n - r)
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    
    # Unused combination logic
    dummy_combo = calculate_combinations(len(significant_peaks) + 3, 3)
    
    # Linear search for first strong positive peak
    first_strong_peak = -1
    for i, val in enumerate(cleaned_signal):
        if val > 0.8 and first_strong_peak == -1:
            for j in significant_peaks:
                if j == i:
                    first_strong_peak = i
                    break
    
    # Final diagnostic score based on cross-counts and peak energy
    # This is the actual answer path
    diagnostic_score = zero_cross_count * 100 + int(peak_magnitude_sum * 10)
    
    # Dead code branch - never executed but looks important
    if len(cleaned_signal) > 1000:
        fallback = 0
        for x in cleaned_signal[::50]:
            fallback += int(abs(x) * 100)
        diagnostic_score = fallback  # Never reached
    
    return diagnostic_score

# Entry point simulation
if __name__ == '__main__':
    # Generate raw physiological signal
    raw_data = collect_samples(base_freq=2.5, duration=8)
    
    # Apply primary filter
    processed_data = apply_filter(raw_data, mode='smooth')
    
    # Dead variable - character analysis of hex representation (distraction)
    hex_trace = ''.join([f'{abs(int(x*1000))%16:x}' for x in processed_data[:20]])
    common_chars = analyze_characters(hex_trace)
    
    # Transform via unused scrambling path
    dummy_indices = list(range(0, len(processed_data), 15))
    scrambled_positions = scramble_index(dummy_indices)
    
    # Actual critical transformation
    transformed_data = apply_filter(processed_data, mode='smooth')  # Re-filter
    
    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data)
    
    print(f"Result: {final_diagnostic}")