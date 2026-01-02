from collections import defaultdict

# Simulate packet transmission rates per channel
def generate_transmission_data():
    data = defaultdict(float)
    data['channel_A'] = 12.5
    data['channel_B'] = 8.3
    data['channel_C'] = 15.7
    data['channel_D'] = 0.0  # No activity
    return data

# Calculate effective network load with decay factor
def calculate_network_load(rates):
    base_factor = 0.9
    load = 0.0
    for key in rates:
        if rates[key] > 0:
            # Apply exponential decay based on channel name length
            decay = base_factor ** len(key)
            load += rates[key] * decay
    return load

# Irrelevant helper: counts non-empty channels (mild distraction)
def count_active_channels(channels):
    return sum(1 for v in channels.values() if v > 0)

transmission_rates = generate_transmission_data()
active_count = count_active_channels(transmission_rates)  # Distractor assignment
initial_sum = sum(transmission_rates.values())  # Another irrelevant calculation
total_load = calculate_network_load(transmission_rates)
print(f"Result: {total_load}")