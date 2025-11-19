import math

# Player position and view parameters
player_x, player_y = 5, 5
view_radius = 3.5

# Grid points considered within potential view (bounding box)
min_x, max_x = int(player_x - view_radius), int(player_x + view_radius)
min_y, max_y = int(player_y - view_radius), int(player_y + view_radius)

# Set of obstacle positions
obstacle_set = frozenset([(4, 6), (5, 6), (6, 6), (5, 4)])

# Count visible unobstructed points using short-circuit evaluation
visible_clear_points = 0
for gx in range(min_x, max_x + 1):
    for gy in range(min_y, max_y + 1):
        # Check if point is within circular view AND not an obstacle
        distance_squared = (gx - player_x)**2 + (gy - player_y)**2
        if distance_squared <= view_radius**2 and (gx, gy) not in obstacle_set:
            visible_clear_points += 1

print(f"Result: {visible_clear_points}")