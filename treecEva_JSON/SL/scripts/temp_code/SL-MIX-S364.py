import math

elevation_data = [150, 210, 180, 300, 270, 240, 330, 400, 360, 390]
terrain_distance = [i * 0.5 for i in range(len(elevation_data))]

log_scale_factor = lambda h: math.log(h + 10) if h > 0 else 0
exp_weight = lambda d: math.exp(-0.2 * d)

scaled_elevations = [log_scale_factor(h) for h in elevation_data]
weights = [exp_weight(d) for d in terrain_distance]

visibility_index = 0
for i in range(len(scaled_elevations)):
    if scaled_elevations[i] > sum(scaled_elevations[:i]) / (i + 1) if i > 0 else True:
        visibility_index += scaled_elevations[i] * weights[i]
    else:
        visibility_index -= scaled_elevations[i] * 0.1

visibility_index = round(visibility_index, 2)
print(f"Result: {visibility_index}")