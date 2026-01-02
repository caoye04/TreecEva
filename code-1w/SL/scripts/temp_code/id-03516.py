system_load = 987
base_offset = 42
phase_map = {1: 3, 2: 7, 3: 5}
status_flag = 3

temp = base_offset * 2
status_flag = (system_load + temp) % 3 + 1
if status_flag in phase_map:
    adjusted = system_load // phase_map[status_flag]
    system_load -= adjusted

final_load = system_load % phase_map[status_flag]
print(f"Result: {final_load}")