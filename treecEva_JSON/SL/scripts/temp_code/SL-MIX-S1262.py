import heapq
from functools import wraps

def transition_tracker(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.transitions.append((self.current_state, result))
        return result
    return wrapper

class CircuitSimulator:
    def __init__(self):
        self.current_state = 0
        self.transitions = []
        self.signal_queue = []
        self.state_history = set()
    
    @transition_tracker
    def process_signal(self, signal):
        # Priority queue for signal processing
        heapq.heappush(self.signal_queue, (-signal, len(self.transitions)))
        
        # State transition logic
        if signal % 3 == 0:
            self.current_state = (self.current_state + signal) % 7
        elif signal % 3 == 1:
            self.current_state = (self.current_state * 2) % 7
        else:  # signal % 3 == 2
            self.current_state = (self.current_state ^ signal) % 7
            
        self.state_history.add(self.current_state)
        return self.current_state
    
    def run_simulation(self, signals):
        states = []
        for sig in signals:
            new_state = self.process_signal(sig)
            states.append(new_state)
            
            # Early return condition
            if len(self.state_history) > 5:
                break
                
        # Post-processing with binary search pattern
        target = max(states)
        sorted_states = sorted(list(self.state_history))
        left, right = 0, len(sorted_states)-1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_states[mid] == target:
                return mid * 10 + len(self.transitions)
            elif sorted_states[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

def compute_final_identifier(simulator, signals):
    result = simulator.run_simulation(signals)
    # Backtracking to find unique identifier
    id_components = []
    temp_val = result
    
    while temp_val > 0:
        id_components.append(temp_val % 7)
        temp_val //= 7
        
    # Combinatorial calculation using itertools concept
    final_id = sum(id_components[i] * (i + 1) for i in range(len(id_components)))
    return final_id

# Execution
signals_sequence = [4, 7, 2, 9, 1, 8, 3, 6]
simulator = CircuitSimulator()
final_state_id = compute_final_identifier(simulator, signals_sequence)
print(f"Result: {final_state_id}")