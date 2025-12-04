# Sensor network status monitoring

# Sensor activation status (1=active, 0=inactive)
is_active = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Configuration parameters
network_id = 5
device_count = len(is_active)

# Calculate monitoring region
start_idx = network_id % 3  # Starting index for monitoring
end_idx = device_count - (network_id // 3)  # Ending index for monitoring

# Calculate sensor statistics
total_sensors = device_count
faulty_sensors = is_active.count(0)
active_sensors = sum(is_active[start_idx:end_idx])

# Additional data processing
reliability_score = (active_sensors / total_sensors) * 100 if total_sensors > 0 else 0

print(f"Result: {active_sensors}")