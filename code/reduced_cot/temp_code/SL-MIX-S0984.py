from collections import deque
import re

def tokenize_notes(note_string):
    return re.findall(r'[A-G][#b]?[0-9]', note_string)

class Note:
    def __init__(self, name, duration=1):
        self.name = name
        self.duration = duration
    
    def __repr__(self):
        return f"Note({self.name}, {self.duration})"

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def calculate_harmonic_tension(note_stack, harmony_queue):
    # Calculate weighted tension using Fibonacci sequence
    stack_tension = sum(fibonacci(i+1) * ord(note.name[0]) for i, note in enumerate(note_stack))
    queue_tension = sum(fibonacci(i+1) * len(harmony) for i, harmony in enumerate(harmony_queue))
    return stack_tension + queue_tension

def process_composition(composition_string):
    tokens = tokenize_notes(composition_string)
    pending_notes = []  # Stack
    resolved_harmonies = deque()  # Queue
    
    for i, token in enumerate(tokens):
        note = Note(token, duration=(i % 4) + 1)
        pending_notes.append(note)
        
        # Resolve harmonies when we have 3 notes
        if len(pending_notes) >= 3:
            harmony = [pending_notes.pop() for _ in range(3)]
            resolved_harmonies.append(tuple(h.name for h in harmony))
    
    # Any remaining notes form a final harmony
    if pending_notes:
        remaining_names = tuple(note.name for note in pending_notes)
        resolved_harmonies.append(remaining_names)
    
    return pending_notes, resolved_harmonies

composition = "C4 D4 E4 F4 G4 A4 B4 C5 D5 E5"
pending_stack, harmony_queue = process_composition(composition)
final_tension = calculate_harmonic_tension(pending_stack, harmony_queue)
print(f"Result: {final_tension}")