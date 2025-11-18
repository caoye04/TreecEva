import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class ParticleSimulator:
    def __init__(self):
        self.energy_level = 100.0
        self.cycle_count = 0
        self.mode = "STABLE"
        self.stability_measure = 0
    
    def transition(self):
        if self.mode == "STABLE":
            if self.energy_level > 150:
                self.mode = "DECAY"
        elif self.mode == "DECAY":
            if self.energy_level < 50:
                self.mode = "RECOVERY"
        elif self.mode == "RECOVERY":
            if self.energy_level > 90:
                self.mode = "STABLE"
    
    def update_energy(self):
        if self.mode == "STABLE":
            self.energy_level *= 1.02
        elif self.mode == "DECAY":
            self.energy_level -= math.log(self.energy_level) * 3
        elif self.mode == "RECOVERY":
            self.energy_level += math.exp(self.energy_level/100) * 0.5
    
    def run_cycle(self):
        self.update_energy()
        self.transition()
        self.cycle_count += 1
        if self.cycle_count % 7 == 0:
            self.stability_measure += 1 if is_prime(int(self.energy_level)) else 0

simulator = ParticleSimulator()

# Run simulation
for _ in range(50):
    simulator.run_cycle()

# Calculate final stability index using number theory
prime_cycles = sum(1 for i in range(1, simulator.cycle_count + 1) if is_prime(i))
stability_index = gcd(simulator.stability_measure * 3 + 7, prime_cycles + simulator.cycle_count)

print(f"Result: {stability_index}")