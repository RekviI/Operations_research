import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.game_over_image = self.get_texture('resources/textures/Lost1.png', RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        # floor_texture = self.get_texture('resources/textures/Egypt floor.png', (WIDTH, HEIGHT - HALF_HEIGHT))
        # self.screen.blit(floor_texture, (0, HALF_HEIGHT))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT - HALF_HEIGHT))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/Egypt walls.png')
        }
