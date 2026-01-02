from collections import Counter

def calculate_net_flow(inputs, outputs):
    input_counter = Counter(inputs)
    output_counter = Counter(outputs)
    total_in = sum(input_counter.values())
    total_out = sum(output_counter.values())
    excess_sources = [k for k, v in input_counter.items() if v > 1]
    obsolete_sinks = [k for k, v in output_counter.items() if v > 1]
    net_flow = total_in - total_out
    if net_flow > 0 and len(excess_sources) > 0:
        net_flow -= len(excess_sources)
    return net_flow

inflows = ['source_a', 'source_b', 'source_a', 'source_c']
outflows = ['sink_x', 'sink_y']

net_flow = calculate_net_flow(inflows, outflows)
print(f'Result: {net_flow}')