lyricfile = open('lyrics.txt', 'r')

lyrics = lyricfile.read();

lyrics = lyrics.split('$lyrics-body">')

lyrics = lyrics[1].split('</span><span data-reactid="')

print lyrics[0]
