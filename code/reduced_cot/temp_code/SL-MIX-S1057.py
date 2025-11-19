import itertools

class FitnessDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, chromosome):
        base_fitness = self.func(chromosome)
        # Apply bitwise adjustment: XOR with mask 0b1101 then right shift 2
        adjusted = (base_fitness ^ 0b1101) >> 2
        return adjusted

@FitnessDecorator
def calculate_base_fitness(chromosome):
    return sum(chromosome) * 3

class ChromosomeNode:
    def __init__(self, genes, left=None, right=None):
        self.genes = genes
        self.left = left
        self.right = right
        self.fitness = 0

def dfs_traverse_and_score(node):
    if not node:
        return 0
    node.fitness = calculate_base_fitness(node.genes)
    left_score = dfs_traverse_and_score(node.left)
    right_score = dfs_traverse_and_score(node.right)
    return node.fitness + left_score + right_score

# Build binary tree
root = ChromosomeNode([1, 0, 1, 1])
root.left = ChromosomeNode([0, 1, 1, 0])
root.right = ChromosomeNode([1, 1, 0, 0])
root.left.left = ChromosomeNode([1, 0, 0, 1])
root.left.right = ChromosomeNode([0, 0, 1, 1])

# Process tree and accumulate adjusted fitness values
stack = [root]
cumulative_adjusted_fitness = 0

while stack:
    current = stack.pop()
    if current:
        raw_fitness = calculate_base_fitness(current.genes)
        cumulative_adjusted_fitness += raw_fitness
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

print(f"Result: {cumulative_adjusted_fitness}")