import sys
import pygame as pg
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from npc import *
from pathfinding import *
from sound import *


class Game:

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.paused = False

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.npc = NPC(self)
        self.pathfinding = PathFinding(self)
        self.sound = Sound(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        self.npc.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.sound.set_volume(0.2)
        self.sound.soundtrack.play()

    def draw(self):
        color2 = (0, 0, 0)
        color = (181, 139, 74)
        self.screen.fill(color)
        self.object_renderer.draw()

        # Зображення 2д варіації гри
        # self.map.draw()
        # self.player.draw()
        # self.npc.draw_ray_cast()

    def toggle_pause(self):
        self.paused = not self.paused
        pg.mouse.set_visible(self.paused)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.toggle_pause()

    def run(self):
        while True:
            self.check_events()
            if not self.paused:
                self.update()
                self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
