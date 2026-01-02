from collections import defaultdict

# Simulate resource distribution in a microgrid system with efficiency decay
def main():
    node_count = 7
    base_capacity = 120
    decay_factor = 0.92

    # Initialize resource pool with default values
    resource_pool = [base_capacity * (decay_factor ** i) for i in range(node_count)]

    # Track efficiency per node using defaultdict
    efficiency_map = defaultdict(float)
    temp_buffer = []

    for i in range(node_count):
        raw_efficiency = (0.88 + i * 0.015) % 1.0
        efficiency_map[f'node_{i}'] = round(raw_efficiency, 3)
        
        # Distractor: buffer some irrelevant intermediate values
        temp_buffer.append(base_capacity * (1 - raw_efficiency))

    # Irrelevant sorting - does not impact final result
    temp_buffer.sort(reverse=True)
    buffer_median = temp_buffer[len(temp_buffer)//2] if len(temp_buffer) > 0 else 0

    # Secondary distractor computation: simulate unused load shift
    shifted_loads = list(map(lambda x: x * 0.95, resource_pool[1::2]))
    average_shift = sum(shifted_loads) / len(shifted_loads) if shifted_loads else 0

    # Core logic: compute effective distribution based on efficiency and capacity
    def calculate_distribution(eff_map, resources):
        total_effective = 0.0
        for idx, cap in enumerate(resources):
            key = f'node_{idx}'
            if key in eff_map:
                total_effective += cap * eff_map[key]
        return int(round(total_effective))

    # Key execution point
    final_load = calculate_distribution(efficiency_map, resource_pool)

    # Print required output
    print(f"Result: {final_load}")

    # Additional red herring: unused transformation
    transformed = [round(x**0.5, 2) for x in resource_pool]
    transformed_sum = sum(transformed)

    return final_load

if __name__ == "__main__":
    main()