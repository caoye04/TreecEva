def calculate_network_capacity(speeds, redundancy):
    base_total = sum(speeds)
    redundant_links = len([s for s in speeds if s > 100])
    efficiency = 0.85 if redundant_links >= 2 else 0.65
    adjusted = base_total * efficiency
    return int(adjusted) + (100 if redundancy else 0)

# System configuration
link_speeds = [95, 150, 120, 80]
redundancy_factor = True

# Irrelevant distraction: logging setup (minimal interference)
log_level = "INFO"
enable_debug = False

# Key computation
final_capacity = calculate_network_capacity(link_speeds, redundancy_factor)
print(f"Result: {final_capacity}")