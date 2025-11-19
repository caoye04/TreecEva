from itertools import permutations

class Dispenser:
    def __init__(self):
        self.state = 'IDLE'
        self.flavors = ['orange', 'lemon', 'berry']
        self.permutation_count = 0
    
    def dispense(self):
        if self.state == 'IDLE':
            self.state = 'ACTIVE'
            perms = list(permutations(self.flavors, 2))
            self.permutation_count = len(perms)
        return self.permutation_count

dispenser = Dispenser()
final_combinations = dispenser.dispense()
print(f'Result: {final_combinations}')