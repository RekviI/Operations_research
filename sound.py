import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/Baldur_s_Gate_3_OST_Freedom_Flight.mp3'
        self.soundtrack = pg.mixer.Sound(self.path)

    def set_volume(self, volume):
        # Ensure volume is within the valid range [0.0, 1.0]
        volume = max(0.0, min(1.0, volume))
        self.soundtrack.set_volume(volume)
