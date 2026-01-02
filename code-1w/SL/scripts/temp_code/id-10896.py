from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal(raw=True):
    return [i * 0.75 + (i % 3) for i in range(120)] if raw else []

def filter_noise(signal, threshold=15.0):
    filtered = []
    noise_log = defaultdict(int)
    for idx, val in enumerate(signal):
        if abs(val - round(val)) < 0.01:
            noise_log['rounded'] += 1
        elif val > threshold:
            noise_log['clipped'] += 1
        else:
            filtered.append(val)
    # Distractor: noise_log is computed but not used later
    return filtered

def time_compress(signal, factor=3):
    compressed = []
    for i in range(0, len(signal), factor):
        chunk = signal[i:i+factor]
        compressed.append(sum(chunk) / len(chunk))
    return compressed

def extract_peaks(signal, sensitivity=0.8):
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            if signal[i] > sensitivity * max(signal):
                peaks.append((i, signal[i]))
    return peaks

def derive_entropy(values):
    count = Counter(values)
    total = len(values)
    entropy = 0.0
    for v in count.values():
        p = v / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def validate_frame_integrity(frames):
    # Dead code path - never actually called
    issues = 0
    for f in frames:
        if sum(f) % 2 != 0:
            issues += 1
    return issues == 0

def generate_checksum(data):
    # Unused distractor function
    return sum(hash(str(d)[:4]) for d in data) % 10000

def normalize_frame(frame):
    mean_val = sum(frame) / len(frame)
    std_val = math.sqrt(sum((x - mean_val)**2 for x in frame) / len(frame))
    return [(x - mean_val) / (std_val + 1e-8) for x in frame]

def analyze_signal(frames):
    diagnostics = []
    
    # Red herring variables
    temp_analysis = {'stage1': [], 'stage2': []}
    cumulative_shift = 0
    
    for i, frame in enumerate(frames):
        if len(frame) < 5:
            continue
            
        # Real computation begins
        peak_count = len(extract_peaks(frame, sensitivity=0.6))
        frame_entropy = derive_entropy([round(x, 2) for x in frame])
        
        # Intermediate misleading metric
        coherence_score = sum(1 for x in frame if abs(x) > 1.0) / len(frame)
        temp_analysis['stage1'].append(coherence_score)
        
        # Actual relevant logic
        signal_power = sum(x**2 for x in frame)
        if signal_power > 25.0:
            cumulative_shift += 0.3
        
        metric = peak_count * 2.5 + frame_entropy * 3.1 - cumulative_shift
        diagnostics.append(metric)
    
    # Distractor: complex-looking but unused structure
    final_summary = {
        'stats': {
            'avg': sum(diagnostics)/len(diagnostics),
            'max': max(diagnostics),
            'version': 'DX-9'
        },
        'flags': [True, False, True]
    }
    
    # Key statement
    final_diagnostic = int(round(sum(diagnostics) / len(diagnostics)))
    
    # Multiple print statements as distractions (not part of logic)
    # print(f'Signal integrity: {validate_frame_integrity(frames)}')
    # print(f'Checksum ID: {generate_checksum(frames[0])}')
    
    return final_diagnostic

# Main execution flow
raw_data = acquire_signal(raw=True)
denoised_signal = filter_noise(raw_data, threshold=18.5)
compressed_blocks = time_compress(denoised_signal, factor=4)
processed_frames = [normalize_frame(compressed_blocks[i:i+8]) for i in range(0, len(compressed_blocks), 8) if i+8 <= len(compressed_blocks)]

# Irrelevant slicing and transformation
auxiliary_slices = [processed_frames[j][::2] for j in range(len(processed_frames)) if j % 3 == 0]
shadow_copy = [[val * 0.95 for val in row] for row in processed_frames]

# Critical statement
final_diagnostic = analyze_signal(processed_frames)

print(f"Result: {final_diagnostic}")