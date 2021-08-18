playlist = {
    'title': 'Bus',
    'author': 'steve',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5 },
        {'title': 'song3', 'artist': ['red','yellow'], 'duration': 5.5 },
        {'title': 'sadsong', 'artist': ['meow'], 'duration': 2.0 }
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration'
print(total_length
