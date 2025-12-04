# Calculate the total valid votes in an election

# Initial vote counts from different polling stations
vote_counts = {
    'station_1': 342,
    'station_2': 418,
    'station_3': 275,
    'station_4': 189
}

# Stations with technical issues
problematic_stations = ['station_2']

# Adjustment factors for each station (based on historical data)
adjustment_factors = {
    'station_1': 1.0,
    'station_2': 0.8,  # Reduce station_2 votes due to technical issues
    'station_3': 1.0,
    'station_4': 1.0
}

# Apply adjustments to vote counts
adjusted_votes = {}
for station, count in vote_counts.items():
    adjusted_votes[station] = int(count * adjustment_factors.get(station, 1.0))

# Filter out stations with major problems
filtered_votes = {}
for station, count in adjusted_votes.items():
    if station not in problematic_stations:
        filtered_votes[station] = count

# Calculate the total valid votes
total_votes = sum(filtered_votes.values())

print(f"Total valid votes: {total_votes}")