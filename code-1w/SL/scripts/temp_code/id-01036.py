import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw_signals = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
    filtered = [x for x in raw_signals if x > 0.5]  # Remove low noise
    return [round(math.sqrt(x), 3) for x in filtered]

# Irrelevant helper: historical metadata (distractor)
def get_metadata():
    return {
        'device_id': 'SEN-9X',
        'firmware': '2.1.7',
        'calibration_date': '2023-05-14',
        'useless_flag': True,
        'temp_offset': -0.3
    }

# Signal transformation with red herring operations
def transform(signal_list):
    shifted = [val * 1.5 for val in signal_list]
    offset = 2.1
    adjusted = [v + offset for v in shifted]
    
    # Decoy computation: looks important but unused later
    envelope = max(adjusted) - min(adjusted)
    threshold = math.floor(envelope / 2)
    spike_count = sum(1 for x in adjusted if x > threshold)
    
    # Actual relevant path
    squared_chain = []
    temp = 1
    for i in range(len(adjusted)):
        temp = (temp * (i + 1)) % 1000
        squared_chain.append(temp)
    
    # Mix in some bit manipulation (relevant part)
    final_bits = 0
    for s in squared_chain[-3:]:
        final_bits ^= int(s) & 255  # Use last 8 bits
    
    return adjusted, final_bits

# Data windowing - slicing operation used here
def slice_window(data, size=4):
    if len(data) < size:
        return data[:]
    mid = len(data) // 2
    return data[mid - size//2 : mid + size//2]

# Secondary analysis with decoy logic
def assess_quality(window):
    mean_val = sum(window) / len(window)
    variance = sum((x - mean_val) ** 2 for x in window) / len(window)
    quality_score = 100 / (1 + variance) if variance > 0 else 100
    
    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: Quality={quality_score}')
    
    # This is actually used
    return round(quality_score, 2)

# Core diagnostic algorithm with lambda and list comprehension
# Also uses integer division and accumulation
analyze_signal = lambda data: (
    sum([
        (data[i] // 1) * (i % 3 + 1)  # Integer division and indexing
        for i in range(0, len(data), 2)
    ]) + 
    len([x for x in data if x > 3.0]) * 7  # Bonus points for high values
)

# Unused function: misleading intermediate result
def compute_baseline():
    base = 0
    for k in range(1, 10):
        base += k ** 2
    return base // 3

# Main execution flow
if __name__ == '__main__':
    samples = collect_samples()                    # Step 1: collect data
    processed_data, fingerprint = transform(samples) # Step 2: transform
    
    # Distractor: unused variables
    audit_log = {'entries': [], 'status': 'pending'}
    calibration_matrix = [[1.0 for _ in range(3)] for _ in range(3)]
    
    # Slicing out a window (relevant)
    focus_window = slice_window(processed_data)      # Step 3: extract window
    
    # Distractor: quality assessment computed but not used in final answer
    quality_metric = assess_quality(focus_window)
    
    # Final diagnostic calculation (answer point)
    final_diagnostic = analyze_signal(processed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")