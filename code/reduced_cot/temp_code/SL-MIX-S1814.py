from functools import reduce

def decode_hex_command(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

def is_valid_command(cmd):
    return cmd.isalpha() and len(cmd) > 3

def transform_score(acc, cmd):
    if is_valid_command(cmd):
        return acc + len(cmd) * 2
    return acc

def process_commands_batch(batch):
    decoded_commands = list(map(decode_hex_command, batch))
    valid_commands = list(filter(is_valid_command, decoded_commands))
    base_score = reduce(transform_score, valid_commands, 0)
    
    # Apply bonus for consecutive valid commands
    bonus = 0
    consecutive_count = 0
    for cmd in decoded_commands:
        if is_valid_command(cmd):
            consecutive_count += 1
            if consecutive_count >= 3:
                bonus += 5
        else:
            consecutive_count = 0
    
    return base_score + bonus

# Encoded command batches
command_batches = [
    ['68656c6c6f', '776f726c64', '707974686f6e'],  # hello, world, python
    ['616263', '78797a', '6465666768'],              # abc, xyz, defgh
    ['636f6465', '74657374', '6169']                 # code, test, ai
]

# Process all batches and accumulate total score
final_protocol_score = 0
for batch in command_batches:
    batch_score = process_commands_batch(batch)
    final_protocol_score += batch_score if batch_score > 10 else 0  # Only count significant batches

print(f"Result: {final_protocol_score}")