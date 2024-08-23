import random
import arcade
from  constants import *


class Entity(arcade.Sprite):
    def __init__(self, sprites, center_x=0, center_y=0, change_x=0, change_y=0, bottom=None):
        super().__init__()
        self.sprites = arcade.Sprite(sprites, CHARACTER_SCALING)
        self.sprites.change_x = change_x
        self.sprites.change_y = change_y
        self.sprites.center_x = center_x
        self.sprites.center_y = center_y
        if bottom: self.sprites.bottom = bottom


class MyGame(arcade.View):

    def __init__(self):
        super().__init__()

        self.player = None
        self.scene = None
        self.player_list = []
        self.meteor_list = []
        self.laser_list = []
        self.star_list = []
        self.physics_engine = None
        self.last_laser_time = 0
        arcade.set_background_color((4, 10, 20))

    def setup(self):
        self.scene = arcade.Scene()

        self.scene.add_sprite_list('Star', use_spatial_hash=True)
        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Meteor', use_spatial_hash=True)
        self.scene.add_sprite_list('Laser', use_spatial_hash=True)

        self.player_list.extend(PLAYER)
        self.meteor_list.extend(METEOR)
        self.laser_list.extend(LASER)
        self.star_list.extend(STAR)

        self.player_setup()

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def player_setup(self):
        self.player = Entity(self.player_list[0], 300, 50)
        self.scene.add_sprite('Player', self.player.sprites)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, None)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprites.change_x = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprites.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprites.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprites.change_x = 0

    def generate_star(self):
        star_sprite = Entity(self.star_list[random.randrange(0, len(self.star_list) - 1)],
                                  center_x=random.randint(0, 600),
                                  center_y=850,
                                  change_y=-(15))
        self.scene.add_sprite('Star', star_sprite.sprites)

    def generate_laser(self):
        laser  = Entity(self.laser_list[0],
                             center_x=self.player.sprites.center_x,
                             change_y=LASER_SPEAD,
                             bottom=self.player.sprites.top)
        self.scene.add_sprite('Laser', laser.sprites)

    def generate_meteor(self):
        meteor_sprite = Entity(self.meteor_list[random.randrange(0, len(self.meteor_list) - 1)],
                               center_x=random.randint(0, 600),
                               center_y=850,
                               change_y=-(random.randint(1, 6)),
                               change_x=random.randint(-3, 3))
        self.scene.add_sprite('Meteor', meteor_sprite.sprites)

    def dell_entity(self):
        for laser in self.scene['Laser']:
            hit_list = arcade.check_for_collision_with_list(laser, self.scene['Meteor'])
            if hit_list:
                laser.remove_from_sprite_lists()
            for meteor_sprite in hit_list:
                meteor_sprite.remove_from_sprite_lists()
            if laser.bottom > 800: laser.remove_from_sprite_lists()

        for meteor_sprite in self.scene['Meteor']:
            if meteor_sprite.top < 0:
                meteor_sprite.remove_from_sprite_lists()

        for star_sprite in self.scene['Star']:
            if star_sprite.top < 0:
                star_sprite.remove_from_sprite_lists()

    def on_update(self, delta_time):
        self.scene.update()
        self.physics_engine.update()

        self.last_laser_time += delta_time
        if self.last_laser_time > LASER_GENERATION_INTERVAL:
            self.generate_laser()
            self.last_laser_time = 0

        if random.random() < 0.15:
            self.generate_meteor()

        if random.random() < 0.5:
            self.generate_star()

        self.dell_entity()
