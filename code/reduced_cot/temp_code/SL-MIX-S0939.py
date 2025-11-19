from enum import Enum

class DispenserState(Enum):
    IDLE = 0
    SELECTING = 1
    DISPENSING = 2

def operate_dispenser(state_sequence):
    balance_counter = 0
    state_actions = {
        DispenserState.SELECTING: lambda x: x + 5,
        DispenserState.DISPENSING: lambda x: x - 3,
        DispenserState.IDLE: lambda x: 0 if x != 0 else x
    }
    
    for state_str in state_sequence[1:]:
        state = DispenserState[state_str]
        balance_counter = state_actions[state](balance_counter)
    
    return balance_counter

states = ['IDLE', 'SELECTING', 'DISPENSING', 'IDLE', 'SELECTING']
final_balance = operate_dispenser(states)
print(f"Result: {final_balance}")