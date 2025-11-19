from collections import deque

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

# City block coordinates
blocks = [Block(0, 0), Block(0, 3), Block(3, 0), Block(3, 3), Block(1, 1), Block(2, 2)]

# Sort blocks by x+y descending to prioritize corners in our greedy approach
blocks.sort(key=lambda b: b.x + b.y, reverse=True)

park_locations = []
covered = set()

# Process blocks using a queue
block_queue = deque(blocks)

while block_queue:
    current_block = block_queue.popleft()
    # Check if already covered
    covered_flag = False
    for park in park_locations:
        if current_block.manhattan_distance(park) <= 2:
            covered_flag = True
            break
    
    if not covered_flag:
        # Place a new park at the current block location (greedy choice)
        park_locations.append(Block(current_block.x, current_block.y))
        # Mark all nearby blocks as covered
        for block in blocks:
            if current_block.manhattan_distance(block) <= 2:
                covered.add((block.x, block.y))

# Count the parks
minimum_parks_needed = len(park_locations)
print(f"Result: {minimum_parks_needed}")