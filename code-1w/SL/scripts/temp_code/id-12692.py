def preprocess_signal(raw_data, threshold=0.5):
    """Irrelevant preprocessing for distraction."""
    filtered = [x for x in raw_data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def transform_coordinates(points):
    """Dead function - never called, distractor."""
    return [(p[1] * 2, p[0] * -1) for p in points]


def accumulate_magnitude(seq):
    """Used in signal chain - relevant."""
    total = 0.0
    for val in seq:
        total += abs(val)
    return total


def extract_peaks(data):
    """Find local maxima - part of real logic."""
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append((i, data[i]))
    return peaks


def shift_window(sequence, offset):
    """Misleading transformation - used but ultimately irrelevant."""
    shifted = [0] * offset
    shifted.extend(sequence[:-offset])
    return shifted


def generate_bands(magnitudes):
    """Classify magnitude levels - red herring with partial relevance."""
    bands = {'low': 0, 'med': 0, 'high': 0}
    for m in magnitudes:
        if m < 10:
            bands['low'] += 1
        elif m < 50:
            bands['med'] += 1
        else:
            bands['high'] += 1
    return bands


def compute_entropy(values):
    """Unused complex math - pure distraction."""
    from math import log
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * log(p)
    return entropy


def rolling_average(data, window_size=3):
    """Actually unused despite being plausible - dead path."""
    averages = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        averages.append(avg)
    return averages


def analyze_readings(signals):
    """Core analysis function - contains key logic."""
    cumulative_energy = 0
    all_coords = [(x, y) for x in range(3) for y in range(3)]
    temp_grid = {i: [] for i in range(5)}  # Unused structure

    # Real logic begins
    processed_magnitudes = []
    for idx, sig in enumerate(signals):
        energy = 0
        for sample in sig:
            if sample < -10:
                energy += sample ** 2 / 100
            elif sample > 10:
                energy += sample ** 2 / 100
        processed_magnitudes.append(energy)

    # Key transformation
    adjusted = [m * 1.5 for m in processed_magnitudes if m > 0]

    # Real accumulation
    temp_sum = 0
    for i, val in enumerate(adjusted):
        temp_sum += val * (i + 1)  # Weight by index

    # Secondary processing
    peak_count = 0
    for series in signals:
        sorted_series = sorted(series)
        mid = sorted_series[len(sorted_series)//2]
        if mid > 0:
            peak_count += 1

    # Distractor: zip and enumerate used meaningfully but not critical
    labels = ['A', 'B', 'C']
    for i, (lbl, sig) in enumerate(zip(labels, signals)):
        _ = f"{lbl}_{i}: {len(sig)}"  # Computed but unused

    # Final computation
    diagnostic_score = int(temp_sum + peak_count * 2.7)

    # Irrelevant sorting
    dummy_list = [3, 1, 4, 1, 5]
    dummy_list.sort(reverse=True)

    # This is the actual answer variable
    final_diagnostic = diagnostic_score + 50
    return final_diagnostic


def main():
    # Input data
    sensor_readings = [
        [-12.1, 5.3, -15.0, 8.2],
        [9.1, 11.5, -6.7, 20.3],
        [2.0, -3.5, 4.1, -13.9]
    ]

    # Irrelevant pre-processing steps
    clean_data = []
    for reading in sensor_readings:
        cleaned = [r for r in reading if r != 0]
        clean_data.append(cleaned)

    baseline_shift = 0.0
    for group in clean_data:
        baseline_shift += sum(group) / len(group)

    # Another distraction
    time_stamps = [1001, 1002, 1003]
    timestamp_map = dict(zip(time_stamps, labels)) if 'labels' in locals() else {}

    # Actual processing pipeline
    processed_signals = []
    for raw in clean_data:
        # Apply real but hidden transformation
        transformed = [x * 0.8 for x in raw]
        processed_signals.append(transformed)

    # Core call
    final_diagnostic = analyze_readings(processed_signals)

    # Print result as required
    print(f"Target result: {final_diagnostic}")

# Simulate execution
if __name__ == "__main__":
    main()