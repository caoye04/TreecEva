import math

# Irrelevant helper function (dead code path)
def dummy_normalization(x):
    return (x + 10) / 2 if x > 5 else x * 3

# Unused transformation table
echo_map = {i: (i ** 2) % 7 for i in range(15)}

# Misleading intermediate calculation with decoy variables
counterfeit_sum = 0
for i in range(1, 100):
    counterfeit_sum += (i * (i + 1)) // 2

# Real computation begins: system load simulation
processor_load = 7

# Simulated sensor array (mostly irrelevant)
sensor_readings = [23.5, 24.1, 22.7, 25.3, 26.0]
avg_sensor = sum(sensor_readings) / len(sensor_readings)
adjusted_avg = avg_sensor + 0.5 if avg_sensor < 24 else avg_sensor - 0.3

# Bit manipulation red herring
bitmask = 0b101010
masked_value = processor_load & bitmask | (bitmask << 2)

# Conditional expression used appropriately (required feature)
scaling_factor = 1.5 if processor_load > 5 else 0.8

# Decoy data structure with unused logic
task_queue = [{'priority': p, 'flag': p % 3 == 0} for p in range(1, 12)]
dropped_tasks = [t for t in task_queue if t['flag']]

# Core calculation function with distraction
def calculate_thermal_output(load):
    base_heat = load ** 3
    
    # Distractor: irrelevant recursive helper
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    
    # More noise: unused logarithmic scaling
    log_comp = math.log(load + 5) * 2.1
    
    # Real work: multi-step thermal model
    dynamic_mod = 0
    for step in range(1, load + 1):
        dynamic_mod += step * (step + 1) // 2  # triangular number accumulation
    
    # Key conditional expression combining prior results
    secondary_boost = dynamic_mod * scaling_factor if load >= 4 else dynamic_mod / 2
    
    # Final composition
    result = base_heat + secondary_boost
    
    # Dead code branch that looks important
    if result > 1000:
        result = int(result * 0.95)
    
    return result

# Trigger the actual computation
temperature_buffer = []
for cycle in range(3):
    temp_val = calculate_thermal_output(processor_load)
    temperature_buffer.append(temp_val)

# Critical assignment point — this is the target
thermal_capacity = calculate_thermal_output(processor_load)

# Output required format
print(f"Result: {thermal_capacity}")