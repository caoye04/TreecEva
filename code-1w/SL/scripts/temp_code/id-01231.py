def analyze_signal(reading):
    base = reading[0] * 2
    offset = sum(reading[1:]) / len(reading[1:])
    return base + offset

readings = [12, 8, 16, 4]
signal_value = analyze_signal(readings)

status_flags = ('critical', 'normal', 'warning')
energy_level = signal_value * 0.75
case_adjusted = tuple(flag.upper() for flag in status_flags)

energy_threshold = int(energy_level - 10)

diagnostics = [energy_threshold + i*5 for i in range(3)]
filter_func = lambda x: x % 2 == 0
diagnostics = list(filter(filter_func, diagnostics))

system_check = lambda pred, vals: all(pred(v) for v in vals)
final_diagnostic = system_check(lambda x: x > energy_threshold, diagnostics)

Result: energy_threshold