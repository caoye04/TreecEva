from collections import defaultdict

# Simulate hourly network traffic analysis across multiple servers
server_logs = [
    'server_a: 85,92,78,96,105,110,98',
    'server_b: 65,70,80,88,95,100,97',
    'server_c: 90,87,95,102,108,115,120',
    'server_d: 70,75,85,90,92,94,90'
]

# Parsing and processing log data
traffic_data = defaultdict(list)
for log in server_logs:
    name, readings = log.split(': ')
    server_id = name.strip()
    values = list(map(int, readings.split(',')))
    smoothed = [round((values[i] + values[i-1]) / 2) for i in range(len(values)) if i > 0]
    traffic_data[server_id] = [v for v in values if v > 80] + [sum(smoothed[:3]) // len(smoothed[:3])]  # Mix raw and processed

# Aggregate all high-usage values per server
aggregated_load = {}
for srv, loads in traffic_data.items():
    base_load = sum(loads)
    adjustment_factor = len(loads) % 7
    adjusted_load = base_load + adjustment_factor
n    aggregated_load[srv] = adjusted_load

# Secondary computation: analyze pattern density
pattern_density = {}
for k, v in aggregated_load.items():
    bin_rep = bin(v)[2:]
    density = bin_rep.count('1') / len(bin_rep)
    pattern_density[k] = round(density, 3)

# Compile trend sequence from highest individual reading per server
usage_trends = []
fake_shift = lambda x: (x << 1) & 0xFF  # Unused transformation (distractor)
for s in ['server_a', 'server_b', 'server_c', 'server_d']:
    raw_line = next(l for l in server_logs if s in l)
    nums = list(map(int, raw_line.split(': ')[1].split(',')))
    peak = max(nums)
    offset = peak % 10
    shifted_peak = peak + offset if peak < 100 else peak - offset
    usage_trends.append(shifted_peak)

# Introduce irrelevant statistical calculation (distractor)
correction_map = {i: (i ** 0.5) * 1.5 for i in range(1, 10)}
scaling_factor = sum(correction_map.values()) / 100  # Not used later

# Key computational step
peak_capacity = max(usage_trends)

# Print final result as required
print(f"Result: {peak_capacity}")