import math

def analyze_phase_shift(signal, threshold=0.7):
    """Irrelevant function: analyzes signal phase (dead code path)"""
    wrapped = signal[-1:] + signal[:-1]
    shifted = [abs(wrapped[i] - signal[i]) for i in range(len(signal))]
    return sum(s > threshold for s in shifted)


def generate_checksum(data):
    """Decoy function: computes XOR checksum (not used in main logic)"""
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item % 256
    return checksum

# Simulated network performance metrics over time
network_metrics = [
    [1.2, 0.8, 3.4, 2.1, 4.5],  # Latency spikes
    [0.9, 1.1, 1.0, 0.8, 1.2],  # Jitter
    [98.7, 99.2, 97.8, 99.5, 98.3],  # Uptime %
    [440, 520, 480, 500, 460],    # Bandwidth (Mbps)
    [3, 5, 2, 6, 4]               # Packet loss count
]

# Irrelevant transformation: reversed slices with no impact
shadow_transform = [row[::-1] for row in network_metrics[::2]]

# Weight matrix for aggregation (only first 3 rows actually used)
weights = [
    [0.3, 0.4, 0.3],      # Latency importance
    [0.2, 0.2, 0.6],      # Jitter sensitivity
    [0.1, 0.1, 0.8],      # Uptime criticality
    [0.5, 0.3, 0.2],      # Bandwidth (unused)
    [0.4, 0.4, 0.2]       # Packet loss (unused)
]

# Misleading intermediate: average across all metrics (distractor)
total_avg = sum(sum(row) / len(row) for row in network_metrics) / len(network_metrics)

# Critical data extraction: focus on uptime, latency, and packet loss only
extracted = {
    'latency': network_metrics[0][1:4],        # Relevant slice: recent spikes
    'uptime': network_metrics[2][:],           # Full uptime series
    'packets': network_metrics[4][:-1]         # Exclude last measurement
}

# Compute rolling 3-point moving averages for stability assessment
smoothed = {}
for key, data in extracted.items():
    smoothed[key] = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)] if len(data) >= 3 else [sum(data)/len(data)]

# Calculate volatility using variance (distraction: not directly used)
volatility = {}
for key, data in extracted.items():
    mean_val = sum(data) / len(data)
    volatility[key] = sum((x - mean_val)**2 for x in data) / len(data)

# Focus on latest smoothed values for decision
latest_smooth = {k: v[-1] for k, v in smoothed.items() if v}

# Normalize values to 0-1 scale based on assumed thresholds
norm = {
    'latency': min(1.0, latest_smooth['latency'] / 4.0),
    'uptime': max(0.0, (latest_smooth['uptime'] - 95.0) / 5.0),  # Only above 95% counts
    'packets': 1 - min(1.0, latest_smooth['packets'] / 5.0)
}

# Apply weighted aggregation using only first three weight vectors
partial_results = []
for i, metric in enumerate(['latency', 'uptime', 'packets']):
    w = weights[i]
    # Composite score: geometric mean of norm and inverse volatility (fake complexity)
    fake_volatility_influence = math.sqrt(norm[metric] * (1 / (1 + volatility.get(metric, 1))))
    partial_results.append(
        w[0] * norm[metric] + 
        w[1] * fake_volatility_influence + 
        w[2] * (norm[metric] ** 0.5)
    )

# Final aggregation uses only the first three components
final_score = sum(partial_results[i] * [0.4, 0.4, 0.2][i] for i in range(3))

# Red herring: modify final_score with unused checksum (but doesn't override)
generate_checksum(network_metrics)

# Actual result output
Result: {final_score}