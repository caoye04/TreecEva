from collections import Counter

def calculate_network_load(packets, limit):
    size_count = Counter(packets)
    total_load = 0
    for size, count in size_count.items():        
        if size < 50:
            contribution = size * count * 0.1
        elif size < 100:
            contribution = size * count * 0.25
        else:
            contribution = size * count * 0.5
        total_load += contribution
        if total_load > limit:
            total_load *= 0.9
            break
    return int(total_load)

# Simulate network packet sizes in bytes
packet_sizes = [30, 30, 60, 60, 60, 120, 120]
threshold = 200
total_load = calculate_network_load(packet_sizes, threshold)
print(f"Result: {total_load}")