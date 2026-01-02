import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_signal = [0.1, 0.8, 1.3, 0.9, 2.1, 3.5, 4.2, 3.9, 5.0, 6.1, 5.8]
    baseline = 1.0
    adjusted = [x - baseline for x in raw_signal]
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_filter(data):
    if len(data) == 0:
        return []
    result = []
    for i in range(len(data)):
        if data[i] > 0.5:
            result.append(data[i])
    return sorted(result)[::-1]

# Signal transformation with slicing and windowing
def apply_window(signal, size=3):
    windows = []
    for i in range(len(signal) - size + 1):
        windows.append(signal[i:i+size])
    return windows

# Misleading intermediate computation - looks important but unused in final result
def compute_entropy(seq):
    from math import log
    freq = {}
    for val in seq:
        freq[val] = freq.get(val, 0) + 1
    total = len(seq)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Core pattern analyzer using logical conditions and itertools combinations
def analyze_pattern(windows, limit):
    valid_patterns = 0
    critical_flags = []
    
    # Complex nested logic with red herrings
    for window in windows:
        center_val = window[1]
        left_edge = window[0] < 0.5
        right_edge = window[2] > 0.7
        
        # Logical combination that appears significant
        if left_edge and not right_edge:
            flag = 'A'
        elif right_edge and abs(center_val) > 1.0:
            flag = 'B'
        else:
            flag = 'C'
        
        critical_flags.append(flag)
        
        # Actual determining condition buried among distractions
        trend = window[2] - window[0]
        magnitude = sum(abs(x) for x in window)
        
        # Real logic path - subtle condition
        if trend > 0.8 and magnitude > limit:
            valid_patterns += 1
    
    # Decoy aggregation - never used
    flag_distribution = {k: len(list(g)) for k, g in itertools.groupby(sorted(critical_flags))}
    
    # Final computation - only this matters
    checksum = 0
    for i, win in enumerate(windows):
        if i % 2 == 0:
            checksum += int(sum(win) * 10)
    
    return valid_patterns * 1000 + checksum

# Secondary transformation chain
# This looks like preprocessing but only one output is used
def preprocess_stream(raw_readings):
    shifted = [round(x + 0.05, 2) for x in raw_readings]
    clipped = [min(max(x, 0.0), 2.0) for x in shifted]  # capping values
    smoothed = []
    for i in range(1, len(clipped)-1):
        avg = (clipped[i-1] + clipped[i] + clipped[i+1]) / 3
        smoothed.append(round(avg, 2))
    return shifted, clipped, smoothed  # Only 'shifted' is actually used later

# Unused diagnostic routine - distractor function
def validate_calibration(signal):
    if not signal:
        return False
    peaks = [i for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1]]
    return len(peaks) >= 2

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect sensor data
    readings = collect_readings()
    
    # Step 2: Apply preprocessing (multiple outputs, only one used)
    full_shifted, _, _ = preprocess_stream(readings)
    
    # Step 3: Transform into sliding windows - relevant
    transformed_data = apply_window(full_shifted, size=3)
    
    # Step 4: Compute irrelevant entropy (distractor)
    _ = compute_entropy([int(x*10) for x in full_shifted if x > 0])
    
    # Step 5: Set threshold based on misleading formula
    dynamic_level = sum(readings) / len(readings)
    threshold = abs(dynamic_level) * 2.5  # Looks adaptive but effectively constant
    
    # Step 6: Call key function - answer determined here
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print final result as required
    print(f"Result: {final_diagnostic}")