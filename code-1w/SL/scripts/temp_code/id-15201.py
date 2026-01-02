def analyze_distribution(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance

# Simulate sensor node readings across zones
data_zones = [45, 67, 52, 71, 49, 88, 63, 58]

# Irrelevant statistical analysis (distractor)
distribution_variance = analyze_distribution(data_zones)

# Initialize storage matrix with capacity allocations
capacity_map = {
    'zone_A': [12, 15, 10],
    'zone_B': [20, 18, 25],
    'zone_C': [8, 14, 16],
    'zone_D': [22, 22, 22]
}

# Build a transposed matrix for processing
storage_matrix = []
for i in range(3):
    row = []
    for key in sorted(capacity_map.keys()):
        row.append(capacity_map[key][i])
    storage_matrix.append(row)

# Threshold determined from environmental constraints
threshold = 15

# Track zone utilization (semi-relevant tracking)
utilization_log = {}
for zone, values in capacity_map.items():
    utilized = sum(1 for v in values if v > threshold)
    utilization_log[zone] = utilized  # Not used later but looks important

# Secondary distraction: string-based status encoding
status_codes = ['OK', 'HIGH', 'CRIT']
encoded_status = ''
for val in data_zones:
    if val < 60:
        encoded_status += status_codes[0]
    elif val < 80:
        encoded_status += status_codes[1]
    else:
        encoded_status += status_codes[2]

# Checksum calculation on encoded string (dead code path)
checksum = 0
for char in encoded_status:
    checksum += ord(char) % 7
checksum = checksum % 11

# Core logic: compute remaining capacity below threshold
def calculate_remaining_capacity(matrix, limit):
    total_available = 0
    for row in matrix:
        for cell in row:
            if cell <= limit:
                total_available += cell
            else:
                total_available += (cell - limit) // 2  # partial credit for overflow
    adjustment_factor = len(encoded_status.replace('OK', ''))  # subtle red herring
    return total_available - adjustment_factor  # actual dependency on distractor

# Execute main computation
final_capacity = calculate_remaining_capacity(storage_matrix, threshold)

# Print result as required
print(f"Target result: {final_capacity}")