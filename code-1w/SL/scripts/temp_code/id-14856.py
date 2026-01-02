from itertools import compress

# Grid energy production data (in MW) for 7 solar farms over a week
energy_output = [
    [12.5, 10.3, 14.1, 9.8, 11.7, 13.2, 10.9],
    [8.7,  9.1,  7.6,  10.2, 9.9,  8.8,  9.5],
    [15.2, 14.8, 16.1, 15.6, 14.3, 16.0, 15.8],
    [6.3,  7.1,  6.9,  6.7,  7.2,  6.8,  7.0],
    [11.4, 12.0, 10.8, 11.9, 12.3, 11.1, 11.6],
    [9.5,  9.3,  9.7,  9.6,  9.4,  9.8,  9.2],
    [13.1, 13.5, 12.9, 13.7, 13.3, 13.6, 13.0]
]

# Efficiency thresholds for each farm (MW)
thresholds = [10.0, 8.0, 15.0, 6.5, 11.0, 9.0, 13.0]

# Determine which farms meet daily efficiency threshold on at least 5 days
valid_days_count = []
for output in energy_output:
    valid_days = sum(1 for x in output if x >= thresholds[energy_output.index(output)])
    valid_days_count.append(valid_days)

# Identify farms that are efficient on at least 5 out of 7 days
is_efficient_farm = [count >= 5 for count in valid_days_count]

# Extract top 3 days for each farm and average them
peak_averages = []
for output in energy_output:
    sorted_output = sorted(output, reverse=True)
    top_three_avg = sum(sorted_output[:3]) / 3
    peak_averages.append(top_three_avg)

# Use itertools.compress to select only efficient farms' peak averages
optimized_grids = list(compress(peak_averages, is_efficient_farm))

# Final aggregation step
total_capacity = sum(optimized_grids)
print(f"Result: {total_capacity}")