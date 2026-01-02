from collections import defaultdict, Counter
import itertools

# Simulated health monitoring system with sensor data processing
def analyze_rhythm(pattern):
    if len(pattern) < 3:
        return False
    return all(a <= b for a, b in zip(pattern, pattern[1:]))

def compute_entropy(sequence):
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 4)

def extract_peaks(values):
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i-1] < values[i] > values[i+1]:
            peaks.append(values[i])
    return peaks or [0]

def dummy_validation(data):
    # Irrelevant validation function - dead code path
    return sum(len(str(x)) for x in data) % 7 == 0

def deprecated_normalization(arr):
    # Unused normalization method - misleading
    mean_val = sum(arr) / len(arr)
    return [round((x - mean_val) / mean_val * 100, 2) for x in arr]

def generate_combinations(items):
    # Distractor: generates combinations but not used in main logic
    combs = []
    for r in range(2, min(4, len(items)+1)):
        combs.extend(itertools.combinations(items, r))
    return combs[:10]

def filter_outliers(seq, factor=1.5):
    # Not actually used; decoy preprocessing
    if len(seq) < 4:
        return seq
    q1, q3 = sorted(seq)[len(seq)//4], sorted(seq)[-len(seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if lower <= x <= upper]

def accumulate_diagnostics(readings):
    # Complex but partially irrelevant accumulation
    history = defaultdict(int)
    trend_scores = []
    for idx, val in enumerate(readings):
        history[f'bucket_{val % 7}'] += 1
        if idx % 3 == 0:
            trend_scores.append(val * (idx % 5))
    score = sum(trend_scores) % 97
    return score

# Main processing function
def process_metrics(sensor_data, config_thresholds):
    
    # Step 1: Extract core signal from nested structure
    raw_signals = [entry['signal'] for entry in sensor_data if entry.get('active')]
    flattened = list(itertools.chain.from_iterable(raw_signals))
    
    # Step 2: Compute primary metrics (only some are used later)
    avg_signal = sum(flattened) / len(flattened)
    peak_values = extract_peaks(flattened)
    max_peak = max(peak_values)
    
    # Step 3: Analyze rhythm using first segment
    rhythm_segment = [x for x in flattened if x > avg_signal][:10]
    has_stable_rhythm = analyze_rhythm(rhythm_segment)
    
    # Step 4: Calculate entropy on transformed data
    transformed = [x // 10 for x in flattened if x > 0]
    signal_entropy = compute_entropy(transformed)
    
    # Step 5: Use Counter to track frequency distribution
    freq_dist = Counter(transformed)
    dominant_band = freq_dist.most_common(1)[0][1]
    
    # Step 6: Generate unused feature combinations (distractor)
    _ = generate_combinations(list(freq_dist.keys()))
    
    # Step 7: Accumulate diagnostic score from readings (red herring)
    _ = accumulate_diagnostics(flattened)
    
    # Step 8: Real computation path begins here — depends on thresholds
    threshold_match = sum(1 for x in flattened if x > config_thresholds['critical'])
    
    # Step 9: Conditional branching based on rhythm and threshold
    if has_stable_rhythm and threshold_match > 3:
        base_score = avg_signal * 1.7
    elif signal_entropy > 2.0:
        base_score = dominant_band * 12.5
    else:
        base_score = max_peak * 0.85
    
    # Step 10: Final adjustment using bit manipulation (key step)
    adjusted = int(base_score) ^ 4321
    final_value = (adjusted & 0xFFFF) + (adjusted >> 16)
    
    # Step 11: Apply modulo to bound result
    bounded_result = final_value % 8999
    
    # Step 12: Final diagnostic assignment (target)
    final_diagnostic = abs(bounded_result - 1337)
    
    # Misleading print — distractor output
    debug_code = (sum(flattened[:5]) * 1000) % 997
    print(f'Debug token: {debug_code}')
    
    return final_diagnostic

# Simulated input data
health_data = [
    {'signal': [120, 135, 142, 150, 148, 160, 175, 180], 'active': True},
    {'signal': [110, 115, 125, 130], 'active': True},
    {'signal': [90, 95, 100], 'active': False},  # Inactive entry
    {'signal': [165, 170, 172, 178, 185, 190, 195, 200, 205], 'active': True}
]

thresholds = {
    'warning': 130,
    'critical': 170,
    'relaxation': 100
}

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f'Result: {final_diagnostic}')