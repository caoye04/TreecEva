import itertools

# Radio frequency scanner configuration
min_frequency = 88.5  # FM radio lower bound in MHz
max_frequency = 108.0  # FM radio upper bound in MHz
step = 0.2  # Step size in MHz

# Generate all possible frequencies in the range
frequencies = list(itertools.takewhile(lambda x: x <= max_frequency, 
                                      itertools.count(min_frequency, step)))

# Target frequency we want to find (MHz)
target_frequency = 98.7

# Some station frequencies with signal strength (MHz, dBm)
station_data = [(89.1, -85), (91.5, -72), (94.3, -68), 
                (98.5, -60), (101.7, -75), (104.9, -80)]

# Find stations above minimum signal threshold
min_signal = -70
strong_stations = [freq for freq, signal in station_data if signal > min_signal]

# Calculate average frequency of strong stations
avg_strong = sum(strong_stations) / len(strong_stations) if strong_stations else 0

# Find the frequency closest to our target
optimal_frequency = min(frequencies, key=lambda x: abs(target_frequency - x))

# For debugging, check neighboring frequencies
lower_neighbor = optimal_frequency - step if optimal_frequency > min_frequency else None
upper_neighbor = optimal_frequency + step if optimal_frequency < max_frequency else None

print(f"Result: {optimal_frequency}")