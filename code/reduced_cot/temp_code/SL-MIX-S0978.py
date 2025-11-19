def state_transition(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result % 7
    return wrapper

class StateMachine:
    def __init__(self):
        self.state = 0
    
    @state_transition
    def update(self, operand):
        return self.state + operand
    
    def process_sequence(self, operations):
        for i in range(len(operations)):
            inner_result = 0
            for j in range(i+1):
                inner_result += operations[j] if j % 2 == 0 else -operations[j]
            self.state = self.update(inner_result) if inner_result > 0 else self.update(inner_result * -1)
        return self.state

machine = StateMachine()
operation_sequence = [3, 5, 2, 8, 1, 4, 6]
final_state = machine.process_sequence(operation_sequence)
print(f'Result: {final_state}')