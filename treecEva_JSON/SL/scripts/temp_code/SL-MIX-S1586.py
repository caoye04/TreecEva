import heapq
from collections import defaultdict

def state_tracer(func):
    def wrapper(*args, **kwargs):
        packet_id, current_state, flag = args
        next_state = func(*args, **kwargs)
        if not hasattr(wrapper, 'transitions'):
            wrapper.transitions = defaultdict(list)
        wrapper.transitions[packet_id].append((current_state, next_state))
        return next_state
    return wrapper

@state_tracer
def compute_next_state(packet_id, current_state, flag):
    state_machine = {
        0: lambda f: 1 if f & 1 else 2,
        1: lambda f: 3 if f & 2 else 0,
        2: lambda f: 1 if f & 4 else 3,
        3: lambda f: 0 if f & 8 else 2
    }
    return state_machine[current_state](flag)

# Packet stream: (packet_id, initial_flag)
packets = [(1, 0b1101), (2, 0b1010), (3, 0b0110), (4, 0b1001)]
active_packets = []

for pid, flag in packets:
    heapq.heappush(active_packets, (flag, pid, 0))  # (priority, id, state)

cycle_counter = 0
max_steps = 20
step = 0

while active_packets and step < max_steps:
    flag, pid, state = heapq.heappop(active_packets)
    next_state = compute_next_state(pid, state, flag)
    if next_state == 0 and state != 0:
        cycle_counter += 1
    if next_state != 0:
        heapq.heappush(active_packets, (flag ^ (1 << (step % 4)), pid, next_state))
    step += 1

print(f"Result: {cycle_counter}")