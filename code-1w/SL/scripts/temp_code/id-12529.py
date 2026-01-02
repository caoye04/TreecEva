from itertools import compress, cycle

def analyze_route_efficiency(distances, thresholds):
    """Determine efficient segments based on threshold comparison."""
    efficiency_flags = [d <= t for d, t in zip(distances, thresholds)]
    return list(compress(distances, efficiency_flags))

def calculate_segment_loads(vehicles, capacity_per_axle):
    """Calculate total load per vehicle (simulated with axle count)."""
    loads = []
    for v in vehicles:
        axle_count = v % 4 + 2  # Simulate axles between 2-5
        load = axle_count * capacity_per_axle
        loads.append(load)
    return loads

def calculate_remaining_capacity(route_map, schedule):
    base_capacities = {k: v * 1.5 for k, v in route_map.items()}
    
    # Simulate time-based availability using cycling pattern
    time_slots = ['morning', 'afternoon', 'night']
    availability_cycle = cycle(time_slots)
    availability_multiplier = {}
    for key in route_map.keys():
        next_slot = next(availability_cycle)
        multiplier = 0.8 if next_slot == 'night' else 1.0
        availability_multiplier[key] = multiplier

    adjusted_capacities = {}
    for stop, base in base_capacities.items():
        adj = base * availability_multiplier[stop]
        adjusted_capacities[stop] = adj
    
    # Dummy tracking variables (not used in final result)
    total_segments = len(adjusted_capacities)
    average_base = sum(base_capacities.values()) / total_segments
    cumulative_proxy = 0
    for i, cap in enumerate(adjusted_capacities.values()):
        cumulative_proxy += cap * (i % 3 + 1) / 100  # Irrelevant accumulation

    # Core logic: apply schedule filtering
    valid_stops = []
    temp_sum = 0
    for idx, (stop, time) in enumerate(schedule):
        if time == 'morning':
            valid_stops.append(stop)
            temp_sum += idx  # Distractor computation

    # Final capacity calculation
    final_capacity = 0
    for stop in valid_stops:
        if stop in adjusted_capacities:
            final_capacity += adjusted_capacities[stop]
    
    # Additional red herring: sort and reverse dummy list
    dummy_list = [cumulative_proxy, temp_sum, average_base]
    dummy_list.sort(reverse=True)
    dummy_list = [x * 0.1 for x in dummy_list]  # Not affecting output

    return int(final_capacity)

# Define inputs
logistics_map = {
    'A': 20,
    'B': 35,
    'C': 25,
    'D': 40,
    'E': 30
}

transport_schedule = [
    ('A', 'morning'),
    ('B', 'night'),
    ('C', 'morning'),
    ('D', 'afternoon'),
    ('E', 'morning')
]

# Misleading preliminary calculations
distances = [15, 40, 22, 50, 28]
thresholds = [25, 38, 20, 55, 27]
efficient_segments = analyze_route_efficiency(distances, thresholds)
vehicle_fleet = [18, 24, 30, 12]
per_axle_capacity = 8
vehicle_loads = calculate_segment_loads(vehicle_fleet, per_axle_capacity)

# Key execution point
final_capacity = calculate_remaining_capacity(logistics_map, transport_schedule)

# Output result
print(f"Result: {final_capacity}")