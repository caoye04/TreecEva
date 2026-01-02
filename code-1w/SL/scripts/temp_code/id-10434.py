import math

# System telemetry simulation with red herrings
telemetry_data = {
    'sensor_1': 42,
    'sensor_2': 87,
    'checksum_valid': True,
    'uptime_hours': 1024,
    'version': '3.7.1'
}

# Diagnostic rules engine (some unused)
diagnostic_rules = [
    lambda x: x ** 2,
    lambda x: x + 100 if x < 50 else x - 10,
    lambda x: int(math.sqrt(x))
]

# Irrelevant historical metrics (distractor)
historical_metrics = {
    'peak_load': 999,
    'last_failure_code': None,
    'reboot_count': 3,
    'calibration_offset': -42.5
}

# Core system status with meaningful data mixed with noise
system_status = {
    'core_temp': 67,
    'fan_speed_rpm': 2400,
    'voltage_stable': True,
    'pending_updates': [],
    'core_health': 8,
    'diagnostics_enabled': False,
    'cache_level': 'L2'
}

# Decoy function - looks important but unused
def compute_system_score(data):
    score = 0
    for key, value in data.items():
        if isinstance(value, int):
            score += (value % 11) * 3
    return score

# Simulated health multiplier calculation with multiple paths
base_factor = len(telemetry_data)  # 5
offset_correction = sum([7, -2, 4]) // 3  # 3

# Misleading intermediate computation (dead path)
temporary_diagnostic = 0
if system_status['voltage_stable']:
    temporary_diagnostic = 42
    for i in range(3):
        temporary_diagnostic = int(temporary_diagnostic ** 0.5)  # becomes 2

# Unused rule application (distractor logic)
rule_result = 0
for rule in diagnostic_rules[:2]:
    rule_result += rule(base_factor)  # 25 + 105 = 130

# Health multiplier depends on core temp and fan speed
if system_status['core_temp'] > 70:
    health_multiplier = 0.8
elif system_status['fan_speed_rpm'] < 2000:
    health_multiplier = 0.9
else:
    health_multiplier = 1.25  # This will be used

# Red herring: conditional that looks consequential but doesn't affect final result
if 'version' in telemetry_data and telemetry_data['version'].startswith('3'):
    telemetry_data['patch_applied'] = True
    # This does not impact final_diagnostic

# Key statement: determines the final answer
final_diagnostic = system_status.get('core_health', 0) * health_multiplier

print(f"Result: {final_diagnostic}")