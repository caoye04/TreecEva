def optimize_system(losses):
    base_capacity = 1500
    adjustment_factor = 0.85
    temp_storage = [base_capacity * (adjustment_factor ** i) for i in range(4)]
    filtered = [val for val in temp_storage if val > 1000]
    average_high = sum(filtered) / len(filtered)
    scaling = 1.2 if average_high > 1200 else 1.0
    return average_high * scaling

# Irrelevant diagnostic variable (minimal distraction)
diagnostic_mode = True
system_version = "v2.1"

# Core computation
efficiency_losses = [0.1, 0.15, 0.2]
final_calculation = optimize_system(efficiency_losses)
energy_capacity = int(final_calculation + 50)

print(f"Target result: {energy_capacity}")