import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [127, 63, 255, 91, 182, 34, 150, 201]

def apply_noise_filter(data):
    # Irrelevant smoothing (distractor)
    smoothed = [(data[i] + data[(i+1)%len(data)]) // 2 for i in range(len(data))]
    return smoothed

def extract_signal_peaks(data):
    # Real signal extraction: find local maxima
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks

def compute_checksum(values):
    # Distractor function: not used in final calculation
    chk = 0
    for v in values:
        chk = (chk ^ v) * 1103515245 % (2**31)
    return chk

def transform_signal(x):
    # Apply non-linear transformation
    return int((x ^ 128) * 1.5) if x % 2 == 0 else int(x * 0.75)

def analyze_pattern(data, limit):
    # Core logic: count how many transformed values exceed limit after XOR adjustment
    adjusted = [transform_signal(val) ^ 32 for val in data]
    count = sum(1 for x in adjusted if x > limit)
    magnitude = sum(abs(x) for x in adjusted) / len(adjusted)
    score = count * magnitude
    return int(score)

def legacy_calibrate(seq):
    # Dead code path — never called
    return [s >> 2 for s in seq if s & 1]

def deprecated_normalize(arr):
    # Unused normalization
    mean = sum(arr) / len(arr)
    return [a - mean for a in arr]

def main():
    # Step 1: Fetch raw sensor readings
    raw_data = fetch_raw_readings()  # [127, 63, 255, 91, 182, 34, 150, 201]

    # Step 2: Apply irrelevant noise filter (distractor)
    filtered_data = apply_noise_filter(raw_data)

    # Step 3: Extract real signal peaks from original data (relevant)
    significant_peaks = extract_signal_peaks(raw_data)

    # Step 4: Transform peaks using non-linear rules
    transformed_data = [transform_signal(p) for p in significant_peaks]

    # Step 5: Compute unused checksum (red herring)
    dummy_checksum = compute_checksum(transformed_data)

    # Step 6: Define threshold based on bitwise manipulation
    base_threshold = 100
    refined_adjustment = (base_threshold << 1) & 255  # = 200 & 255 = 200
    mask = 7
    threshold = (refined_adjustment ^ mask) + 10  # (200 ^ 7) + 10 = 199 + 10 = 209

    # Step 7: Analyze pattern with transformed data and threshold
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Step 8: Print result (required output format)
    print(f"Target result: {final_diagnostic}")

    # Irrelevant debug prints (distractions)
    # print(f"Peaks: {significant_peaks}")
    # print(f"Transformed: {transformed_data}")
    # print(f"Checksum (unused): {dummy_checksum}")

    return final_diagnostic

if __name__ == "__main__":
    main()