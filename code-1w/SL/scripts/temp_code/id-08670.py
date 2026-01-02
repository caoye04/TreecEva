import itertools

# Simulated sensor data processing with embedded diagnostics
raw_readings = [0.88, -1.22, 3.14, -2.71, 0.0, 1.41, -1.73, 2.23]
offset_calibration = 0.5
smoothing_factor = 0.9

# Irrelevant statistical counters (distractors)
mean_counter = 0
deviation_sum = 0
peak_moments = []
compression_ratio = 2.5  # Unused parameter

# Data conditioning with red herring transformations
conditioned = []
for x in raw_readings:
    adjusted = abs(x + offset_calibration)
    if adjusted > 1.0:
        adjusted = smoothing_factor * adjusted
    conditioned.append(round(adjusted, 2))

# Spurious frequency analysis (dead path)
frequency_bins = [0] * 5
for val in conditioned:
    bin_idx = min(int(val), 4)
    frequency_bins[bin_idx] += 1

# Dummy transformation chain (decoy logic)
shifted_data = [v * 1.1 for v in conditioned if v > 0.5]
scaled_projection = list(itertools.accumulate(shifted_data, lambda a, b: a * 0.8 + b))
filtered_stream = [x for x in scaled_projection if x > 1.0]

# Real processing path begins here (obscured by prior noise)
effective_signals = [x for x in raw_readings if x != 0.0]
rectified = [abs(x) for x in effective_signals]
attenuated = [r * 0.75 for r in rectified]

# Key intermediate computation (masked by context)
integration_window = []
for i, val in enumerate(attenuated):
    if i % 2 == 0:
        integration_window.append(val ** 2)
    else:
        integration_window.append(val + 0.5)

# Conditional expression mix (required python feature)
status_flag = 'active' if sum(integration_window) > 10 else 'standby'
mode_weight = 1.25 if status_flag == 'active' else 0.75

# Core diagnostic calculation
weighted_diagnostic = 0
for j, w in enumerate(integration_window):
    if j < 4:  # Limited scope processing
        weighted_diagnostic += w * (j + 1) * mode_weight

# Secondary decoy system: entropy simulation
symbol_counts = {chr(65+i): int(w*10) for i, w in enumerate(rectified[:5])}
total_symbols = sum(symbol_counts.values())
entropy_score = 0
for count in symbol_counts.values():
    if count > 0:
        prob = count / total_symbols
        entropy_score -= prob * __import__('math').log2(prob)

# Tertiary distraction: unused recursive function
def forecast_decay(levels, depth=3):
    if depth == 0 or len(levels) == 0:
        return 0
    mid = len(levels) // 2
    return levels[mid] + forecast_decay(levels[:mid], depth-1)

# Final processing stage with correct logic flow
processed_data = [round(x, 2) for x in integration_window]

def analyze_signal(data):
    base = 0
    for k, val in enumerate(data):
        if k % 3 == 0:
            base += val * 2.5
        elif k % 3 == 1:
            base += val * 1.3
        else:
            base += val * 0.7
    # Final adjustment based on signal length parity
    correction = 1.1 if len(data) % 2 == 0 else 0.9
    return round(base * correction, 4)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output required result
print(f"Result: {final_diagnostic}")