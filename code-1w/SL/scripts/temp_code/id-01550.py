def transform_entry(entry):
    # Irrelevant transformation
    temp_a = (entry['value'] ** 2) % 17
    temp_b = entry['value'] & 15
    shifted = (temp_a << 2) ^ temp_b
    return {**entry, 'transformed': shifted}


def filter_relevant(records):
    # Distractor: complex filtering with red herring condition
    threshold = sum(r['value'] for r in records) / len(records)
    decoy_result = [r for r in records if r['value'] > threshold * 0.7]
    # Actual relevant logic (less obvious)
    return [r for r in records if r['flag'] and r['value'] % 3 != 0]


def accumulate_metrics(items):
    metrics = {}
    running = 0
    for i, item in enumerate(items):
        running += item['value']
        if i % 2 == 0:
            running -= 1
        # Decoy metric collection
        metrics[f'step_{i}'] = running * (i + 1)
    # Real result stored obscurely
    metrics['final_accum'] = running
    return metrics


def extract_signals(data_slice):
    # Bit manipulation red herring
    signal_mask = 0b1101
    signals = []
    for x in data_slice:
        masked = x & signal_mask
        if masked in [1, 3, 5]:
            signals.append(masked)
    # Unused but plausible computation
    aggregate_signal = sum(signals) << 1
    # Actual needed result
    return len(signals)


def process_chunk(chunk):
    # Complex unpacking and slicing distractor
    mid_index = len(chunk) // 2
    left_half = chunk[:mid_index]
    right_half = chunk[mid_index:]
    
    # Multiple assignments with misleading names
    (a, b), (c, d) = (left_half[0], left_half[-1]), (right_half[0], right_half[-1])
    pivot = (b + c) // 2
    
    # List comprehension that seems important but isn't used in final path
    derived_values = [x * 2 + pivot for x in chunk if x < pivot]
    
    # Relevant operation buried here
    adjusted = [x - 1 for x in chunk if x % 4 == 0]
    return sum(adjusted)


def harvest_results(dataset):
    # Dictionary operations with multiple lookups
    lookup_table = {i: i * 3 + 2 for i in range(15)}
    
    # Slicing that appears critical
    window = dataset[2:10:2]
    
    # Logical operations mixed with decoys
    valid_flags = all(d['active'] for d in dataset if d['type'] == 'node')
    debug_info = [d['id'] for d in dataset if not d['active']]
    
    # Key actual calculation (non-obvious)
    base_score = sum(lookup_table.get(d['meta'], 0) for d in dataset)
    adjustment = extract_signals([process_chunk([d['value'] for d in dataset]) + 5])
    
    # Final computation chain
    intermediate = base_score - len(debug_info)
    final_yield = intermediate * 3 + adjustment
    return final_yield

# Main execution flow
raw_entries = [
    {'id': 0, 'value': 8, 'flag': True, 'meta': 4, 'type': 'node', 'active': True},
    {'id': 1, 'value': 12, 'flag': False, 'meta': 7, 'type': 'sensor', 'active': True},
    {'id': 2, 'value': 4, 'flag': True, 'meta': 10, 'type': 'node', 'active': False},
    {'id': 3, 'value': 16, 'flag': True, 'meta': 4, 'type': 'node', 'active': True},
    {'id': 4, 'value': 3, 'flag': False, 'meta': 13, 'type': 'sensor', 'active': True},
    {'id': 5, 'value': 20, 'flag': True, 'meta': 7, 'type': 'node', 'active': False},
    {'id': 6, 'value': 7, 'flag': True, 'meta': 10, 'type': 'sensor', 'active': True},
    {'id': 7, 'value': 9, 'flag': False, 'meta': 4, 'type': 'node', 'active': True}
]

# Irrelevant preprocessing chain
transformed_data = [transform_entry(e) for e in raw_entries]
filtered_data = filter_relevant(transformed_data)
collected_metrics = accumulate_metrics(filtered_data)

# Data restructuring that looks important
structured_chunks = [[e['value']] for e in raw_entries]
processed_data = [
    {**e, 'batch': process_chunk([e['value']])} for e in raw_entries
]

# Critical execution point
final_yield = harvest_results(processed_data)
print(f"Target result: {final_yield}")