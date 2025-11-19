import math
from contextlib import contextmanager

@contextmanager
def navigation_context():
    yield

waypoint_ids = [b'A1', b'B2', b'C3']
waypoint_coords = [(0, 0), (3, 4), (6, 8)]

is_valid_waypoint = lambda x, y: x >= 0 and y >= 0 and math.sqrt(x**2 + y**2) <= 10

decode_id = lambda enc: enc.decode('utf-8')

with navigation_context():
    checksum_components = [
        ord(char) 
        for wid in waypoint_ids 
        for char in decode_id(wid)
        if is_valid_waypoint(*waypoint_coords[waypoint_ids.index(wid)])
    ]
    
    cumulative_distance = sum(
        math.sqrt((waypoint_coords[i][0] - waypoint_coords[i-1][0])**2 + 
                  (waypoint_coords[i][1] - waypoint_coords[i-1][1])**2)
        for i in range(1, len(waypoint_coords))
        if is_valid_waypoint(*waypoint_coords[i]) and is_valid_waypoint(*waypoint_coords[i-1])
    )
    
    final_checksum = sum(checksum_components) + int(cumulative_distance)

print(f"Result: {final_checksum}")