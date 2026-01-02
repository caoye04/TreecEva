import math

# Simulated sensor data processing with diagnostic analysis
raw_samples = [127, 255, 98, 64, 201, 188, 73]
threshold = 100
calibration_factor = 0.87
offset = 12

# Irrelevant backup configuration (dead code path)
def legacy_calibrate(x):
    return x * 0.76 + 5  # Unused function - red herring

# Misleading intermediate transformation (distractor)
temp_adjusted = [round((v - offset) * 1.05) for v in raw_samples]
spurious_metric = sum(temp_adjusted) // len(temp_adjusted)

# Actual signal filtering logic
filtered_signals = []
for val in raw_samples:
    if val > threshold:
        filtered_signals.append(val * calibration_factor)
    else:
        filtered_signals.append(val * 0.5)

# Simulated timestamp alignment (partially relevant but complexified)
timestamps = [1690000000 + i*30 for i in range(len(raw_samples))]
nominal_times = [t for t in timestamps if t % 100 != 0]  # Filter rule not used later

# Data envelope calculation (relevant)
envelope_max = max(filtered_signals)
envelope_min = min(filtered_signals)
envelope_diff = envelope_max - envelope_min

# Bit manipulation for checksum (relevant concept but partially obfuscated)
checksum = 0
for sig in filtered_signals:
    truncated = int(sig)
    checksum ^= (truncated & 0xFF)  # XOR folding byte by byte
    checksum = (checksum << 1) | (checksum >> 7)  # Rotate left by 1
    checksum &= 0xFF  # Keep within byte range

# Auxiliary statistical distraction (irrelevant)
mean_raw = sum(raw_samples) / len(raw_samples)
variance_proxy = sum((x - mean_raw) ** 2 for x in raw_samples) / len(raw_samples)
skew_warning = variance_proxy > 2000  # Never used

# Log compression via string encoding (distractor with string methods)
compressed_log = ''.join([chr(65 + (int(sig) % 26)) for sig in filtered_signals if sig > 70])
reversed_chunks = [compressed_log[i:i+2][::-1] for i in range(0, len(compressed_log), 2)]
scrambled_tag = ''.join(reversed_chunks).lower()  # Looks important but unused

# Real processing: transform and analyze
processed_logs = []
for idx, sig in enumerate(filtered_signals):
    entry = {
        'id': f"LOG{idx+1:02}",
        'value': sig,
        'flagged': sig > 150,
        'rank': int(math.log(sig + 1) * 10) if sig > 0 else 0
    }
    processed_logs.append(entry)

# Secondary distraction: sorting that isn't used
sorted_by_value = sorted(processed_logs, key=lambda x: x['value'], reverse=True)
sorted_by_rank = sorted(processed_logs, key=lambda x: x['rank'])  # Dead end

# Core diagnostic algorithm
ranking_scores = [log['rank'] for log in processed_logs if log['flagged']]
aggregate_score = sum(ranking_scores)
penalty = len([x for x in processed_logs if x['value'] < 50]) * 10
adjusted_score = aggregate_score - penalty

# Final diagnostic computation (key point)
def analyze_readings(logs):
    total_risk = 0
    for log in logs:
        if log['flagged']:
            total_risk += log['rank'] * 1.5
        if log['value'] > 200:
            total_risk += 5
    # Additional adjustment based on checksum (subtle but real dependency)
    global checksum
    if checksum > 128:
        total_risk *= 1.1
    return int(total_risk)

final_diagnostic = analyze_readings(processed_logs)

# Output requirement
print(f"Target result: {final_diagnostic}")