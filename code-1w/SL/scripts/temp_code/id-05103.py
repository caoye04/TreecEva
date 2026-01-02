def calculate_grid_efficiency(phases, threshold):
    phase_names = ['alpha', 'beta', 'gamma']
    phase_powers = [p * 1.5 for p in phases]
    status_codes = [200, 201, 202]
    
    indexed_powers = list(enumerate(phase_powers))
    filtered_powers = [power for i, power in indexed_powers if power > threshold]
    
    safety_margin = 1.1
    total_phase_power = sum(filtered_powers)
    efficiency_ratio = total_phase_power / (sum(phase_powers) + 1e-9)
    
    diagnostics = dict(zip(phase_names, status_codes))
    return total_phase_power

phases_input = [18, 25, 30]
threshold_limit = 35
total_phase_power = calculate_grid_efficiency(phases_input, threshold_limit)
print(f"Result: {total_phase_power}")