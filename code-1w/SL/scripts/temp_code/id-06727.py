def preprocess(data, limit):
    temp = []
    for x in data:
        if x > limit:
            temp.append(x * 0.9)
    return temp

# Irrelevant transformation chain
buffer_cache = [i**2 for i in range(15) if i % 3 != 0]
decay_factor = 0.95
adjusted_weights = {i: decay_factor ** i for i in range(10)}

# Unused but misleading diagnostic function
def legacy_diagnose(seq):
    total = 0
    for val in seq:
        total += abs(val) // 2
    return total // 3

# Distractor: complex but unused filter
class SignalFilter:
    def __init__(self, alpha=0.8):
        self.alpha = alpha
        self.state = 0
    
    def update(self, x):
        self.state = self.alpha * self.state + (1 - self.alpha) * x
        return self.state

# Real processing path begins
status_flags = [False, True, False]
sample_offset = 17

primary_samples = [i * 1.5 for i in range(20)]
secondary_samples = [abs((i - 10) ** 1.5) for i in range(20)]

# Key signal data
samples = [primary_samples[i] - secondary_samples[i] for i in range(20)]

threshold = sum([x for x in samples if x > 0]) / len(samples)

# Misleading normalization step
normalized = [x / (max(samples) + 1e-8) for x in samples]

# Another red herring: entropy-like calculation
entropy_proxy = 0.0
for x in normalized:
    if x > 0:
        entropy_proxy -= x * (x).log()  # This would fail without math import — intentionally misleading!

import math  # Now imported only when needed

# Actual analysis logic
running_avg = 0
alpha = 0.7
smoothed = []
for s in samples:
    running_avg = alpha * running_avg + (1 - alpha) * s
    smoothed.append(running_avg)

# Extract features from smoothed signal
peaks = []
for i in range(1, len(smoothed)-1):
    if smoothed[i] > smoothed[i-1] and smoothed[i] > smoothed[i+1]:
        peaks.append(smoothed[i])

# Slice to only last 8 peaks (some may not be real)
valid_peaks = peaks[-8:] if len(peaks) > 8 else peaks[:]

# Compute peak variance as stability metric
if valid_peaks:
    mean_peak = sum(valid_peaks) / len(valid_peaks)
    variance = sum((p - mean_peak)**2 for p in valid_peaks) / len(valid_peaks)
else:
    variance = 0

# Character counting distraction (unused)
diagnostic_tag = "SIGMON_V3"
char_count = len(diagnostic_tag)

# Sorting distraction
sorted_indices = sorted(range(len(samples)), key=lambda i: samples[i], reverse=True)
top_values = [samples[i] for i in sorted_indices[:5]]

# Critical decision logic
variance_threshold = 4.5
signal_strength = sum(abs(s) for s in samples) / len(samples)

flag_state = any(status_flags)

# Final diagnostic depends only on variance and threshold comparison
if variance < variance_threshold and signal_strength > threshold:
    final_diagnostic = int(mean_peak * 100) + sample_offset
else:
    final_diagnostic = int(variance * 50) - 100

# Additional decoy assignment that does nothing
final_diagnostic = final_diagnostic + 0  # No-op to mislead static analysis

# Print result as required
print(f"Target result: {final_diagnostic}")