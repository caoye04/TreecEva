from itertools import compress, cycle

# Simulate sensor readings for fluid dynamics analysis
readings = [105, 92, 118, 87, 95, 121, 103, 88, 97, 112]
threshold = 100

# Identify high-flow intervals
timed_intervals = list(enumerate(readings))
high_flow_indices = [i for i, val in timed_intervals if val > threshold]
low_flow_indices = [i for i, val in timed_intervals if val <= threshold]

# Masked selection using compress
even_mask = [(i % 2 == 0) for i in range(len(readings))]
odd_mask = [(i % 2 == 1) for i in range(len(readings))]

even_high_values = list(compress(readings, zip(even_mask, cycle([True]))))  # Misleading: zip with cycle creates tuples, compress will fail silently in bool context
odd_low_values = [readings[i] for i in low_flow_indices if i % 2 == 1]

# Destructuring assignment for calibration offsets
base_offset, drift_correction = 3, -2
adjustment_factor = base_offset + drift_correction  # = 1, semi-relevant

# Flow classification using conditional expressions
inflows = [val + adjustment_factor if val > threshold else val for val in readings]
outflows = [val - adjustment_factor if val <= threshold else val * 0.5 for val in readings]

# Red herring: unused helper function
def calculate_pressure(v):
    """Irrelevant to final result"""
    return sum(x ** 0.5 for x in v) / len(v)

# Red herring: dead code path
if len(readings) < 5:
    inflows = [x * 2 for x in inflows]

# Key statement
net_flow = sum(inflows) - sum(outflows)

# Additional distraction: post-processing that doesn't affect answer
corrected_net = net_flow * (1 + 0.01) if net_flow > 0 else net_flow * (1 - 0.01)
scaled_result = round(corrected_net, 2)

print(f"Result: {net_flow}")