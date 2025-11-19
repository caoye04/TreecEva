class SensorNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_sensor_list(values):
    if not values:
        return None
    head = SensorNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SensorNode(val)
        current = current.next
    return head

def max_consecutive_product(head):
    if not head or not head.next or not head.next.next:
        return 0
    
    max_product = float('-inf')
    first = head
    second = head.next
    third = head.next.next
    
    while third:
        product = first.value * second.value * third.value
        if product > max_product:
            max_product = product
        first = second
        second = third
        third = third.next
        if max_product > 1000:  # Early termination condition
            break
    
    return max_product

# Sensor readings
readings = [2, -3, 4, -1, 2, 1, -5, 4]
sensor_list = build_sensor_list(readings)
max_product = max_consecutive_product(sensor_list)
print(f"Result: {max_product}")