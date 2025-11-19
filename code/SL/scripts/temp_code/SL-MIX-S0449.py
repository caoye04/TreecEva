import math

def process_waveform_signal(samples):
    state = 'INIT'
    amplitude_sum = 0
    sample_count = 0
    modulation_index = 13
    
    for i, sample in enumerate(samples):
        if state == 'INIT':
            if sample > 0:
                state = 'ACCUMULATE'
            else:
                continue
        elif state == 'ACCUMULATE':
            amplitude_sum += sample
            sample_count += 1
            if sample_count >= 3:
                state = 'MODULATE'
        elif state == 'MODULATE':
            if sample <= 0:
                break
            amplitude_sum = (amplitude_sum * sample) % modulation_index
            state = 'SCALE' if amplitude_sum > 10 else 'ACCUMULATE'
        elif state == 'SCALE':
            amplitude_sum = int(math.log(amplitude_sum + 1)) if amplitude_sum > 0 else 0
            sample_count = 0
            state = 'ACCUMULATE'
    
    final_adjustment = amplitude_sum if amplitude_sum < 100 else amplitude_sum // 2
    return final_adjustment

digitized_samples = [2, 4, 6, 3, 1, 8, 0, 5, 7]
final_adjustment = process_waveform_signal(digitized_samples)
print(f'Result: {final_adjustment}')