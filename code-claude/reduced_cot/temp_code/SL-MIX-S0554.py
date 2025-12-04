from collections import defaultdict
import itertools

def analyze_playlist(tracks):
    # Track structure: (name, artist, duration_seconds, play_count, rating)
    genre_mapping = {
        "Artist1": "Rock",
        "Artist2": "Pop",
        "Artist3": "Electronic",
        "Artist4": "Jazz",
        "Artist5": "Classical"
    }
    
    # Count tracks by genre (not used in final calculation)
    genre_counts = defaultdict(int)
    for track in tracks:
        artist = track[1]
        genre = genre_mapping.get(artist, "Unknown")
        genre_counts[genre] += 1
    
    # Create pairs of tracks for analysis
    track_pairs = list(itertools.combinations(tracks, 2))
    pair_count = len(track_pairs)  # Not used in final result
    
    # Filter tracks that meet specific criteria
    filtered_tracks = []
    for track in tracks:
        name, artist, duration, play_count, rating = track
        popularity_score = play_count * rating
        
        # Apply filter criteria
        if duration > 180 and popularity_score > 400:
            filtered_tracks.append(track)
    
    # Calculate total duration of filtered tracks
    total_duration = calculate_total_duration(filtered_tracks)
    
    # This calculation doesn't affect the result
    average_rating = sum(track[4] for track in tracks) / len(tracks) if tracks else 0
    
    return total_duration, genre_counts, average_rating

def calculate_total_duration(track_list):
    # Calculate the total duration with a specific adjustment
    base_duration = sum(track[2] for track in track_list)
    
    # Apply time normalization factor (not really necessary but adds complexity)
    normalization = 0.95 if len(track_list) > 3 else 1.0
    
    # Extra calculation that doesn't affect the result
    max_duration = max([track[2] for track in track_list]) if track_list else 0
    min_duration = min([track[2] for track in track_list]) if track_list else 0
    range_duration = max_duration - min_duration  # Not used
    
    return int(base_duration * normalization)

# Define the playlist data
playlist = [
    ("Song1", "Artist1", 245, 50, 8.5),
    ("Song2", "Artist2", 198, 120, 7.2),
    ("Song3", "Artist3", 320, 30, 9.1),
    ("Song4", "Artist4", 175, 85, 6.8),
    ("Song5", "Artist5", 412, 25, 9.4),
    ("Song6", "Artist1", 203, 95, 8.2)
]

# Process the playlist
total_duration, genres, avg_rating = analyze_playlist(playlist)

# Check which tracks were filtered
filtered_tracks = []
for track in playlist:
    name, artist, duration, play_count, rating = track
    if duration > 180 and play_count * rating > 400:
        filtered_tracks.append(track)

# Recalculate the total duration
total_duration = calculate_total_duration(filtered_tracks)

print(f"Result: {total_duration}")