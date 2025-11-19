class FabricNode:
    def __init__(self, color_code):
        self.color_code = color_code
        self.prev = None
        self.next = None

# Initialize doubly-linked list with fabric color codes
head = FabricNode(18)
node2 = FabricNode(7)
node3 = FabricNode(23)
node4 = FabricNode(4)
node5 = FabricNode(15)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

def rotate_bits_left(value, positions):
    return ((value << positions) | (value >> (8 - positions))) & 0xFF

def process_fabric_sequence(start_node):
    current = start_node
    color_values = []
    while current:
        # Apply bit rotation based on node position
        position = 1 if current.prev is None else (2 if current.next is None else 3)
        rotated = rotate_bits_left(current.color_code, position)
        color_values.append(rotated)
        current = current.next
    return color_values

# Stage 1: Process fabric sequence
processed_colors = process_fabric_sequence(head)

# Stage 2: Apply filtering and transformation
filtered_colors = list(filter(lambda x: x & 0x0F != 0, processed_colors))
transformed_colors = list(map(lambda x: (x ^ 0x55) & 0xFF, filtered_colors))

# Stage 3: Encode into pattern matrix
pattern_matrix = [[0 for _ in range(4)] for _ in range(4)]
for i in range(min(len(transformed_colors), 4)):
    pattern_matrix[i][i] = transformed_colors[i]

# Stage 4: Apply switch-based weaving logic
def apply_weaving_pattern(matrix):
    weave_code = 0
    for i in range(4):
        for j in range(4):
            value = matrix[i][j]
            # Switch/case logic for weaving pattern determination
            if value == 0:
                weave_code += 0
            elif 1 <= value <= 32:
                weave_type = value % 4
                if weave_type == 0:
                    weave_code += value << 1
                elif weave_type == 1:
                    weave_code += value << 2
                elif weave_type == 2:
                    weave_code += value << 3
                else:  # weave_type == 3
                    weave_code += value
            else:
                weave_code += value & 0x0F
    return weave_code

# Stage 5: Final encoding
final_weave_code = apply_weaving_pattern(pattern_matrix)

print(f"Result: {final_weave_code}")