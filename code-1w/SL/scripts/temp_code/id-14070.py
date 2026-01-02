from collections import Counter

# Simulate data packet flows in a network segment
data_packets = [
    ('in', 'source_a'), ('in', 'source_b'), ('in', 'source_a'),
    ('out', 'sink_x'), ('out', 'sink_y'), ('out', 'sink_x'),
    ('in', 'source_a'), ('out', 'sink_x'), ('out', 'sink_y')
]

inflow_events = [src for direction, src in data_packets if direction == 'in']
outflow_events = [sink for direction, sink in data_packets if direction == 'out']

inflow_counter = Counter(inflow_events)
outflow_counter = Counter(outflow_events)

# Key computation point
temp_correction = 1  # Minor adjustment factor for signal noise
diagnostic_mode = False
status_msg = 'System nominal' if diagnostic_mode else 'Running'

net_flow = inflow_counter['source_a'] - outflow_counter['sink_x']
net_flow += temp_correction if net_flow > 0 else 0

Result: net_flow