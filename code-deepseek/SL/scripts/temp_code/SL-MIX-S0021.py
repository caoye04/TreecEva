from collections import Counter

# Inventory tracking system for warehouse capacity planning
base_capacity = 850
overflow_reserve = 120
redundancy_factor = 3
temp_buffer = 75
primary_storage = base_capacity + temp_buffer
overflow_storage = overflow_reserve * 2
storage_distribution = Counter({'main': primary_storage, 'backup': overflow_storage})
distribution_sum = sum(storage_distribution.values())
capacity_adjustment = distribution_sum // redundancy_factor
final_capacity = (primary_storage + overflow_storage) // redundancy_factor
print(f"Target result: {final_capacity}")