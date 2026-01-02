system_active = True
safety_margin = 1.05
base_levels = [85, 90, 95, 100]
adjusted_levels = [int(level * safety_margin) for level in base_levels]
standby_levels = [level - 10 for level in adjusted_levels if level > 95]
operational_levels = [level for level in adjusted_levels if level >= 90]

diagnostic_mode = False
buffer_zone = 5
energy_threshold = min(operational_levels) if system_active else max(standby_levels)

Result: energy_threshold