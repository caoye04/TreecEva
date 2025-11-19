camera_rect = {'left': 0, 'right': 100, 'bottom': 0, 'top': 100}
objects = [
    {'id': 1, 'bbox': {'left': 10, 'right': 30, 'bottom': 10, 'top': 30}},
    {'id': 2, 'bbox': {'left': 150, 'right': 170, 'bottom': 150, 'top': 170}},
    {'id': 3, 'bbox': {'left': 50, 'right': 80, 'bottom': 50, 'top': 80}},
    {'id': 4, 'bbox': {'left': -20, 'right': -10, 'bottom': -20, 'top': -10}}
]

# Function to check if two rectangles intersect (axis-aligned bounding boxes)
def rectangles_intersect(rect1, rect2):
    return not (rect1['right'] < rect2['left'] or
                rect1['left'] > rect2['right'] or
                rect1['top'] < rect2['bottom'] or
                rect1['bottom'] > rect2['top'])

# Simulate a simple occlusion test that always passes for objects in the scene
# In a real engine, this would be a complex rasterization or depth-buffer check
def is_occluded(obj_id):
    # Dummy implementation: odd IDs are occluded
    return obj_id % 2 == 1

visible_count = 0
for obj in objects:
    # Short-circuit evaluation: if not in frustum, don't check occlusion
    if rectangles_intersect(camera_rect, obj['bbox']) and not is_occluded(obj['id']):
        visible_count += 1

print(f"Result: {visible_count}")