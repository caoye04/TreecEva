class SensorNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_linked_list(values):
    if not values:
        return None
    head = SensorNode(values[0])
    current = head
    for v in values[1:]:
        current.next = SensorNode(v)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def sliding_window_xor(seq, window_size=3):
    n = len(seq)
    if n < window_size:
        return [0] * n
    result = []
    for i in range(n - window_size + 1):
        xor_val = 0
        for j in range(window_size):
            xor_val ^= seq[i + j]
        result.append(xor_val)
    return result + [0] * (window_size - 1)

def compute_coherence(seq_a, seq_b):
    if len(seq_a) != len(seq_b):
        return 0
    n = len(seq_a)
    total = 0
    for i in range(n):
        total += (seq_a[i] ^ seq_b[i]) * (n - i)
    return total

# Sensor data
sensor1_raw = [15, 7, 3, 12, 9, 6]
sensor2_raw = [8, 11, 5, 14, 2, 13]
sensor3_raw = [4, 1, 10, 16, 7, 5]

# Build linked lists for each sensor
sensor1_ll = build_linked_list(sensor1_raw)
sensor2_ll = build_linked_list(sensor2_raw)
sensor3_ll = build_linked_list(sensor3_raw)

# Convert back to lists (simulating data retrieval)
sensor1_data = linked_list_to_list(sensor1_ll)
sensor2_data = linked_list_to_list(sensor2_ll)
sensor3_data = linked_list_to_list(sensor3_ll)

# Apply sliding window XOR transformation
transformed_s1 = sliding_window_xor(sensor1_data)
transformed_s2 = sliding_window_xor(sensor2_data)
transformed_s3 = sliding_window_xor(sensor3_data)

# Store transformed data in a hash table
processed_data = {
    'sensor_1': transformed_s1,
    'sensor_2': transformed_s2,
    'sensor_3': transformed_s3
}

# Calculate coherence metrics
coherences = {}
sensor_keys = list(processed_data.keys())
for i in range(len(sensor_keys)):
    for j in range(i+1, len(sensor_keys)):
        key_pair = f"{sensor_keys[i]}_{sensor_keys[j]}"
        coherences[key_pair] = compute_coherence(processed_data[sensor_keys[i]], processed_data[sensor_keys[j]])

# Find minimum coherence
min_coherence = min(coherences.values())

# Calculate final metric using list comprehension and lambda
adjustment_factors = [(lambda x: x * 2 if x % 2 == 0 else x + 1)(i) for i in range(len(coherences))]
final_metric = min_coherence + sum(adjustment_factors)

print(f"Result: {final_metric}")