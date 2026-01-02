from collections import defaultdict

def calculate_network_load(rates, efficiency):
    load = 0
    for i, rate in enumerate(rates):
        adjusted_rate = rate * efficiency
        if adjusted_rate > 50:
            load += adjusted_rate * 1.2
        else:
            load += adjusted_rate
    return int(load)

def monitor_system_health():
    # Irrelevant monitoring logic (minimal distraction)
    health_flags = defaultdict(bool)
    health_flags['network'] = True
    health_flags['disk'] = False

transmission_rates = [30, 60, 40, 80]
efficiency_factor = 0.85

# Key computation step
total_load = calculate_network_load(transmission_rates, efficiency_factor)

monitor_system_health()  # Call with no side effects

print(f"Result: {total_load}")