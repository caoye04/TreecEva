from itertools import permutations
from contextlib import contextmanager

def step_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

@contextmanager
def secure_state(data_key):
    state = {'active': True, 'key': data_key}
    try:
        yield state
    finally:
        state['active'] = False

def encode_permutations(perm_list, base_map):
    encoded_values = []
    for perm in perm_list:
        value = 0
        for i, char in enumerate(perm):
            value += base_map[char] * (len(base_map) ** i)
        encoded_values.append(value)
    return encoded_values

packet_ids = ['A', 'T', 'G']
base_encoding = {'A': 1, 'T': 2, 'G': 3, 'C': 4}

with secure_state('experiment_01') as state:
    if state['active']:
        @step_tracker
        def get_perms(elements):
            return list(permutations(elements))
        
        @step_tracker
        def process_encoding(perm_data, encoding_map):
            return encode_permutations(perm_data, encoding_map)
        
        raw_perms = get_perms(packet_ids)
        encoded_vals = process_encoding(raw_perms, base_encoding)
        final_checksum = sum(encoded_vals) % 1000
    else:
        final_checksum = -1

print(f"Result: {final_checksum}")