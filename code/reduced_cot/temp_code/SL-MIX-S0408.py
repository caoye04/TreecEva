from collections import defaultdict

def get_state_code(state):
    state_codes = {'IDLE': 100, 'HEATING': 200, 'PROCESSING': 300, 'COOLING': 400, 'ERROR': 900}
    return state_codes.get(state, 0)

def process_reactor_events(initial_state, events):
    state = initial_state
    for event in events:
        if state == 'IDLE' and event == 'START_HEAT':
            state = 'HEATING'
        elif state == 'HEATING' and event == 'TEMP_REACHED':
            state = 'PROCESSING'
        elif state == 'PROCESSING' and event == 'PROCESS_DONE':
            state = 'COOLING'
        elif state == 'COOLING' and event == 'COOL_REACHED':
            state = 'IDLE'
        elif not (state == 'IDLE' and event == 'START_HEAT') and \
             not (state == 'HEATING' and event == 'TEMP_REACHED') and \
             not (state == 'PROCESSING' and event == 'PROCESS_DONE') and \
             not (state == 'COOLING' and event == 'COOL_REACHED'):
            state = 'ERROR'
            break
    return state

events_sequence = ['START_HEAT', 'TEMP_REACHED', 'PROCESS_DONE', 'COOL_REACHED']
initial_reactor_state = 'IDLE'

final_reactor_state = process_reactor_events(initial_reactor_state, events_sequence)
final_reactor_state_code = get_state_code(final_reactor_state)

print(f"Result: {final_reactor_state_code}")