from collections import Counter, defaultdict
import itertools
import math

def process_log_entry(entry):
    # Process log entry to extract signal strength and noise
    components = entry.split(':')
    if len(components) < 2:
        return None, None
    
    signal_str = components[0].strip()
    noise_level = 0
    
    try:
        # Extract signal strength value
        signal = int(signal_str) if signal_str.isdigit() else len(signal_str)
        
        # Calculate noise from remaining parts
        for part in components[1:]:
            if part.strip().isdigit():
                noise_level += int(part.strip())
            else:
                noise_level += sum(ord(c) % 7 for c in part if c.isalnum())
        
        return signal, noise_level
    except ValueError:
        return None, None

def calculate_interference(signals, noise_levels):
    # This calculates interference patterns (not relevant to final answer)
    interference = 0
    for s, n in zip(signals, noise_levels):
        if s > n * 2:
            interference += s - n
        else:
            interference -= n // 2
    return interference

def analyze_frequency_distribution(data):
    # Analyze frequency distribution (distraction)
    frequencies = Counter(data)
    dominant = frequencies.most_common(1)[0][0] if frequencies else 0
    variance = sum((x - dominant) ** 2 for x in data) / len(data) if data else 0
    return dominant, variance

def calculate_priority_factor(data_points):
    # The actual calculation that determines the answer
    if not data_points:
        return 0.0
    
    # Extract valid signals and noise levels
    valid_signals = [s for s, n in data_points if s is not None and n is not None]
    valid_noise = [n for s, n in data_points if s is not None and n is not None]
    
    # Calculate signal-to-noise ratio
    signal_strength = sum(valid_signals)
    noise_level = sum(valid_noise)
    
    # Prevent division by zero
    if noise_level == 0:
        return float(signal_strength) if signal_strength > 0 else 0.0
    
    # Calculate the ratio with precision adjustment
    raw_ratio = signal_strength / noise_level
    adjusted_ratio = math.floor(raw_ratio * 100) / 100.0
    
    return adjusted_ratio

# Main processing logic
log_entries = [
    "75: network traffic: high",
    "30: system load: medium: 45",
    "invalid entry",
    "90: memory usage: critical: 80: urgent",
    "60: cpu: normal: 25"
]

# Process all log entries
processed_data = []
filtered_signals = []
all_noise_values = []

for entry in log_entries:
    signal, noise = process_log_entry(entry)
    if signal is not None and noise is not None:
        processed_data.append((signal, noise))
        filtered_signals.append(signal)
        all_noise_values.append(noise)

# Calculate various metrics (mostly distractions)
signal_groups = defaultdict(list)
for s, n in processed_data:
    signal_groups[s // 10].append(n)

# Generate some potential thresholds (distraction)
thresholds = list(itertools.accumulate(range(1, 6)))
valid_thresholds = [t for t in thresholds if t % 2 == 0]

# More distraction calculations
dominant_signal, signal_variance = analyze_frequency_distribution(filtered_signals)
interference_level = calculate_interference(filtered_signals, all_noise_values)

# Calculate signal-to-noise ratios for different groupings (distraction)
group_ratios = {}
for group, values in signal_groups.items():
    if values:
        group_ratios[group] = group / sum(values) if sum(values) > 0 else 0

# This is the key calculation
priority_ratio = calculate_priority_factor(processed_data)

# Apply some irrelevant transformations (distraction)
modified_ratio = priority_ratio * (1 + interference_level / 1000)
adjusted_threshold = sum(valid_thresholds) / len(valid_thresholds) if valid_thresholds else 0

# More distractions
if dominant_signal > adjusted_threshold:
    weighted_factor = dominant_signal / adjusted_threshold
else:
    weighted_factor = adjusted_threshold / (dominant_signal if dominant_signal else 1)

# Final irrelevant calculation (distraction)
final_metric = modified_ratio * weighted_factor

print(f"Interference level: {interference_level}")
print(f"Signal variance: {signal_variance:.2f}")
print(f"Adjusted threshold: {adjusted_threshold}")
print(f"Priority ratio: {priority_ratio}")
print(f"Final metric: {final_metric:.4f}")