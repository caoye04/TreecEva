from collections import defaultdict

# Simulate hourly energy consumption and system capacity for a microgrid
time_slots = ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00"]
energy_input = [120, 200, 250, 300, 275, 190]  # Solar/wind input in kWh
energy_demand = [180, 220, 240, 320, 310, 230]  # Demand in kWh

# Compute net surplus/deficit
net_flow = [gen - use for gen, use in zip(energy_input, energy_demand)]

# Initialize storage levels with default behavior
storage_system = defaultdict(float)
storage_capacity_kwh = 150
current_charge = 50  # Initial charge in kWh

# Charge/discharge logic over time
for surplus in net_flow:
    current_charge += surplus
    # Cap at maximum capacity and prevent underflow
    if current_charge > storage_capacity_kwh:
        current_charge = storage_capacity_kwh
    elif current_charge < 0:
        current_charge = 0
    storage_system[len(storage_system)] = current_charge

# Record capacity utilization levels
capacity_levels = [val / storage_capacity_kwh * 100 for val in storage_system.values()]

# Key computation point
peak_capacity = max(capacity_levels)

print(f"Result: {peak_capacity}")