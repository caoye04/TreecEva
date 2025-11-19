from functools import reduce

def beats_to_seconds(beats):
    return beats * 0.5  # At 120 BPM, 1 beat = 0.5 seconds

note_durations = [1, 2, 1.5, 0.5, 3, 1]
valid_notes = filter(lambda x: x > 0 and x <= 4, note_durations)  # Short-circuit: only process valid note durations
processed_times = map(beats_to_seconds, valid_notes)
total_duration = reduce(lambda a, b: a + b, processed_times, 0)

print(f"Result: {total_duration}")