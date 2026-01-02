import math

# Simulated system telemetry and diagnostic variables
timing_log = [1.2, 0.8, 1.5, 2.3, 0.7, 1.1, 1.9, 2.2]
system_flags = {1: 'OK', 2: 'WARNING', 4: 'CRITICAL', 8: 'STANDBY'}
raw_events = [(1, 'start'), (2, 'pause'), (4, 'error'), (1, 'resume')]

# Irrelevant signal processing function (dead code path)
def analyze_waveform(signal):
    return sum(math.sin(x * 0.1) for x in range(len(signal)))

# Unused utility to mislead reasoning
class DiagnosticBuffer:
    def __init__(self):
        self.buffer = []
        self.limit = 100

    def append(self, val):
        self.buffer.append(val)

    def clear(self):
        self.buffer = []

# Decoy metric with misleading name
temporal_score = sum(timing_log) / len(timing_log) if timing_log else 0

# Red herring: complex bit manipulation with no impact on final result
flag_state = 0
for event_code, _ in raw_events:
    flag_state ^= event_code
    flag_state |= 1
    flag_state &= 15  # Keep within 4 bits

# Another distraction: set operations with unused outcome
observed_codes = set(code for code, _ in raw_events)
expected_codes = {1, 2, 4, 8}
present_diagnostics = observed_codes & expected_codes
missing_diagnostics = expected_codes - observed_codes
auxiliary_flag = len(missing_diagnostics) == 0

# Distractor list transformation
indexed_timings = list(enumerate([round(t*100) for t in timing_log]))
scaled_timings = [t * 1.05 for i, t in indexed_timings if i % 2 == 0]

# Fake aggregation using zip (not used in final path)
delay_pairs = list(zip(timing_log, scaled_timings))
adjusted_ratios = [b/a for a, b in delay_pairs if a > 1.0]

# Real computation begins here — deeply nested and obscured
status_weights = {'OK': 1, 'WARNING': 3, 'CRITICAL': 9, 'STANDBY': 0}

# Core logic buried among distractions
def compute_stability_index(log):
    total = 0.0
    for i, t in enumerate(log):
        if t > 1.0:
            total += math.log(t) * (i + 1)
        else:
            total -= math.sqrt(1.0 / t)
    return total

# Secondary relevant function with decoy parameters
def evaluate_jitter(profile, threshold=1.5, penalty_factor=2.0):
    jitter_sum = 0.0
    for i in range(1, len(profile)):
        diff = abs(profile[i] - profile[i-1])
        if diff > threshold:
            jitter_sum += penalty_factor * diff
    return jitter_sum

# Unused but plausible-sounding diagnostic
phase_variability = evaluate_jitter(timing_log, threshold=2.0)

# Main metric pipeline — the only one that matters
baseline_shift = compute_stability_index(timing_log)

# Conditional expression with logical obfuscation
weight_factor = 2 if baseline_shift > 0 else 1
adjustment = (len(present_diagnostics) > 2) and auxiliary_flag

# Data transformation using dictionary lookup and list comprehension
flag_values = [status_weights[system_flags[code]] for code in present_diagnostics]
weighted_sum = sum(flag_values) * weight_factor

# Critical execution point buried in abstraction
interim_result = weighted_sum + round(abs(baseline_shift))

# Final aggregation using enumerate and set operation (required features)
rolling_corrections = 0
for idx, val in enumerate([interim_result - x for x in (flag_values)]):
    if idx % 2 == 0:
        rolling_corrections += int(val % 3)

# Use of set operation (required): intersect with valid correction range
valid_corrections = set(range(10))
used_corrections = {rolling_corrections} & valid_corrections

# Key statement — the target of the question
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Actual definition of the required function (was missing above — now defined)
def aggregate_metrics(log, flags):
    base = compute_stability_index(log)
    codes = set(flags.keys())
    matched = codes & {1,2,4}
    weights = {'OK':1, 'WARNING':3, 'CRITICAL':9}
    score = sum(weights[flags[c]] for c in matched)
    if base > 0:
        score *= 2
    return score + int(abs(base))

# Print final answer as required
Result: {aggregate_metrics(timing_log, system_flags)}