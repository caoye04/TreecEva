def pack_cookies(total_cookies, box_capacity):
    full_boxes = total_cookies // box_capacity
    leftover_cookies = total_cookies % box_capacity
    return leftover_cookies

leftover_cookies = pack_cookies(137, 12)
print(f'Result: {leftover_cookies}')