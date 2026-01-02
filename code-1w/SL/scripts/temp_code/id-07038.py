def analyze_efficiency(data):
    efficiency_list = []
    for i, entry in enumerate(data):
        raw_efficiency = entry['output'] / (entry['input'] + 1e-5)
        adjusted_efficiency = raw_efficiency * entry.get('factor', 1.0)
        efficiency_list.append(adjusted_efficiency)
    
    # Distractor: irrelevant smoothing
    smoothed = [efficiency_list[0]]
    for i in range(1, len(efficiency_list)):
        smoothed.append(0.7 * efficiency_list[i] + 0.3 * smoothed[-1])
    
    return efficiency_list


def calculate_phase_trend(phases):
    trends = []
    for i in range(1, len(phases)):
        delta = phases[i]['output'] - phases[i-1]['output']
        trends.append(delta)
    average_trend = sum(trends) / len(trends) if trends else 0
    return average_trend

production_phases = [
    {'input': 120, 'output': 98, 'factor': 1.05},
    {'input': 150, 'output': 112, 'factor': 0.98},
    {'input': 130, 'output': 107, 'factor': 1.02},
    {'input': 160, 'output': 118, 'factor': 1.01}
]

# Irrelevant preprocessing
phase_names = ['initiation', 'growth', 'stabilization', 'decline']
indexed_phases = dict(zip(phase_names, production_phases))

# Distractor computation: unused metrics
redundant_ratios = [
    p['output'] / p['input'] for p in production_phases if p['input'] > 100
]

# Semi-relevant transformation
baseline = production_phases[0]['output']
evaluated_outputs = []
for idx, phase in enumerate(production_phases):
    offset_correction = phase['output'] - baseline - idx * 2
    evaluated_outputs.append(offset_correction * phase.get('factor', 1.0))

# Core logic embedded within noise
average_output = sum(p['output'] for p in production_phases) / len(production_phases)
trend_factor = calculate_phase_trend(production_phases)
efficiencies = analyze_efficiency(production_phases)
overall_efficiency = sum(efficiencies) / len(efficiencies)

# Key distraction: complex but unused structure
summary_matrix = []
for i, (name, phase) in enumerate(indexed_phases.items()):
    row = []
    for j in range(3):
        row.append((i * j + phase['output']) % 5)
    summary_matrix.append(row)

# Final calculation with minor interference
fluctuation_penalty = 0
for i in range(1, len(evaluated_outputs)):
    diff = abs(evaluated_outputs[i] - evaluated_outputs[i-1])
    if diff > 10:
        fluctuation_penalty += 0.5

scaling_constant = 2.1

# Critical statement
final_yield = int(scaling_constant * average_output * overall_efficiency - fluctuation_penalty * 10)

print(f"Result: {final_yield}")