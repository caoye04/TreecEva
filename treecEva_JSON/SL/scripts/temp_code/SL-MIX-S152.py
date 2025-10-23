encoding_map = {
    'alpha': 0x4D,
    'beta': 0x7A,
    'gamma': 0x5F,
    'delta': 0x6B
}

decoding_ops = [
    lambda x: (x >> 2) & 0xFF,
    lambda x: x ^ 0x3C,
    lambda x: (x * 3) % 256
]

def telemetry_decoder(value, stage):
    return decoding_ops[stage](value)

sensor_data = [encoding_map[k] for k in ['alpha', 'gamma', 'beta', 'delta']]

accumulated_value = 0
for idx, encoded in enumerate(sensor_data):
    stage_one = telemetry_decoder(encoded, 0)
    stage_two = telemetry_decoder(stage_one, 1)
    stage_three = telemetry_decoder(stage_two, 2)
    accumulated_value = (accumulated_value << 8) | stage_three

final_telemetry_value = sum([
    (accumulated_value >> (i * 8)) & 0xFF
    for i in range(4)
])

print(f"Result: {final_telemetry_value}")