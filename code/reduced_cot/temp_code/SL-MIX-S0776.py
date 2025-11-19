from collections import namedtuple

# Define a simple data structure for tree sample
tree_sample = namedtuple('Sample', ['rings'])

# Sample data for an oak tree
oak_sample_a = tree_sample(rings=15)
oak_sample_b = tree_sample(rings=18)

# Environmental stress factor for oak trees
stress_factor = 0.9

# Calculate raw age estimation
raw_age = oak_sample_a.rings + oak_sample_b.rings

# Apply environmental stress adjustment
adjusted_age = raw_age * stress_factor

print(f'Result: {int(adjusted_age)}')