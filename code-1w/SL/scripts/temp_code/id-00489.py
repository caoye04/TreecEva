def analyze_signal(raw_samples, filter_threshold):
    filtered = [x for x in raw_samples if abs(x) > filter_threshold]
    offset = sum(filtered) // len(filtered) if filtered else 0
    adjusted = [x - offset for x in raw_samples]
    return adjusted


def transform_segments(data, window_size):
    segments = []
    for i in range(0, len(data) - window_size + 1, window_size // 2):
        segment = data[i:i + window_size]
        if len(segment) == window_size:
            segments.append(segment)
    transposed = list(zip(*segments))
    transformed = [sum(col) / len(col) for col in transposed]
    padding = [0] * (8 - len(transformed))
    return transformed + padding


def calculate_equilibrium(signal, limit):
    magnitude = sum(abs(x) for x in signal)
    scale_factor = 1.0 if magnitude == 0 else 100.0 / magnitude
    scaled = [x * scale_factor for x in signal]
    
    # Distractor: irrelevant frequency analysis
    peak = max(scaled, key=abs)
    peaks = [x for x in scaled if abs(x) > 0.5 * abs(peak)]
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    
    # Actual computation path
    center_slice = scaled[3:-3] if len(scaled) > 6 else scaled
    moment = sum(i * val for i, val in enumerate(center_slice))
    inertia = sum(val ** 2 for val in center_slice)
    balance = moment / inertia if inertia != 0 else 0
    
    # More distractions
    noise_floor = sum(1 for x in scaled if abs(x) < 1) * 0.1
    entropy_proxy = len(set(round(x, 1) for x in scaled))
    
    equilibrium = int(abs(balance * 100)) % 97
    return equilibrium

# Main execution
raw_signal = [12, -7, 3, -1, 8, 15, -21, 4, 9, -6, 2, 5, -8, 11, -14, 18]
threshold = 4

# Irrelevant preprocessing chain
normalized = [x / max(map(abs, raw_signal)) * 20 for x in raw_signal]
denoised = [x for x in normalized if x != 0]
expanded = denoised[:8] + [denoised[i % len(denoised)] for i in range(8, 16)]

processed = analyze_signal(expanded, threshold // 2)
processed = transform_segments(processed, 4)

# Key statement
equilibrium = calculate_equilibrium(processed, threshold)

print(f"Result: {equilibrium}")