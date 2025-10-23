from functools import reduce

class DelayNode:
    def __init__(self, delay, next_node=None):
        self.delay = delay
        self.next = next_node

def build_delay_chain(measurements):
    head = None
    for delay in reversed(measurements):
        head = DelayNode(delay, head)
    return head

class BatchProcessor:
    def __enter__(self):
        self.filtered_delays = []
        return self
    
    def add_filtered(self, values):
        self.filtered_delays.extend(values)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Initialize delay measurements for three network nodes
node_a_measurements = [120, 150, 90, 200, 110]
nodel_b_measurements = [140, 160, 80, 220, 130]
nodel_c_measurements = [100, 170, 70, 250, 95]

# Build linked lists for each node
chain_a = build_delay_chain(node_a_measurements)
chain_b = build_delay_chain(nodel_b_measurements)
chain_c = build_delay_chain(nodel_c_measurements)

# Process measurements with context manager
with BatchProcessor() as processor:
    all_chains = [chain_a, chain_b, chain_c]
    for chain in all_chains:
        current = chain
        delays = []
        while current:
            delays.append(current.delay)
            current = current.next
        # Filter out delays greater than 200 (anomalies)
        normal_delays = list(filter(lambda x: x <= 200, delays))
        processor.add_filtered(normal_delays)
    
    # Calculate average of filtered delays
    total_filtered = processor.filtered_delays
    avg_delay = reduce(lambda a, b: a + b, total_filtered) / len(total_filtered)
    
    # Count delays within 20% of average
    threshold = avg_delay * 0.2
    low_variation_count = len(list(filter(lambda x: abs(x - avg_delay) <= threshold, total_filtered)))
    
    # Reliability scoring logic
    has_good_average = avg_delay < 150
    has_low_variation = low_variation_count >= len(total_filtered) * 0.6
    sufficient_samples = len(total_filtered) >= 10
    
    reliability_score = 0
    if has_good_average and has_low_variation and sufficient_samples:
        reliability_score = 100
    elif (has_good_average or has_low_variation) and sufficient_samples:
        reliability_score = 75
    elif not has_good_average and not has_low_variation:
        reliability_score = 25
    else:
        reliability_score = 50

print(f"Result: {reliability_score}")