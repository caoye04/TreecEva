from collections import defaultdict

def decode_hex_command(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

def process_commands(cmd_list):
    state_machine = defaultdict(int)
    current_state = 'IDLE'
    state_machine[current_state] = 1
    
    for hex_cmd in cmd_list:
        try:
            cmd = decode_hex_command(hex_cmd)
        except:
            continue  # Skip invalid commands
            
        if current_state == 'IDLE' and cmd == 'CONNECT':
            current_state = 'ACTIVE'
            state_machine[current_state] += 1
        elif current_state == 'ACTIVE' and cmd == 'AUTH':
            current_state = 'AUTHORIZED'
            state_machine[current_state] += 2
        elif current_state == 'AUTHORIZED' and cmd == 'EXEC':
            current_state = 'ALERT'
            state_machine[current_state] += 3
        elif current_state == 'ALERT' and cmd == 'RESET':
            current_state = 'IDLE'
            state_machine[current_state] += 1
        else:
            state_machine['ERROR'] += 1
    
    return state_machine

network_commands = ['434F4E4E454354', '41555448', '45584543', '5245534554', '434F4E4E454354', '41555448', '45584543']
final_state_counts = process_commands(network_commands)
print(f"Result: {final_state_counts['ALERT']}")