from collections import defaultdict

def hash_color(r, g, b):
    return (r * 31 + g) * 31 + b

def transform_pixel(canvas, x, y):
    if x < 0 or y < 0 or x >= len(canvas) or y >= len(canvas[0]):
        return 0
    r, g, b = canvas[x][y]
    # Neighbor influence: average of immediate neighbors' red values
    neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    neighbor_reds = [canvas[nx][ny][0] for nx, ny in neighbors if 0 <= nx < len(canvas) and 0 <= ny < len(canvas[0])]
    avg_red = sum(neighbor_reds) // len(neighbor_reds) if neighbor_reds else r
    # Transformation: increase blue by neighbor influence
    new_b = min(255, b + (avg_red // 10))
    return hash_color(r, g, new_b)

canvas = [
    [(100, 150, 200), (120, 160, 180)],
    [(110, 155, 190), (125, 165, 185)]
]

artistic_score = 0
for i in range(len(canvas)):
    for j in range(len(canvas[0])):
        transformed_hash = transform_pixel(canvas, i, j)
        artistic_score += transformed_hash

print(f"Result: {artistic_score}")