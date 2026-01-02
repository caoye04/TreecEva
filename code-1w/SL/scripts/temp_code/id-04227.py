def calculate_remaining_capacity(vehicles, stations):
    total_vehicles = sum(v[1] for v in vehicles)
    max_capacity = sum(s[1] for s in stations)
    utilized = max_capacity * 0.7
    available = max_capacity - utilized
    if available > total_vehicles:
        return available - total_vehicles
    else:
        return total_vehicles - available

# Irrelevant auxiliary data (distractor)
weather_data = [('Day1', 'Sunny'), ('Day2', 'Rainy')]
temp_readings = [22.5, 25.1, 19.8]

# Core data structures
transport_fleet = [
    ('truck', 120),
    ('van', 85),
    ('bike', 60)
]

charging_stations_network = [
    ('ZoneA', 100),
    ('ZoneB', 150),
    ('ZoneC', 200)
]

# Key computation
final_capacity = calculate_remaining_capacity(transport_fleet, charging_stations_network)
print(f"Result: {final_capacity}")