from collections import defaultdict
import math

class SignalNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def build_signal_chain(values):
    if not values:
        return None
    head = SignalNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SignalNode(val)
        current = current.next
    return head

def calculate_variance(node_head, mean_val):
    count = 0
    sum_squared_diff = 0
    current = node_head
    while current:
        sum_squared_diff += (current.value - mean_val) ** 2
        count += 1
        current = current.next
    return sum_squared_diff / count if count > 0 else 0

def process_signals():
    # Stage mapping with signal data
    stage_signals = defaultdict(list)
    stage_signals['preprocessing'] = [12, 15, 18, 20]
    stage_signals['filtering'] = [8, 10, 14]
    stage_signals['enhancement'] = [22, 25, 27, 30, 32]
    
    # Build linked lists for each stage
    signal_chains = {stage: build_signal_chain(values) for stage, values in stage_signals.items()}
    
    # Compute means using lambda
    mean_computer = lambda node: sum(n.value for n in iter(lambda: node.__class__ if node else None, None)) or (lambda n: (lambda vals: sum(vals)/len(vals))([n.value for n in iter(lambda: n.__class__ if n else None, None)]))
    
    # Manual mean computation for clarity
    stage_means = {}
    for stage, chain in signal_chains.items():
        values = []
        current = chain
        while current:
            values.append(current.value)
            current = current.next
        stage_means[stage] = sum(values) / len(values)
    
    # Merge with additional data
    additional_stats = {'preprocessing': 16, 'filtering': 12, 'compression': 9}
    merged_data = {**stage_means, **additional_stats}
    
    # Apply transformation
    transformed = {k: v * 2 if v > 15 else v + 5 for k, v in merged_data.items()}
    
    # Aggregate calculation
    aggregate_mean = sum(transformed.values()) / len(transformed)
    
    return aggregate_mean

# Execute processing
aggregate_mean = process_signals()
print(f"Result: {aggregate_mean}")