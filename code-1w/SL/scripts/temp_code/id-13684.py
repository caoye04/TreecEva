import math

# System diagnostics simulator with redacted logic and interference

def analyze_phase_coherence(timestamps):
    if len(timestamps) < 2:
        return 0.0
    phase_shift = 0.0
    for i in range(1, len(timestamps)):
        delta = timestamps[i] - timestamps[i-1]
        phase_shift += math.sin(delta) * math.cos(delta)
    return round(phase_shift, 5)


def detect_anomalies(sensor_readings):
    anomalies = []
    baseline = sum(sensor_readings) / len(sensor_readings)
    variance = sum((x - baseline) ** 2 for x in sensor_readings) / len(sensor_readings)
    threshold = baseline + math.sqrt(variance) * 1.5
    for val in sensor_readings:
        if val > threshold:
            anomalies.append(val)
    # Distractor: unused anomaly processing path
    processed = [math.log(abs(a) + 1) for a in anomalies if a != 0]
    normalized = [p / max(processed) if processed else 1 for p in processed]
    return len(anomalies)

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)

# Core but misleading intermediate calculation
def generate_timing_signature(sequence):
    sig = 0
    for idx, val in enumerate(sequence):
        sig ^= (val + idx) & 255  # Bit manipulation red herring
    sig = (sig * 17) % 101
    return sig

# Unused fault classification tree (dead code path)
class FaultClassifier:
    def __init__(self):
        self.thresholds = {"critical": 90, "warning": 60}

    def classify(self, code):
        if code > 90:
            return 'CRITICAL'
        elif code > 60:
            return 'WARNING'
        else:
            return 'NORMAL'

# Real processing chain with key logic buried under noise
def evaluate_system_health(config_vector, timing_log, events):
    # Distractor variables
    temp_buffer = [x * 1.05 for x in config_vector if x % 2 == 0]
    checksum = sum(temp_buffer) % 1000
    metadata_index = len(events) * 2 // 3

    # Relevant computation hidden among irrelevancies
    event_mask = [1 if e in {'overload', 'spike', 'reset'} else 0 for e in events]
    trigger_count = sum(event_mask)

    coherence = analyze_phase_coherence(timing_log)
    anomaly_count = detect_anomalies(config_vector)

    # Decoy aggregation (never used)
    fake_score = (coherence * 100) + anomaly_count - checksum

    # Actual signal extraction
    valid_timings = [t for t in timing_log if t > 0]
    avg_timing = sum(valid_timings) / len(valid_timings) if valid_timings else 0

    # Key dependency: only this matters for final result
    adjustment_factor = 1 if avg_timing > 50 else -1
    critical_flag = 1 if anomaly_count >= 3 or abs(coherence) > 1.0 else 0

    return adjustment_factor, critical_flag, trigger_count

# Primary data inputs (simulated telemetry)
timing_log = [120, 85, 60, 45, 30, 15]
sensor_data = [23, 45, 67, 89, 101, 98, 76, 54, 32]
event_stream = ['start', 'spike', 'tick', 'spike', 'reset', 'spike', 'update']
config_params = [10, 20, 30, 40, 50, 60, 70]

# Unused transformations (distractors)
encoded_config = [(c >> 2) ^ 15 for c in config_params]
hashed_events = [hash(e) % 100 for e in event_stream]

# Simulated fault flags based on partial analysis
preliminary_flags = []
for val in sensor_data:
    if val > 90:
        preliminary_flags.append(2)  # severe
    elif val > 70:
        preliminary_flags.append(1)  # mild
    else:
        preliminary_flags.append(0)

# Dead function call (no side effects)
fault_engine = FaultClassifier()
ignored_diagnostics = fault_engine.classify(sum(preliminary_flags))

# Real but obscured control flow
health_factor, critical_status, spike_count = evaluate_system_health(
    config_params, timing_log, event_stream
)

# Secondary irrelevant analysis
signature_code = generate_timing_signature(timing_log)
entropy_value = calculate_entropy([len(str(h)) for h in hashed_events])

# Now compute fault flags more directly for final use
recent_faults = [i for i, t in enumerate(timing_log) if t < 25]
fault_intensity = sum(preliminary_flags[i] for i in recent_faults if i < len(preliminary_flags))
fault_flags = set()
if critical_status:
    fault_flags.add('SYS_CRITICAL')
if fault_intensity > 2:
    fault_flags.add('HIGH_INTENSITY')
if spike_count >= 3:
    fault_flags.add('RECURRING_SPIKE')

# Final aggregation — KEY STATEMENT
final_diagnostic = aggregate_metrics(timing_log, fault_flags)

# Implementation of aggregate_metrics (buried to increase trace difficulty)
def aggregate_metrics(times, flags):
    base = sum(t // 10 for t in times)
    multiplier = 1
    if 'SYS_CRITICAL' in flags:
        multiplier *= 2
    if 'HIGH_INTENSITY' in flags:
        multiplier *= -3
    if 'RECURRING_SPIKE' in flags:
        multiplier *= 2
    # Only this line produces the real answer
    result = base * multiplier
    print(f"Result: {result}")
    return result

# Force execution order
if __name__ == "__main__":
    final_diagnostic = aggregate_metrics(timing_log, fault_flags)