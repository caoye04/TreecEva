from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (irrelevant for final result)
sensor_fragments = ['ax7', 'bt3', 'cq9', 'dm2', 'ep8']
raw_checksum = sum(ord(f[0]) * int(f[-1]) for f in sensor_fragments)

# Misleading preprocessing chain
temporal_weights = [math.sin(i * 0.5) for i in range(6)]
weighted_sum = sum(temporal_weights)
normalized_score = raw_checksum * (weighted_sum / 6) if weighted_sum != 0 else 0

# System load profile with red herring transformations
system_load = [18, 22, 19, 25, 30, 28, 24, 20, 17, 23]
expanded_load = system_load[:5] + [x * 2 for x in system_load[5:]]  # unused extension
load_stats = {
    'mean': sum(system_load) / len(system_load),
    'peak': max(system_load),
    'variance': sum((x - sum(system_load)/len(system_load))**2 for x in system_load) / len(system_load)
}

# Health signature with multiple decoy operations
health_signature = [
    (3, 'critical'), (7, 'normal'), (1, 'warning'),
    (9, 'normal'), (5, 'critical'), (2, 'warning')
]

# Irrelevant sorting and grouping
classification_count = defaultdict(int)
for val, cls in health_signature:
    classification_count[cls] += 1
sorted_classes = sorted(classification_count.items(), key=lambda x: x[1], reverse=True)

# Hidden signal extraction via slicing and bit manipulation
signal_peaks = [v for v, c in health_signature if c == 'critical']
masked_signal = signal_peaks[0] ^ 15  # XOR obfuscation
shifted_mask = masked_signal << 2

# Decoy statistical analysis
entropy_proxy = 0.0
for v in signal_peaks:
    if v > 0:
        entropy_proxy -= (v / sum(signal_peaks)) * math.log(v / sum(signal_peaks))

# Core logic buried under distractions
def extract_pattern(seq):
    """Extract hidden pattern using slice and modular arithmetic"""
    segment = seq[1:-1]  # slice excluding first and last
    total = 0
    for i, x in enumerate(segment):
        total += x * ((i + 1) % 4)  # position-weighted sum
    return total

# Unused recursive distraction
def forecast_stress(levels, depth=3):
    if depth <= 0 or not levels:
        return [0]
    smoothed = [(levels[i-1] + levels[i] + levels[i+1])//3 
                for i in range(1, len(levels)-1)]
    return forecast_stress(smoothed, depth-1)

# Another decoy function with complex but irrelevant logic
def calculate_resilience_index(data):
    counts = Counter([x % 3 for x in data])
    return sum(counts.values()) / (1 + abs(counts[0] - counts[2]))

# Main processing buried in noise
def process_metrics(metrics, load):
    # Extract critical values from metrics
    critical_vals = [v for v, c in metrics if c == 'critical']
    
    # Real computation path starts here (obscured)
    base = critical_vals[0] * 100
    
    # Use slice to get mid-range load values
    mid_load = load[3:7]  # relevant slice
    adjustment = sum(mid_load) % 19  # modular arithmetic
    
    # Combine with bit manipulation on hidden signal
    signal_component = shifted_mask & 63  # bitmask to extract lower bits
    
    # Final calculation
    result = base + adjustment + (signal_component >> 1)
    
    # Dead code branch (never executed due to logic)
    if len(metrics) < 0:  # impossible condition
        result *= 0.5
        
    return result

# Spurious intermediate variables
diagnostic_trace = extract_pattern(system_load)
resilience = calculate_resilience_index(system_load)
forecast = forecast_stress(system_load)

# Key execution point
final_diagnostic = process_metrics(health_signature, system_load)

# Output the target result
print(f"Target result: {final_diagnostic}")