import math

def entropy_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.entropy_sum += result if isinstance(result, (int, float)) else 0
        return result
    wrapper.entropy_sum = 0
    return wrapper

class PrimeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    @entropy_tracker
    def compute_entropy(self):
        if self.value <= 1:
            return 0
        # Calculate entropy using logarithmic and number theory functions
        prime_factor_count = sum(1 for i in range(2, int(math.sqrt(self.value)) + 1) if self.value % i == 0 and all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)))
        return math.log2(self.value) * prime_factor_count

# Tree construction
root = PrimeNode(30)
root.left = PrimeNode(15)
root.right = PrimeNode(42)
root.left.left = PrimeNode(10)
root.left.right = PrimeNode(18)
root.right.left = PrimeNode(35)
root.right.right = PrimeNode(77)

def traverse_and_compute(node):
    if not node:
        return
    node.compute_entropy()
    traverse_and_compute(node.left)
    traverse_and_compute(node.right)

traverse_and_compute(root)
accumulated_entropy = root.compute_entropy.entropy_sum
print(f"Result: {accumulated_entropy}")