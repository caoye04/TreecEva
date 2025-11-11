from functools import reduce

def transform_modifier(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2 if result > 0 else result // 2
    return wrapper

@transform_modifier
def signal_filter(value, threshold=10):
    if value > threshold:
        return value - threshold
    else:
        return threshold - value

def process_packets(packet_sequence):
    impact_log = {}
    for idx, packet in enumerate(packet_sequence):
        filtered = signal_filter(packet)
        impact_log[idx] = filtered
        if idx > 0:
            impact_log[idx] += impact_log[idx-1]
    return impact_log

packets = [15, 7, 22, 3, 18]
processed_log = process_packets(packets)
cumulative_impact = reduce(lambda a, b: a + b, processed_log.values())

print(f"Result: {cumulative_impact}")