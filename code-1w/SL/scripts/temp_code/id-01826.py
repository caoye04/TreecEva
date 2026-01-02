import math

def analyze_harmonic(signal):
    # Irrelevant harmonic analysis (dead function)
    return sum(math.sin(x * 0.1) for x in range(len(signal)))

def shift_register(values, offset):
    # Distractor: bit manipulation with no effect on main logic
    shifted = []
    for i in range(len(values)):
        shifted.append((values[i] << 2) ^ offset)
    return shifted

def compute_entropy(data):
    # Misleading intermediate: looks important but unused
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

def process_phase(sequence, idx):
    # Core logic embedded in noise
    accumulator = 0
    threshold = 7
    
    # Real logic begins
    for i, val in enumerate(sequence):
        if i == 0:
            accumulator += val * 3
        elif i % 2 == 0 and val > threshold:
            accumulator -= int(math.sqrt(val))
        else:
            accumulator += (val % 4) * (i % 5)
    
    # Conditional expression affecting result
    adjustment = -5 if accumulator > 20 else 8
    
    # Slice-based transformation (relevant)
    segment = sequence[idx:idx+3]
    for j, item in enumerate(segment):
        if j == 1:
            accumulator += item // 2
    
    # Early return red herring – never reached due to logic
    if len(segment) < 2:
        return 0  # dead path
    
    # Final adjustment using bitwise (distractor masking real change)
    dummy_mask = 0xFF
    masked_acc = accumulator & dummy_mask
    
    # Actual final step (non-obvious due to distractions)
    accumulator += adjustment
    
    return accumulator

def main():
    # Initialization with meaningful and irrelevant variables
    base_signal = [2, 7, 16, 3, 9, 12, 4]
    twist_sequence = [x**2 - x for x in base_signal]  # [2, 42, 240, 6, 72, 132, 12]
    
    # Unused transformations (distractors)
    fft_approx = [complex(math.cos(i), math.sin(i)) for i in range(5)]
    checksum = sum(shift_register([1, 2, 3], 4)) % 100
    
    # Key index computed through indirect logic
    pivot_index = len(twist_sequence) // 2  # 3
    
    # Decoy control flow
    if pivot_index < 0 or pivot_index >= len(twist_sequence):
        pivot_index = 0
    
    # Redundant list creation
    temp_grid = [[i+j for j in range(3)] for i in range(3)]
    
    # Core execution point
    phase_output = process_phase(twist_sequence, pivot_index)
    
    # Additional distraction: zip used meaninglessly
    labels = ['A', 'B', 'C']
    for label, val in zip(labels, temp_grid[0]):
        pass  # no effect
    
    # Print required result
    print(f"Result: {phase_output}")

if __name__ == "__main__":
    main()