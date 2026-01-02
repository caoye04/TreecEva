def process_sensor_data(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: normalize data (not actually used in final result)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > 0.1]

    # Distractor: complex but unused signal transformation
    transformed = []
    for val in raw_readings:
        if val % 3 == 0:
            transformed.append(val ** 2)
        elif val % 5 == 0:
            transformed.append(val * 2)
        else:
            transformed.append(val + 1)

    # Real computation begins: extract high-frequency events
    event_markers = set()
    for i, reading in enumerate(raw_readings):
        if reading > threshold * max(raw_readings):
            event_markers.add(i)

    # Secondary distractor: simulate system diagnostics (dead code path)
    def run_diagnostics(code=42):
        status_flags = {"OK": 0, "WARN": 1, "ERROR": 2}
        if sum(transformed) > 1000:
            return status_flags["ERROR"]
        return status_flags["OK"]

    # Unused recursive function (red herring)
    def recursive_sum(n):
        return n + recursive_sum(n - 1) if n > 0 else 0

    # Core logic: detect pattern in event spacing
    intervals = []
    last = None
    for idx in sorted(event_markers):
        if last is not None:
            intervals.append(idx - last)
        last = idx

    # Analyze interval symmetry (key operation)
    interval_set = set(intervals)
    reversed_set = set([intervals[-i-1] for i in range(len(intervals))])
    symmetric = interval_set == reversed_set and len(intervals) > 0

    # Bit manipulation decoy (looks important but unused)
    checksum = 0
    for val in raw_readings:
        checksum ^= int(val) & 0xF
        checksum = (checksum << 1) | (checksum >> 3)
        checksum &= 0xF

    # Real result derived from logical combination
    magnitude_score = sum(1 for x in raw_readings if x > threshold * max(raw_readings))
    temporal_score = len(intervals) * 2
    stability_flag = 1 if len(set(raw_readings[-3:])) == 1 else 0

    # Final diagnostic calculation (this is where the answer comes from)
    base_diagnostic = magnitude_score * temporal_score + (stability_flag << 3)
    adjustment = 5 if symmetric else -3
    final_diagnostic = base_diagnostic + adjustment

    # Dead branch: never executed due to condition
    if min(raw_readings) < 0:
        final_diagnostic *= -1

    # Key assignment statement
    final_diagnostic = analyze_pattern(collected_signals, system_key)

    # Print result as required
    print(f"Result: {final_diagnostic}")

# External definitions needed for execution

def analyze_pattern(signal_list, key):
    # This function simulates a pattern matcher using set operations
    base_set = set(range(0, len(signal_list), 2))  # Even indices
    signal_peaks = {i for i, val in enumerate(signal_list) if val > 25}
    matched = base_set.intersection(signal_peaks)
    if key == 'A':
        matched = matched.difference({0, 2})
    elif key == 'B':
        matched = matched.union({len(signal_list)})
    return len(matched) * 7 - 3

# Input data
collected_signals = [10, 20, 30, 15, 25, 35, 40, 18, 22]
system_key = 'A'

# Execute main logic
process_sensor_data(collected_signals)