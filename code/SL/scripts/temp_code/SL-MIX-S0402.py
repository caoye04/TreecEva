from collections import defaultdict

def simulate_population(zone_data, year=0):
    if year >= 3:
        return zone_data
    
    next_zone_data = defaultdict(int)
    for zone, count in zone_data.items():
        # Each zone's population contributes to itself and its neighbors
        next_zone_data[zone] += count * 2
        next_zone_data[chr(ord(zone) + 1)] += count // 3
        next_zone_data[chr(ord(zone) - 1)] += count // 3
    
    # Remove non-alphabetic zone keys that might have been created
    filtered_data = {k: v for k, v in next_zone_data.items() if 'A' <= k <= 'Z'}
    return simulate_population(filtered_data, year + 1)

initial_zones = {'B': 150, 'C': 200, 'D': 180}
final_zone_counts = simulate_population(initial_zones)
total_butterfly_count = sum(final_zone_counts.values())
print(f"Result: {total_butterfly_count}")