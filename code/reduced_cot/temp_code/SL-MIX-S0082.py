channels = [
    {'id': 'CH_A', 'bandwidth': 120, 'latency': 15},
    {'id': 'CH_B', 'bandwidth': 90, 'latency': 10},
    {'id': 'CH_C', 'bandwidth': 200, 'latency': 25},
    {'id': 'CH_D', 'bandwidth': 150, 'latency': 20}
]

# Efficiency formula: bandwidth / latency
channel_efficiencies = {ch['id']: ch['bandwidth'] / ch['latency'] for ch in channels}

visited_channels = frozenset(['CH_B', 'CH_D'])
valid_channels = {k: v for k, v in channel_efficiencies.items() if k not in visited_channels}

max_efficiency = 0
for cid, eff in valid_channels.items():
    if eff > max_efficiency:
        max_efficiency = eff
    if max_efficiency > 8.0:
        break

print(f'Result: {max_efficiency}')