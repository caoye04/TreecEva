import math
from collections import namedtuple

SignalData = namedtuple('SignalData', ['frequency', 'amplitude', 'phase'])

def analyze_cosmic_signal(signals):
    processed_count = 0
    cosmic_index = 0
    energy_signatures = {1, 2, 4, 8, 16}
    forbidden_frequencies = frozenset([3, 7, 11, 15])
    
    for idx, signal in enumerate(signals):
        if signal.frequency in forbidden_frequencies:
            continue
        
        transformed_freq = signal.frequency % 5
        
        match transformed_freq:
            case 0:
                cosmic_index += int(math.log2(signal.amplitude)) if signal.amplitude > 0 else 0
            case 1 | 4:
                cosmic_index += signal.phase * 2
            case 2:
                if signal.amplitude in energy_signatures:
                    cosmic_index += int(math.log(signal.amplitude))
                else:
                    cosmic_index -= 1
            case _:
                cosmic_index += signal.frequency
        
        processed_count += 1
        if processed_count >= 3:
            break
    
    return cosmic_index

observed_signals = [
    SignalData(frequency=12, amplitude=16, phase=3),
    SignalData(frequency=7, amplitude=8, phase=5),  # Forbidden frequency
    SignalData(frequency=9, amplitude=4, phase=2),
    SignalData(frequency=14, amplitude=32, phase=1),
    SignalData(frequency=5, amplitude=2, phase=4)
]

cosmic_index = analyze_cosmic_signal(observed_signals)
print(f"Result: {cosmic_index}")