def compute_score(values, limit):
    valid_count = 0
    temp_sum = 0
    
    for num in values:
        if num > limit:
            valid_count += 1
            temp_sum += num
    
    return temp_sum // valid_count if valid_count > 0 else 0

data_points = [45, 28, 67, 32, 89, 54, 23, 76]
threshold = 35
final_score = compute_score(data_points, threshold)
print(f"Target result: {final_score}")