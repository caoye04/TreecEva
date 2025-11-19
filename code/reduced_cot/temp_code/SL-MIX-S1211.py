readings = ['0x1F3', '0xA2B', '0x4C9', '0x7E4']
values = [int(r, 16) for r in readings]
tokens = [v % 256 for v in values]
checksum = 0
for i, t in enumerate(tokens):
    if i % 2 == 0:
        checksum = (checksum + t * 3) % 1000
    else:
        checksum = (checksum ^ t) % 1000
mod_result = checksum % 100
final_adjustment = (mod_result * 7 + 13) % 100
current_checksum = (checksum + final_adjustment) % 1000
checksum = current_checksum
print(f"Result: {checksum}")