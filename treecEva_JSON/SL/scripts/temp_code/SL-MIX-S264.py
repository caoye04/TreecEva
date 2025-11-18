import re

def hex_to_decimal_count(hex_ids):
    count = 0
    for hex_id in hex_ids:
        try:
            decimal_value = int(hex_id, 16)
            if re.search(r'\d', str(decimal_value)):
                count += 1
        except ValueError:
            continue
    return count

bird_hex_ids = ['1A3F', 'BEEF', 'DEAD', 'CAFE', '1234', '5678']
migration_count = hex_to_decimal_count(bird_hex_ids)
print(f"Result: {migration_count}")