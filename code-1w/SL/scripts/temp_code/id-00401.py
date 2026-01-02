from collections import defaultdict, Counter

# Simulate a network packet processing system with state transitions
def analyze_traffic(patterns):
    freq = Counter()
    for p in patterns:
        freq[p] += 1
    return freq.get('SYN', 0)

# Irrelevant helper: counts vowels in string representations of ports (distractor)
def count_vowels_in_ports(ports):
    vowels = 'aeiou'
    total = 0
    for port in ports:
        s = str(port)
        for c in s:
            if c in vowels:
                total += 1
    return total

# State transition rules for firewall logic
def update_state(current, event):
    mapping = {
        ('IDLE', 'SYN'): 'SYN_RECEIVED',
        ('SYN_RECEIVED', 'ACK'): 'ESTABLISHED',
        ('ESTABLISHED', 'FIN'): 'CLOSE_WAIT',
        ('CLOSE_WAIT', 'ACK'): 'IDLE'
    }
    return mapping.get((current, event), current)

# Misleading function that computes checksum but is unused
def compute_checksum(data):
    chk = 0
    for d in data:
        chk ^= hash(str(d)) % 256
    return chk

# Core logic: process event sequence and track state transitions
def process_state(transitions, log):
    state_counter = defaultdict(int)
    current_state = 'IDLE'
    history = []
    
    # Real work: follow transitions based on events
    for event in log:
        prev = current_state
        current_state = update_state(current_state, event)
        state_counter[current_state] += 1
        if prev != current_state:
            history.append((prev, current_state))
    
    # Distractor computation: slice manipulation with no impact
    snapshot = history[1::2]  # every other transition
    summary = ''.join([h[1][0] for h in snapshot if len(h[1]) > 0])
    mask_value = len(summary) << 2
    
    # Unused recursive path (dead code)
    def traverse_path(path, idx):
        if idx >= len(path):
            return 0
        return len(path[idx]) + traverse_path(path, idx + 1)
    
    # Another red herring: tuple unpacking with dummy values
    metadata = (len(log), len(set(log)), mask_value)
    packet_size, unique_events, shift_key = metadata
    
    # Actual answer derivation
    cycle_count = 0
    for i in range(len(history)):
        if history[i] == ('IDLE', 'SYN_RECEIVED'):
            # Look ahead for full handshake completion
            for j in range(i+1, len(history)):
                if history[j] == ('ESTABLISHED', 'CLOSE_WAIT'):
                    cycle_count += 1
                    break

    base_score = state_counter['ESTABLISHED'] * 17
    penalty = state_counter['CLOSE_WAIT'] * 3
    final_output = base_score - penalty + cycle_count
    
    # Print required result
    print(f"Result: {final_output}")
    return final_output

# Setup inputs
port_list = [80, 443, 22, 21, 25, 53, 110]
vowel_noise = count_vowels_in_ports(port_list)

traffic_patterns = ['SYN', 'DATA', 'ACK', 'SYN', 'ACK', 'FIN', 'RST']
syn_count = analyze_traffic(traffic_patterns)

transitions_map = {
    'IDLE': {'SYN': 'SYN_RECEIVED'},
    'SYN_RECEIVED': {'ACK': 'ESTABLISHED'},
    'ESTABLISHED': {'FIN': 'CLOSE_WAIT'},
    'CLOSE_WAIT': {'ACK': 'IDLE'}
}

event_stream = ['SYN', 'ACK', 'FIN', 'ACK', 'SYN', 'ACK']

# Trigger point
final_output = process_state(transitions_map, event_stream)