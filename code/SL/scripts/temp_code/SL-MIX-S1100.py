def calculate_ride_cycle(ride_letter):
    return (ord(ride_letter) - ord('A')) % 5 + 3

rides = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
cycle_times = {ride: calculate_ride_cycle(ride) for ride in rides}

# Visitor preference sets
visitor_sets = [
    frozenset(['A', 'C', 'G']),
    frozenset(['B', 'D', 'F']),
    frozenset(['A', 'B', 'E']),
    frozenset(['C', 'E', 'G'])
]

total_satisfaction_score = 0

for shift in [1, 2, 3]:
    if shift == 1:
        active_rides = {'A', 'C', 'E'}
    elif shift == 2:
        active_rides = {'B', 'D', 'F'}
    elif shift == 3:
        active_rides = {'A', 'B', 'G'}
    else:
        active_rides = set()
    
    shift_points = sum(
        len(active_rides & visitor_set) * cycle_times[ride]
        for ride in active_rides
        for visitor_set in visitor_sets
        if ride in visitor_set
    )
    total_satisfaction_score += shift_points

print(f"Result: {total_satisfaction_score}")