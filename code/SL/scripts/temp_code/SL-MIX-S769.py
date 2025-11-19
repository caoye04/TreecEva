import math

def min_boxes(total_cookies, box_capacity):
    if total_cookies <= box_capacity:
        return 1
    mid = total_cookies // 2
    left_boxes = min_boxes(mid, box_capacity)
    right_boxes = min_boxes(total_cookies - mid, box_capacity)
    return left_boxes + right_boxes

cookie_count = 987
box_size = 12
required_boxes = min_boxes(cookie_count, box_size)
# Adjust for overcounting due to recursive splitting
actual_boxes = math.ceil(cookie_count / box_size)
print(f'Result: {actual_boxes}')