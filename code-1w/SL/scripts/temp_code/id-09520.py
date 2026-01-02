import math

# Network resource allocation simulation with interference

def calculate_latency(hops, congestion_factor):
    return hops * 1.8 + congestion_factor / 4.2

# Irrelevant helper function (dead code path)
def estimate_power_usage(voltage, current):
    return voltage * current * 0.85

# Core bandwidth adjustment logic
def adjust_bandwidth(base, surges):
    temp = base
    for surge in surges:
        if surge > 75:
            temp += temp * 0.1
        elif surge > 50:
            temp -= temp * 0.05
        else:
            temp = temp * 0.95  # Minor decay
    return int(temp)

# Signal integrity check (distractor - looks important but unused)
def verify_signal_strength(signal, threshold=30):
    if signal < threshold:
        return False
    return True if (signal ** 2) % 7 < 5 else False

# Unused data transformation (red herring)
raw_logs = [23, 84, 91, 15, 67]
processed_metrics = [math.ceil(x / 3) for x in raw_logs]
summary_score = sum(processed_metrics) // len(processed_metrics)

# Simulated system parameters (mix of relevant and irrelevant)
base_allocation = 120000
peak_load = 98765  # Distractor: looks like it should be used
traffic_surges = [45, 80, 60, 90, 30]
latency_hops = 5
congestion = 68

# Decoy assignment chain
shadow_copy = base_allocation
shadow_copy *= 1.05
shadow_copy = int(shadow_copy)
shadow_copy -= 1000  # Misleading modification

# Conditional expression (required language feature): determines test mode
is_stress_test = True
multiplier = 1.1 if is_stress_test else 0.9

# Apply multiplier but then override — adds confusion
base_allocation = int(base_allocation * multiplier)
base_allocation = 120000  # Reset to original (distractor)

# Critical statement
final_bandwidth = adjust_bandwidth(base_allocation, traffic_surges)

# Print result as required
print(f"Result: {final_bandwidth}")