from collections import defaultdict

def process_power_flow(readings, capacity):
    # Distractor: unused energy conversion factor
    conversion_factor = 1.341  # horsepower to kW - misleading constant
    
    # Main logic with bitwise operations
    base_power = 0
    for i, reading in enumerate(readings):
        # Distractor: misleading temporary calculation
        temp_shift = (reading << 2) & 0xFF  # irrelevant bit operation
        
        if i % 3 == 0:
            base_power += reading * 2
        elif i % 3 == 1:
            base_power += reading ^ 0b1010  # XOR operation
        else:
            base_power += reading | 0b0011  # OR operation
    
    # Distractor: unused backup adjustment
    unused_adjustment = capacity * 0.75  # dead code path
    
    # Core energy calculation
    capacity_mask = capacity & 0b1111
    adjusted_base = base_power - (base_power >> 1)
    
    # Distractor: misleading intermediate value
    misleading_peak = adjusted_base * 1.25  # never used
    
    if capacity_mask > 7:
        energy_result = adjusted_base + (capacity_mask * 10)
    else:
        energy_result = adjusted_base - capacity_mask
    
    return energy_result

# Main execution with distractor variables
initial_readings = [15, 22, 8, 31, 12, 19]
backup_capacity = 11

# Distractor: irrelevant data structure
power_distribution = defaultdict(int)
for idx, val in enumerate(initial_readings):
    power_distribution[f'node_{idx}'] = val * 3  # never used

# Distractor: misleading calculation path
redundant_sum = sum(initial_readings) * 0.5  # dead code

# Key execution point
energy_calculation = process_power_flow(initial_readings, backup_capacity)

# Final energy with additional distractor operations
voltage_offset = 7  # misleading variable
final_energy = energy_calculation - (voltage_offset & 0b0011)

print(f"Target result: {final_energy}")