def calculate_thermal_output(state, flow):
    base_output = 125.0
    efficiency = 0.88 if state == 'active' else 0.3
    adjusted_flow = flow if flow > 0 else 1
    return base_output * efficiency * (flow / adjusted_flow)

reactor_state = 'active'
coolant_flow = 4

# Irrelevant diagnostic variables (minimal interference)
diagnostic_code = 200
last_updated = "2023-11-15"

thermal_capacity = calculate_thermal_output(reactor_state, coolant_flow)
print(f"Result: {thermal_capacity}")