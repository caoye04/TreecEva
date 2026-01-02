from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor array data with noise and calibration offsets
def generate_raw_signals():
    base = [12.5, -3.2, 8.7, 19.1, 0.0, -7.6, 4.3]
    noise = [0.1, -0.2, 0.3, -0.1, 0.05, -0.15, 0.25]
    return [b + n for b, n in zip(base, noise)]

def calibrate_signal(value, factor=1.02, offset=0.05):
    # Over-engineered calibration with red herring parameters
    temp_log = []
    for i in range(5):
        temp_log.append((value * factor) + offset)
    return temp_log[-1]  # Only last value used

def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    filtered = [x for x in data if abs(x - median_val) < threshold]
    return filtered if len(filtered) > 3 else data  # fallback

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        segment = values[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    return smoothed

def accumulate_trend(readings):
    trend = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend += 1
        elif readings[i] < readings[i-1]:
            trend -= 0.5
    return trend * 1.5  # arbitrary scaling

# Distractor: Unused complex transformation
def spectral_decompose(signal_list):
    result = []
    for x in signal_list:
        comp = (x ** 2 + 1j * x) / (x + 0.1)
        result.append(abs(comp))
    return result

# Misleading intermediate diagnostic (dead end)
def legacy_diagnostic(arr):
    count_pos = sum(1 for x in arr if x > 0)
    count_neg = sum(1 for x in arr if x < 0)
    return (count_pos * 2) - (count_neg * 3)

# Real processing chain
def preprocess_signal(raw_data):
    calibrated = [calibrate_signal(x) for x in raw_data]
    denoised = rolling_average(calibrated)
    cleaned = filter_outliers(denoised)
    return cleaned

# Critical function with hidden logic dependency
def analyze_readings(cleaned_readings):
    stats = defaultdict(float)
    stats['length'] = len(cleaned_readings)
    stats['base_sum'] = sum(cleaned_readings)
    
    # Hidden key computation path
    trend_score = accumulate_trend(cleaned_readings)
    stats['trend'] = trend_score
    
    # Irrelevant aggregation
    magnitude_count = Counter()
    for val in cleaned_readings:
        bucket = f"{int(abs(val))}"
        magnitude_count[bucket] += 1
    
    # Decoy statistic
    stats['entropy_approx'] = len(magnitude_count) * 0.7
    
    # Key logical junction: conditional override based on pattern
    pattern_cycle = cycle([1, -1, 0])
    parity_check = sum(a * b for a, b in zip(islice(pattern_cycle, len(cleaned_readings)), cleaned_readings))
    
    if abs(parity_check) < 5.0:
        adjustment = 23
    else:
        adjustment = -17
    
    # Final diagnostic depends on both trend and adjustment
    final_value = int(stats['base_sum'] + stats['trend'] + adjustment)
    
    # Red herring: unused detailed breakdown
    debug_trace = []
    for k, v in stats.items():
        debug_trace.append(f"{k}: {v:.3f}")
    
    return final_value

# Orchestration with misleading branches
if __name__ == "__main__":
    raw_signals = generate_raw_signals()
    
    # Distractor block: alternate path never taken
    if sum(raw_signals) < 0:
        processed_signals = [x * 2 for x in raw_signals]
    else:
        processed_signals = preprocess_signal(raw_signals)  # Actual path
    
    # Another decoy function call (no side effects)
    _ = legacy_diagnostic(raw_signals)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print required output
    print(f"Result: {final_diagnostic}")