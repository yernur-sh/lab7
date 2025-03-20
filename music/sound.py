import pygame

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((960, 600))

songs = [
    '/Users/ernrsahar/Desktop/PP2_projects/lab7/music/Bea Miller.mp3',
    '/Users/ernrsahar/Desktop/PP2_projects/lab7/music/francemusic.mp3',
    '/Users/ernrsahar/Desktop/PP2_projects/lab7/music/Stray.mp3'
]

def load_and_play(song):
    pygame.mixer.music.unload()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

i = 0
paused = False

load_and_play(songs[i])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                load_and_play(songs[i])
                paused = False

            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                load_and_play(songs[i])
                paused = False

            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused

    pygame.display.flip()
