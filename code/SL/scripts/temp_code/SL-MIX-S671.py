import math
from collections import defaultdict

event_log = [127, 63, 31, 15, 7]
key_rotation = [lambda x: int(math.log2(x+1)) if x > 0 else 1,
               lambda x: int(math.log10(x+1)) if x > 0 else 1,
               lambda x: x >> 1]
state_transitions = {
    'IDLE': {'pattern_match': 'ALERT'},
    'ALERT': {'escalate': 'CRITICAL', 'resolve': 'IDLE'},
    'CRITICAL': {'acknowledge': 'IDLE'}
}
current_state = 'IDLE'
intrusion_score = 0
pattern_buffer = set()
threshold_map = defaultdict(lambda: 3)
threshold_map.update({'ALERT': 2, 'CRITICAL': 1})

for i, event_code in enumerate(event_log):
    decrypted_event = event_code ^ key_rotation[i % len(key_rotation)](event_code)
    pattern_buffer.add(decrypted_event)
    
    if current_state == 'IDLE' and len(pattern_buffer) >= threshold_map[current_state]:
        current_state = state_transitions[current_state]['pattern_match']
        intrusion_score += len(pattern_buffer) * 2
        pattern_buffer.clear()
    elif current_state == 'ALERT':
        if decrypted_event & 0b1111 == 0b1111:
            current_state = state_transitions[current_state]['escalate']
            intrusion_score <<= 1
        else:
            current_state = state_transitions[current_state]['resolve']
            intrusion_score -= len(pattern_buffer)
            pattern_buffer.clear()
    elif current_state == 'CRITICAL':
        if decrypted_event > 100:
            intrusion_score += decrypted_event
        current_state = state_transitions[current_state]['acknowledge']
        pattern_buffer.clear()

print(f"Result: {intrusion_score}")