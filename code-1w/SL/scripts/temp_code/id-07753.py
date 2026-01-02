def calculate_system_efficiency(ratios):
    adjusted = [r * (1.5 if r < 0.5 else 0.8) for r in ratios]
    efficiencies = [round((r + 0.1) ** 2, 3) for r in adjusted]
    
    # Irrelevant diagnostic log
    debug_mode = False
    if debug_mode:
        print(f'Debug: {efficiencies}')
    
    # Core logic
    baseline = sum(efficiencies) / len(efficiencies)
    peak_efficiency = max(efficiencies[1:-1])
    
    # Print result as required
    print(f'Target result: {peak_efficiency}')

# Input data
input_ratios = [0.3, 0.6, 0.4, 0.9, 0.2, 0.7]
calculate_system_efficiency(input_ratios)