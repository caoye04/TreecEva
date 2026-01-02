def analyze_fragment(data, index):
    if index < len(data) and data[index] > 0:
        return data[index] * 2
    return 0

fragments = [3, -1, 4, 1, 5, -2, 9]
buffer_snapshot = fragments[2:5]

# Irrelevant accumulation (distractor)
total_scan = 0
for val in fragments:
    total_scan += abs(val)

# Semi-relevant preprocessing
temp_analysis = []
for i in range(len(fragments)):
    temp_analysis.append(analyze_fragment(fragments, i))

# Buffer optimization logic
threshold = 4
capacities = []

for x in buffer_snapshot:
    if x >= threshold:
        capacities.append(x ** 2)
    else:
        capacities.append(x + 1)

# Additional distraction: unused transformation
transformed_caps = [c // 2 for c in capacities if c > 4]

# Core computation with slicing and conditional logic
def optimize_buffer(buf, limit):
    result = 0
    for item in buf:
        if item > limit:
            result += item * 1.5
        elif item == limit:
            result += item
        else:
            result += item * 0.5
    return int(result)

final_capacity = optimize_buffer(capacities, threshold)

# Print required output
print(f"Target result: {final_capacity}")