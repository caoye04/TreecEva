from itertools import compress

def process_intervals(intervals, limit):
    # Calculate midpoints of each interval
    midpoints = [(start + end) / 2 for start, end in intervals]
    
    # Determine which midpoints are below threshold
    mask = [mid < limit for mid in midpoints]
    
    # Use compress to filter intervals by condition
    filtered_intervals = list(compress(intervals, mask))
    
    # Compute total width of filtered intervals
    total_width = sum(end - start for start, end in filtered_intervals)
    
    # Apply scaling factor based on count
    scale = len(filtered_intervals) if filtered_intervals else 1
    result = total_width * scale
    
    return result

# Define input data
intervals = [(2, 6), (3, 7), (10, 14), (1, 4)]
threshold = 5.0

# Irrelevant auxiliary variable (minor distraction)
dummy_var = [x**2 for x in range(3)]

result = process_intervals(intervals, threshold)
print(f"Result: {result}")