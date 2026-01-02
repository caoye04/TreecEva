def calculate_efficiency(data):
    base = data['input']
    losses = sum(data['losses'])
    efficiency = (base - losses) / base
    adjust = lambda x: x * 1.1 if x < 0.8 else x * 0.95
    return int(adjust(efficiency) * 100)

metrics = {
    'input': 500,
    'losses': [50, 30, 20, 10],
    'timestamp': 1712345678
}

energy_output = calculate_efficiency(metrics)
print(f"Target result: {energy_output}")