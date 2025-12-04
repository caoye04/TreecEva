from collections import Counter, defaultdict

def process_dataset(raw_data, threshold=0.5):
    # Process raw sensor readings
    processed = []
    for i, value in enumerate(raw_data):
        # Apply calibration factor
        calibrated = value * 1.08 - 0.15
        
        # Filter noise
        if i % 3 == 0:
            calibrated += 0.22
        
        # Add to processed data if above threshold
        if calibrated > threshold:
            processed.append(calibrated)
    
    # This is never used but looks important
    noise_ratio = len(processed) / len(raw_data) if raw_data else 0
    return processed

def analyze_distribution(data):
    # Count frequency of each value rounded to nearest 0.5
    frequency = Counter([round(x * 2) / 2 for x in data])
    
    # Find most common values - this is a distraction
    common_values = frequency.most_common(3)
    
    # Calculate distribution metrics
    total = sum(data)
    mean = total / len(data) if data else 0
    
    # Return mean and frequency data
    return mean, frequency

def calculate_density(data, dimensions):
    # Extract volume from dimensions
    width, height, depth = dimensions
    volume = width * height * depth
    
    # This set operation is just a distraction
    unique_values = set([round(x, 1) for x in data])
    
    # Misleading intermediate calculation
    potential_density = len(unique_values) / volume if volume else 0
    
    # Group data into regions
    regions = defaultdict(list)
    for value in data:
        # Determine region based on value
        region_id = int(value * 2) % 3
        regions[region_id].append(value)
    
    # Calculate actual density
    if len(regions) > 0 and volume > 0:
        # Average value across all regions
        region_averages = [sum(values)/len(values) for values in regions.values()]
        region_weight = 0.75  # Weighting factor
        
        # The actual calculation that matters
        data_points = len(data)
        data_density = data_points / volume
        return data_density
    else:
        return 0

# Sample sensor data
raw_sensor_data = [1.2, 0.8, 0.3, 1.5, 0.9, 1.7, 0.4, 1.3, 1.1]

# Apply initial filtering
filtered_data = process_dataset(raw_sensor_data, threshold=0.4)

# These dimensions are in meters
dimensions = (2.0, 1.5, 1.0)

# Additional preprocessing that isn't actually needed
preprocessed = []
for reading in filtered_data:
    # Apply unnecessary transformation
    transformed = reading ** 0.5 * 2
    if transformed > 2.0:
        preprocessed.append(reading)
    else:
        # This branch is actually never taken with our data
        transformed -= 0.1
        preprocessed.append(transformed)

# This is misleading - we're not actually using the preprocessed data
mean, freq_data = analyze_distribution(preprocessed)

# Calculate the density using the original filtered data, not preprocessed
data_density = calculate_density(filtered_data, dimensions)

# More distraction calculations
optimal_density = data_density * 1.25
efficiency_score = (data_density / optimal_density) * 100

# Slice operations that don't affect the result
if len(filtered_data) > 3:
    high_values = filtered_data[-3:]
    low_values = filtered_data[:2]
    mid_values = filtered_data[2:-3]
else:
    high_values = filtered_data
    low_values = []
    mid_values = []

print(f"Result: {data_density}")