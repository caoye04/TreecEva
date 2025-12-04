def calculate_overlap(r1, r2):
    # Calculate the overlapping area between two rectangles
    # Each rectangle is represented as [x, y, width, height]
    # where (x,y) is the top-left corner
    
    # Find overlapping region boundaries
    left = max(r1[0], r2[0])
    top = max(r1[1], r2[1])
    right = min(r1[0] + r1[2], r2[0] + r2[2])
    bottom = min(r1[1] + r1[3], r2[1] + r2[3])
    
    # Check if rectangles overlap
    width = max(0, right - left)
    height = max(0, bottom - top)
    
    return width * height

# Define two rectangles on a grid system [x, y, width, height]
rect1 = [5, 8, 10, 6]
rect2 = [8, 10, 12, 9]

# Tracking total area for reference
total_area = rect1[2] * rect1[3] + rect2[2] * rect2[3]

# Calculate the overlapping area
overlap_area = calculate_overlap(rect1, rect2)

# Calculate unique area (non-overlapping)
unique_area = total_area - overlap_area

print(f"Result: {overlap_area}")