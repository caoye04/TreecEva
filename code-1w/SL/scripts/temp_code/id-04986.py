from collections import defaultdict

# Simulate water treatment plant stages and flow metrics
stages = ['coagulation', 'sedimentation', 'filtration', 'disinfection']
flow_rates = [85.5, 72.3, 68.9, 75.1]  # in m³/h
pressure_readings = [4.2, 3.8, 5.1, 4.6]

efficiency_map = defaultdict(float)
for i, stage in enumerate(stages):
    efficiency_map[stage] = flow_rates[i] * (1 + pressure_readings[i] / 10)

efficient_stages = [s for s, e in efficiency_map.items() if e > 70.0]

bypass_mode = False
maintenance_log = {"last_cleaned": "2023-07-15", "bypass_valve": False}
system_active = not bypass_mode and not maintenance_log["bypass_valve"]

efficiency_factor = round(sum(efficiency_map[s] for s in efficient_stages) / len(efficient_stages), 2)

filtration_score = len(efficient_stages) * efficiency_factor if system_active else 0

# Irrelevant tracking variable (minimal distraction)
current_operator_id = "OPR-284"

print(f"Result: {filtration_score}")