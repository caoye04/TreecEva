from itertools import groupby

# Simulate sensor readings from warehouse shelves with item weights
cargo_data = '12,15,12,12,18,20,20,18,22,25,25,25'

# Parse and sort weight readings
cargo_weights = sorted(map(int, cargo_data.split(',')))

# Group consecutive identical weights and count occurrences
grouped = {k: len(list(g)) for k, g in groupby(cargo_weights)}

# Identify frequently occurring weight clusters (appearing more than once)
frequent_weights = [k for k, count in grouped.items() if count > 1]

# Filter original weights to keep only items with frequent base weights
filtered_weights = [w for w in cargo_weights if w in frequent_weights]

# Compute total adjusted load
total_weight = sum(filtered_weights)

print(f"Result: {total_weight}")