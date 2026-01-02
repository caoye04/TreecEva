import itertools

# System health monitoring simulation with signal processing

def collect_diagnostics(raw_samples, mode='standard'):
    cumulative_energy = 0
    transient_peaks = []
    baseline_shift = 0
    harmonic_cache = set()
    temp_shadow = 0  # Irrelevant metric

    for i, sample in enumerate(raw_samples):
        if i % 4 == 0:
            baseline_shift += sample * 0.1

        adjusted = abs(sample - baseline_shift)
        if adjusted > 50:
            transient_peaks.append(i)

        if sample % 7 == 0:
            harmonic_cache.add(sample)

        # Distractor computation
        temp_shadow += (sample ^ i) % 3

        cumulative_energy += sample ** 2

    return cumulative_energy, transient_peaks, harmonic_cache


def compute_entropy(data_list):
    from math import log2
    freq_map = {}
    total = len(data_list)
    for item in data_list:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy if total > 0 else 0.0

# Misleading auxiliary function (dead code path)
def deprecated_filter(seq, limit=100):
    result = []
    warning_flags = []
    for x in seq:
        if x < 0:
            warning_flags.append('NEG')
        elif x > limit:
            warning_flags.append('HIGH')
    return result  # Never used

# Core analysis engine
def analyze_pattern(signal, config_thresholds):
    segment_length = len(signal)
    critical_windows = []
    rolling_checksum = 0
    phase_tracker = []
    
    # Real computation begins
    for idx in range(0, segment_length, 3):
        window = signal[idx:idx+3]
        if len(window) != 3:
            continue
            
        # Primary logic branch
        if sum(window) > config_thresholds['power']:
            product = 1
            for w in window:
                product *= w
            if product > config_thresholds['stability']:
                critical_windows.append(idx // 3)

        # Secondary condition with distractor
        avg_val = sum(window) / 3
        dummy_mask = 0
        for v in window:
            dummy_mask ^= int(v)  # Bitwise red herring
        
        if avg_val > config_thresholds['noise_floor']:
            phase_tracker.append(dummy_mask % 5)

        # Rolling checksum (used later)
        rolling_checksum += sum(w * (i+1) for i, w in enumerate(window))

    # Use of dictionary to track state transitions
    transition_log = {}
    for i in range(len(phase_tracker) - 1):
        key = (phase_tracker[i], phase_tracker[i+1])
        transition_log[key] = transition_log.get(key, 0) + 1

    # Set operations on detected harmonics (distractor)
    flat_signal = [x for x in signal if x % 2 == 1]
    unique_odds = set(flat_signal)
    superset_check = {x*2 for x in unique_odds}  # Unused

    # Final diagnostic calculation (this is the real answer)
    base_score = len(critical_windows) * rolling_checksum
    penalty = len(transition_log) * 17
    final_diagnostic = base_score - penalty

    # Dead assignment - misleading
    final_diagnostic = max(final_diagnostic, 0) if len(unique_odds) > 10 else final_diagnostic

    return final_diagnostic

# Simulated sensor input
def main():
    readings = [
        12, 58, 21, 67, 33, 44,
        71, 19, 52, 88, 23, 64,
        95, 14, 37, 73, 29, 56,
        48, 82, 31, 69, 25, 53
    ]
    
    # Irrelevant preprocessing
    energy_total, peaks, harmonics = collect_diagnostics(readings)
    signal_entropy = compute_entropy(readings)
    
    # Configuration map with meaningful and irrelevant keys
    thresholds = {
        'power': 100,
        'stability': 50000,
        'noise_floor': 30,
        'decay_rate': 0.85,  # unused
        'timeout': 300       # unused
    }
    
    # Decoy call
    _ = deprecated_filter(readings, limit=200)
    
    # Key statement
    final_diagnostic = analyze_pattern(readings, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()