from functools import reduce

class SensorEventNode:
    def __init__(self, timestamp, next_node=None):
        self.timestamp = timestamp
        self.next = next_node

def generate_fibonacci_sequence(n):
    seq = [1, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def compute_event_chain_delays(chain_head):
    delays = []
    current = chain_head
    while current and current.next:
        delays.append(current.next.timestamp - current.timestamp)
        current = current.next
    return delays

# Initialize sensor event chains
sensor_A_events = reduce(lambda head, ts: SensorEventNode(ts, head), reversed(generate_fibonacci_sequence(6)), None)
sensor_B_events = reduce(lambda head, ts: SensorEventNode(ts * 2, head), reversed(generate_fibonacci_sequence(5)), None)

# Process delays
chain_A_delays = compute_event_chain_delays(sensor_A_events)
chain_B_delays = compute_event_chain_delays(sensor_B_events)

# Merge and process
delay_map = {f'seq_{i}': delay for i, delay in enumerate(chain_A_delays + chain_B_delays)}
filtered_delays = {k: v for k, v in delay_map.items() if v > 1}

cumulative_delay = sum(filtered_delays.values())

print(f'Result: {cumulative_delay}')