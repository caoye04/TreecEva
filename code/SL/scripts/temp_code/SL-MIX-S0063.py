base_coordinates = (15, 8, 22)
threshold = 12
x, y, z = base_coordinates

adjusted_x = x + 5 if x < threshold else x - 3
adjusted_y = y * 2 if y > threshold else y + 7
adjusted_z = z // 2 if z % 2 == 0 else z * 2

adjusted_value = adjusted_x + adjusted_y + adjusted_z
final_result = adjusted_value

print(f"Result: {final_result}")