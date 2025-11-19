from functools import reduce

document_segments = ['alpha', 'beta', 'gamma']
state_transitions = {'INITIAL': 'PROCESSING', 'PROCESSING': 'FINAL', 'FINAL': 'INITIAL'}
current_state = 'INITIAL'
hash_base = 31
hash_modulus = 1000000007
final_hash_accumulator = 0

segment_weights = {seg: len(seg) * 2 + 1 for seg in document_segments}
weighted_chars = [(c, segment_weights[seg]) for seg in document_segments for c in seg]

for char, weight in weighted_chars:
    if current_state == 'INITIAL':
        current_state = state_transitions[current_state]
        char_value = ord(char) - ord('a') + 1
        final_hash_accumulator = (final_hash_accumulator * hash_base + char_value * weight) % hash_modulus
    elif current_state == 'PROCESSING':
        current_state = state_transitions[current_state]
        char_value = ord(char) - ord('a') + 1
        final_hash_accumulator = (final_hash_accumulator + char_value * weight * hash_base) % hash_modulus
    else:  # FINAL state
        current_state = state_transitions[current_state]
        char_value = ord(char) - ord('a') + 1
        final_hash_accumulator = (final_hash_accumulator ^ (char_value * weight)) % hash_modulus

print(f"Result: {final_hash_accumulator}")