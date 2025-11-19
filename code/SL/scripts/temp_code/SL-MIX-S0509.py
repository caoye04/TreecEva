import math

def compute_synchronization_signal(base_freqs, phase_offsets):
    sync_metric = 0.0
    harmonics = [2, 3, 5]
    
    for idx, freq in enumerate(base_freqs):
        if freq <= 0:
            continue
        channel_energy = 0.0
        
        for harmonic in harmonics:
            adjusted_freq = freq * harmonic
            phase = phase_offsets[idx] * harmonic
            component = math.sin(adjusted_freq + phase) * math.log(freq + 1)
            channel_energy += component
            
            if component > 1.5:
                sync_metric += component * 0.5
                break
        
        sync_metric += channel_energy * 0.1
        
        if sync_metric > 10.0:
            sync_metric = sync_metric % 7.0
    
    return sync_metric

frequencies = [1.2, 2.5, 0, 4.8, 3.3]
phases = [0.1, 0.4, 0.7, 0.9, 1.2]
sync_metric = compute_synchronization_signal(frequencies, phases)
sync_metric = round(sync_metric, 6)
print(f"Result: {sync_metric}")