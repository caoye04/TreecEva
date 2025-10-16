class JointPositionBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.head = 0
        self.count = 0
    
    def push(self, position):
        self.buffer[self.head] = position
        self.head = (self.head + 1) % self.size
        if self.count < self.size:
            self.count += 1
    
    def get(self, index):
        if index >= self.count:
            return None
        actual_index = (self.head - self.count + index) % self.size
        return self.buffer[actual_index]

def detect_anomaly(buffer_obj):
    if buffer_obj.count < 3:
        return False
    
    for i in range(buffer_obj.count - 2):
        pos1 = buffer_obj.get(i)
        pos2 = buffer_obj.get(i + 1)
        pos3 = buffer_obj.get(i + 2)
        
        if pos1 is not None and pos2 is not None and pos3 is not None:
            # Check for sudden large change followed by correction
            if abs(pos2 - pos1) > 100 and abs(pos3 - pos2) > 100 and abs(pos3 - pos1) < 20:
                return True
    return False

# Initialize robotic arm controller
joint_buffer = JointPositionBuffer(8)

# Simulate joint movements
movements = [10, 15, 22, 145, 28, 33, 31, 160, 35, 40, 38]

for pos in movements:
    joint_buffer.push(pos)

# Maintenance routine
maintenance_flag = 0

with open('maintenance_log.txt', 'w') as log_file:
    if detect_anomaly(joint_buffer):
        maintenance_flag = 1
        log_file.write('Anomaly detected in joint movements\n')
    else:
        log_file.write('No anomalies detected\n')
    
    # Additional diagnostics using itertools
    from itertools import combinations
    
    if joint_buffer.count >= 4:
        positions = [joint_buffer.get(i) for i in range(joint_buffer.count)]
        # Remove None values
        positions = [p for p in positions if p is not None]
        
        # Check all combinations of 3 positions
        for combo in combinations(positions, 3):
            a, b, c = combo
            # Pattern: a -> b -> c where b is midpoint
            if abs((a + c) // 2 - b) < 2:
                maintenance_flag |= 2  # Set second bit
                break
    
    # Check for oscillation pattern
    oscillation_count = 0
    for i in range(joint_buffer.count - 3):
        p1 = joint_buffer.get(i)
        p2 = joint_buffer.get(i + 1)
        p3 = joint_buffer.get(i + 2)
        p4 = joint_buffer.get(i + 3)
        
        if all(p is not None for p in [p1, p2, p3, p4]):
            # Check for oscillation: up, down, up, down or vice versa
            diff1 = p2 - p1
            diff2 = p3 - p2
            diff3 = p4 - p3
            
            if diff1 * diff2 < 0 and diff2 * diff3 < 0:
                oscillation_count += 1
                if oscillation_count >= 2:
                    maintenance_flag |= 4  # Set third bit
                    break

print(f'Result: {maintenance_flag}')