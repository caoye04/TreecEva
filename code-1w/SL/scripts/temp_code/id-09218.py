import itertools

# Simulated sensor data processing pipeline with diagnostic analysis
def collect_samples(duration, rate=100):
    # Generate time-series samples (irrelevant beyond initial data supply)
    return [((i * 0.01) ** 2 + 9.8 * i * 0.01) for i in range(int(duration * rate))]


def filter_noise(samples, kernel_size=3):
    # Simple moving average filter (partially relevant)
    filtered = []
    pad = kernel_size // 2
    extended = [samples[0]] * pad + samples + [samples[-1]] * pad
    for i in range(len(samples)):
        window = extended[i:i + kernel_size]
        filtered.append(sum(window) / len(window))
    return filtered


def extract_peaks(signal, sensitivity=0.5):
    # Identify rising and falling peaks (red herring: not used in final path)
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > sensitivity:
            peaks.append((i, signal[i]))
    return peaks


def compute_checksum(data_chunk):
    # Irrelevant cryptographic checksum (distractor)
    chk = 0
    for val in data_chunk:
        chk ^= int(val * 100) & 0xFF
        chk = (chk << 1) | (chk >> 7)
        chk &= 0xFF
    return chk


def compress_signal(raw_signal):
    # Key transformation: run-length encoding of quantized values
    quantized = [int(x * 4) / 4.0 for x in raw_signal]  # Quantize to 0.25 intervals
    compressed = []
    count = 1
    for i in range(1, len(quantized)):
        if quantized[i] == quantized[i-1]:
            count += 1
        else:
            compressed.append((quantized[i-1], count))
            count = 1
    compressed.append((quantized[-1], count))
    return compressed


def validate_frame(sequence):
    # Dead code path — never actually called (decoy)
    total = sum(count for _, count in sequence)
    parity = sum(int(val * 10) for val, _ in sequence) % 2
    return total > 0 and parity == 1


def analyze_signal(compressed_data, threshold):
    # Core analysis logic (only this contributes to answer)
    magnitude_score = 0.0
    activation_count = 0
    
    # Secondary filtering based on run length and value
    for value, run_length in compressed_data:
        if run_length >= 3:  # Stable segments only
            normalized = abs(value - 4.5)  # Reference baseline
            if normalized > threshold:
                magnitude_score += normalized * run_length
                activation_count += 1
    
    # Decoy intermediate calculation (misleading)
    dummy_metric = (magnitude_score * 1000) % 777
    temp_adjustment = 0
    for i in range(5):
        temp_adjustment += (dummy_metric // (i + 1)) % 100
    
    # Final diagnostic depends only on magnitude_score
    final_weight = 3.75
    final_diagnostic = int(magnitude_score * final_weight)  # Truncate to integer
    
    # Unused branching (dead code)
    if final_diagnostic < 0:
        final_diagnostic = -final_diagnostic
    elif final_diagnostic == 42:
        final_diagnostic = 0  # Easter egg that won't trigger

    return final_diagnostic

# === Main Execution Pipeline ===
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    raw_samples = collect_samples(duration=2.5)

    # Step 2: Apply noise filtering
    clean_signal = filter_noise(raw_samples)

    # Step 3: Extract diagnostic peaks (unused - red herring)
    significant_peaks = extract_peaks(clean_signal, sensitivity=0.3)

    # Step 4: Compute data checksum (irrelevant side channel)
    checksum = compute_checksum(clean_signal[:50])  # Partial segment

    # Step 5: Compress signal for transmission efficiency
    compressed_data = compress_signal(clean_signal)

    # Step 6: Simulate frame validation (never invoked)
    # validate_frame(compressed_data)  # Commented out — dead path

    # Step 7: Analyze compressed signal for anomaly detection
    threshold = 1.25
    final_diagnostic = analyze_signal(compressed_data, threshold)

    # Step 8: Print result (required format)
    print(f"Result: {final_diagnostic}")
