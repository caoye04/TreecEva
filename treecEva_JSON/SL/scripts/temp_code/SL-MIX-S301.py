import collections
import math

class SignalProcessor:
    def __init__(self):
        self.stack = collections.deque()
        self.accumulator = 0
        self.transform_map = {}
    
    def load_signal(self, value):
        self.stack.append(value)
    
    def apply_transform(self, opcode):
        if opcode == 0b1010 and len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            result = (a ^ b) & 0xFF
            self.stack.append(result)
        elif opcode == 0b0101 and self.stack:
            val = self.stack[-1]
            shifted = (val << 2) | (val >> 6)
            self.stack[-1] = shifted & 0xFF
        elif opcode == 0b1111 and self.stack:
            val = self.stack.pop()
            adjusted = math.floor(val * 1.618)  # Golden ratio
            self.accumulator += adjusted
    
    def synchronize(self):
        temp_sum = sum(list(self.stack)[:3]) if len(self.stack) >= 3 else sum(self.stack)
        self.accumulator ^= temp_sum
        return self.accumulator

def build_operation_tree():
    # Binary tree represented as [root, left, right, left-left, left-right, ...]
    return [0b1010, 0b0101, 0b1111, 0b1010, 0b0101, None, None]

def process_signals():
    processor = SignalProcessor()
    ops_tree = build_operation_tree()
    
    # Load initial signals
    signals = [42, 18, 73, 29, 55]
    for sig in signals:
        processor.load_signal(sig)
    
    # Process according to tree - level order traversal
    queue = collections.deque([0])  # Start with root index
    
    while queue and processor.stack:
        idx = queue.popleft()
        if idx < len(ops_tree) and ops_tree[idx] is not None:
            opcode = ops_tree[idx]
            processor.apply_transform(opcode)
            
            # Add children to queue if they exist
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            if left_child < len(ops_tree) and ops_tree[left_child] is not None:
                queue.append(left_child)
            if right_child < len(ops_tree) and ops_tree[right_child] is not None:
                queue.append(right_child)
    
    # Final synchronization step
    final_value = processor.synchronize()
    return final_value

# Execute processing pipeline
final_accumulator = process_signals()
print(f"Result: {final_accumulator}")