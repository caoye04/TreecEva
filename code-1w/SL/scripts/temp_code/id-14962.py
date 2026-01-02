def normalize_energy(log):
    total = sum(log)
    average = total / len(log) if log else 0
    normalized = [x / average for x in log]
    return round(sum(normalized), 3)

def analyze_efficiency(data):
    peak = max(data)
    efficiency_ratio = peak / sum(data)
    return efficiency_ratio

def main():
    consumption_log = [120, 150, 130, 170, 140]
    baseline = 100
    adjustment_factor = 1.1
    adjusted_log = [int(x * adjustment_factor) for x in consumption_log]
    energy_threshold = normalize_energy(consumption_log)
    efficiency_score = analyze_efficiency(consumption_log)
    status = 'efficient' if efficiency_score > 0.2 else 'needs review'
    summary = f'System {status} with score {efficiency_score:.3f}'
    print(f'Result: {energy_threshold}')

main()