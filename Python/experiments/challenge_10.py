def play_next(playlist, song_title):
    playlist.insert(1, song_title)
    return playlist

my_playlist = ['Song A', 'Song B', 'Song C']
new_song = input('Enter the song name to add to the queue: ').strip()

updated_playlist = play_next(my_playlist, new_song)
formatted_songs = ', '.join(f'{song}' for song in updated_playlist)

print(f'Song added to queue: {new_song}\n'
      f'Updated playlist: {formatted_songs}')
