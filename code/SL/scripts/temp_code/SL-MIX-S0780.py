import base64
from collections import defaultdict

encoded_logs = [
    b'RVJST1I6IEZhaWxlZCB0byBjb25uZWN0IHRvIGRhdGFiYXNl',
    b'SU5GTzogVXNlciBsb2dnZWQgaW4gc3VjY2Vzc2Z1bGx5',
    b'RVJST1I6IEludmFsaWQgdXNlcm5hbWUgb3IgcGFzc3dvcmQ=',
    b'V0FSTklORzogTG93IGRpc2sgc3BhY2U=',
    b'RVJST1I6IFBlcm1pc3Npb24gZGVuaWVkIGZvciBmaWxl'
]

decoded_patterns = defaultdict(int)
error_count = 0

for log_entry in encoded_logs:
    decoded_str = base64.b64decode(log_entry).decode('utf-8')
    if 'ERROR:' in decoded_str:
        error_count += 1
    parts = decoded_str.split(': ', 1)
    if len(parts) == 2:
        decoded_patterns[parts[0]] += 1

print(f'Result: {error_count}')