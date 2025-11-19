import math
phase_changes = {t: math.sin(t * 0.1) for t in range(1, 11)}
cumulative_sum = lambda d: {k: sum(list(d.values())[:i+1]) for i, k in enumerate(d.keys())}
cumulative_phases = cumulative_sum(phase_changes)
final_phase = cumulative_phases[10] % (2 * math.pi)
print(f'Result: {final_phase}')