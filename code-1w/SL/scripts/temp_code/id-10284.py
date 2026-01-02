from collections import defaultdict, Counter

# Simulated sensor data aggregation for a health monitoring system
def collect_readings():
    readings = [105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
    offset = 5
    adjusted = [r + offset for r in readings]
    return adjusted

# Legacy function – unused but looks relevant
def calculate_stress_index(data):
    return sum(d ** 0.5 for d in data if d > 120) // len(data)

# Noise filter with red herring logic
def apply_filter(signal):
    filtered = []
    noise_floor = 100
    for s in signal:
        if s < noise_floor:
            continue
        if s % 10 == 0:
            filtered.append(s * 1.1)
        else:
            filtered.append(s * 0.9)
    return [int(f) for f in filtered]

# Bitmask-based mode selector (distractor)
def get_device_mode(config_word):
    mode = 0
    if config_word & 1:
        mode += 1
    if config_word & 2:
        mode += 2
    if config_word & 8:
        mode += 3
    return mode  # never actually used

# Core processing with meaningful logic buried
threshold_map = defaultdict(lambda: 125)
thresh_pairs = [("critical", 140), ("elevated", 130), ("normal", 120)]
for label, val in thresh_pairs:
    threshold_map[label] = val

status_flags = [True, False, True]
flag_sum = sum(status_flags)  # red herring

raw_data = collect_readings()
processed_signal = apply_filter(raw_data)

# Irrelevant transformation using slicing and conditional expressions
decoy_sequence = processed_signal[::2] if len(processed_signal) > 8 else processed_signal[:5]
shadow_copy = [x // 2 if x > 130 else x for x in decoy_sequence]

# Real computation begins here — subtle entry point
def analyze_trend(seq):
    trend_scores = []
    for i in range(1, len(seq)):
        diff = seq[i] - seq[i-1]
        score = diff * (1 if diff > 0 else -2)
        trend_scores.append(score)
    return trend_scores

analysis_result = analyze_trend(processed_signal)

# Misleading aggregation
aggregate_noise = sum([x ^ 7 for x in shadow_copy])  # XOR red herring

# Key data structure with cross-references
class MetricEngine:
    def __init__(self, base_vals):
        self.raw = base_vals
        self.histogram = Counter(base_vals)
        self.peaks = tuple(sorted(set(self.raw)))
        self.peak_shift = self.peaks[-1] - self.peaks[0]  # used later

    def compute_baseline(self):
        mid_vals = sorted(self.raw)[len(self.raw)//4 : -(len(self.raw)//4)]
        return sum(mid_vals) / len(mid_vals)

engine = MetricEngine(processed_signal)
baseline = engine.compute_baseline()

# Conditional logic chain with distractors
adjustment_factor = 1.0
if engine.peak_shift > 50:
    adjustment_factor *= 0.9
elif engine.peak_shift < 30:
    adjustment_factor *= 1.1
else:
    adjustment_factor *= 1.05

# Another decoy function call
mode_code = get_device_mode(5)

# Central calculation obscured by context
rolling_deltas = [abs(analysis_result[i+1] - analysis_result[i]) for i in range(len(analysis_result)-1)]
smoothness = sum(rolling_deltas) // len(rolling_deltas) if rolling_deltas else 0

# Final decision logic with multiple inputs, only some matter
suspicious_count = len([x for x in engine.histogram.values() if x == 1])

scaling_constant = 3
# Real formula starts here — depends on baseline, smoothness, peak_shift
interim = int(baseline) + smoothness
interim ^= engine.peak_shift  # XOR in peak shift
interim += suspicious_count * scaling_constant

# This function appears complex but has one real path
def process_metrics(data, thresholds):
    critical_level = thresholds["critical"]
    elevated_level = thresholds["elevated"]
    count_high = sum(1 for x in data if x >= critical_level)
    count_moderate = sum(1 for x in data if elevated_level <= x < critical_level)
    
    # Distraction: unused branch
    if count_high > 5:
        impact_score = 999
    elif count_high == 0:
        impact_score = 111
    else:
        impact_score = 500
    
    # Actual dependency: combines interim and flag_sum (which is irrelevant)
    diagnostic_weight = impact_score // 100
    final_value = interim * diagnostic_weight + flag_sum  # flag_sum is distraction
    return final_value

# Key execution point
final_diagnostic = process_metrics(processed_signal, threshold_map)
print(f"Result: {final_diagnostic}")