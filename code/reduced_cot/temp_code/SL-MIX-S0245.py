class SensorNode:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

def build_sensor_list(readings):
    head = None
    current = None
    for i, val in enumerate(readings):
        node = SensorNode(val, i+1)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head

def decode_value(node):
    key = (node.position << 2) & 0xFF
    return node.value ^ key

def compute_checksum_divide_conquer(nodes_list):
    if not nodes_list:
        return 0
    if len(nodes_list) == 1:
        return decode_value(nodes_list[0])
    mid = len(nodes_list) // 2
    left_checksum = compute_checksum_divide_conquer(nodes_list[:mid])
    right_checksum = compute_checksum_divide_conquer(nodes_list[mid:])
    return (left_checksum + right_checksum) & 0xFF

def collect_nodes(head):
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    return nodes

def main():
    sensor_readings = [0x3C, 0x7A, 0x5F, 0x1D, 0x9B]
    sensor_head = build_sensor_list(sensor_readings)
    node_collection = collect_nodes(sensor_head)
    final_checksum = compute_checksum_divide_conquer(node_collection)
    print(f"Result: {final_checksum}")

if __name__ == "__main__":
    main()