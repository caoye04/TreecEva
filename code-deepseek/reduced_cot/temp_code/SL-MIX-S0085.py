initial_capacity = 150
buffer_size = initial_capacity * 2
threshold = buffer_size // 3
overflow_margin = threshold + 50

active_connections = 25
max_connections = 100
connection_ratio = active_connections / max_connections
load_factor = 1.5 if connection_ratio > 0.2 else 0.8

system_load = active_connections * load_factor
redundancy_factor = 2 if system_load > threshold else 1

allocated_memory = buffer_size * redundancy_factor
unused_buffer = allocated_memory - buffer_size

final_value = allocated_memory if system_load > overflow_margin else unused_buffer
result = final_value
print(f"Target result: {result}")