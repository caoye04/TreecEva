import math

# Simulated sensor readings and calibration data
def get_sensor_readings():
    raw_data = [1.2, 3.4, 0.9, 5.1, 2.2, 8.8, 6.3, 7.1, 4.4, 3.9]
    calibrated = list(map(lambda x: round(x * 1.05 + 0.1, 2), raw_data))
    return calibrated[:len(calibrated) // 2 + len(calibrated) % 2]  # Return first half

# Irrelevant preprocessing: signal smoothing (unused path)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(i+2, len(signal))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Misleading auxiliary function: frequency analysis (dead end)
def analyze_frequency(data):
    freq_map = {}
    for d in data:
        bin_key = int(d // 1)
        freq_map[bin_key] = freq_map.get(bin_key, 0) + 1
    sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    dominant = sorted_freq[0][0] if sorted_freq else 0
    return [dominant, len(sorted_freq)]

# Core logic disguised among distractions
def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    stability_score = math.exp(-variance / (baseline + 1e-5))
    return stability_score > 0.7

# Decoy state tracker (looks important but unused in final result)
class SystemMonitor:
    def __init__(self):
        self.logs = []
        self.alert_count = 0
    
    def record(self, value):
        self.logs.append(value)
        if value < 1.0:
            self.alert_count += 1

# Another red herring: complex filter chain that's never invoked
def apply_filter_chain(data):
    filters = [
        lambda d: [x for x in d if x > 1.5],
        lambda d: [x for x in d if x < 7.5],
        lambda d: sorted(d, reverse=True)
    ]
    result = data.copy()
    for f in filters:
        result = f(result)
    return result

# Key higher-order function with nested logic and distractors
def system_status(condition_checker):
    def wrapper(input_data):
        # Real processing begins here
        processed = [x * 1.1 for x in input_data if x > 0.5]  # Actual relevant transformation
        
        # Distractor: irrelevant normalization
        total = sum(processed)
        normalized = [p / (total + 1e-8) for p in processed]
        
        # More misdirection: entropy calculation (not used in decision)
        entropy = -sum(p * math.log(p + 1e-8) for p in normalized)
        
        # Critical path hidden in closure logic
        threshold = 4.0
        above_threshold = len([x for x in processed if condition_checker(x)])
        below_critical = len([x for x in processed if x < 2.0])
        
        # Actual decision logic (non-obvious due to surrounding noise)
        if above_threshold >= 3 and below_critical == 0:
            return 1001
        elif above_threshold >= 1:
            return 501
        else:
            return 101
    return wrapper

# Unused diagnostic tree (complex but irrelevant)
def full_diagnostic_tree(data):
    if len(data) == 0:
        return {'status': 'empty', 'code': -1}
    elif len(data) == 1:
        return {'status': 'singleton', 'code': -2}
    else:
        return {'status': 'normal', 'code': len(data)}

# Execution flow with misleading intermediate steps
readings = get_sensor_readings()

# Fake monitoring initialization
monitor = SystemMonitor()
for val in readings:
    monitor.record(val)

# Apply fake transformations that look meaningful
frequency_profile = analyze_frequency(readings)
dummy_filtered = apply_filter_chain(readings)

# Real but obscured computation
stability = evaluate_stability(readings)  # Used indirectly via control flow?

# HIDDEN BRANCH: this condition looks like a shortcut but is actually bypassed
temp_result = None
if len(readings) > 10:
    temp_result = sum(dummy_filtered) // 2
else:
    # This branch runs, but temp_result is never used again
    temp_result = frequency_profile[0] * 100

# THE KEY STATEMENT — answer determined here
final_diagnostic = system_status(lambda x: x > threshold)(readings)

# Print required output
print(f"Result: {final_diagnostic}")