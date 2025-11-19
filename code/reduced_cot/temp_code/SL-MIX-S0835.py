class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Position({self.x}, {self.y})"

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.prev = None
        self.next = None

class MovementTracker:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_position(self, pos):
        new_node = Node(pos)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def get_positions(self):
        positions = []
        current = self.head
        while current:
            positions.append(current.pos)
            current = current.next
        return positions

# Arena parameters
ARENA_SIZE = 100

# Robot movement logic
move_robot = lambda dx, dy: lambda pos: Position((pos.x + dx) % ARENA_SIZE, (pos.y + dy) % ARENA_SIZE)

# Initialize tracker and starting position
tracker = MovementTracker()
initial_pos = Position(50, 50)
tracker.add_position(initial_pos)

current_pos = initial_pos
movements = [
    move_robot(15, 25),
    move_robot(-10, 5),
    move_robot(30, -20),
    move_robot(-5, -15),
    move_robot(0, 30)
]

for move in movements:
    current_pos = move(current_pos)
    tracker.add_position(current_pos)

# Calculate heading based on last two positions
last_pos = tracker.tail.pos
second_last_pos = tracker.tail.prev.pos

x_diff = (last_pos.x - second_last_pos.x) % ARENA_SIZE
y_diff = (last_pos.y - second_last_pos.y) % ARENA_SIZE

# Normalize differences to handle wrapping
if x_diff > ARENA_SIZE // 2:
    x_diff -= ARENA_SIZE
if y_diff > ARENA_SIZE // 2:
    y_diff -= ARENA_SIZE

final_heading = (x_diff * 100) + y_diff
print(f"Result: {final_heading}")