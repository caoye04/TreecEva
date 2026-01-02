def calculate_performance(accuracy, bonus):
    base_score = sum([a * 10 for a in accuracy])
    time_multiplier = 1.2 if bonus else 1.0
    return int(base_score * time_multiplier)

# Simulation data
accuracy_list = [0.85, 0.92, 0.78, 0.96]
time_bonus = True
initial_total = sum(accuracy_list) * 100  # Irrelevant tracking variable
normalization_factor = max(accuracy_list)  # Unused auxiliary variable
final_score = calculate_performance(accuracy_list, time_bonus)
print(f"Result: {final_score}")