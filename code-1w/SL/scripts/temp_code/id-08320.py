def calculate_peak(grid):
    total = 0
    peak_capacity = 0
    
    # Analyze traffic grid efficiency using slicing and enumeration
    for i, row in enumerate(grid):
        if i % 2 == 0:
            segment = row[1:4]  # Slice middle columns
            total += sum(segment)
            
            # Track maximum row sum on even-indexed rows
            row_sum = sum(row)
            if row_sum > peak_capacity:
                peak_capacity = row_sum
    
    # Dummy variables for minimal interference (intervention level 5)
    avg_flow = total / 2 if total > 0 else 0
    dummy_flag = False
    temp_buffer = [avg_flow * 2]
    
    # Use zip to align diagonal elements (irrelevant to main logic)
    diagonals = [a[i] for i, a in enumerate(grid) if i < len(a)]
    paired = list(zip(diagonals[:-1], diagonals[1:]))
    
    return peak_capacity

# Input grid representing urban traffic load per zone
grid = [
    [3, 6, 2, 8, 1],
    [4, 5, 7, 3, 9],
    [2, 8, 6, 5, 4],
    [9, 1, 3, 7, 2],
    [5, 4, 8, 6, 3]
]

# Key computation
peak_capacity = calculate_peak(grid)

# Output result
print(f"Target result: {peak_capacity}")