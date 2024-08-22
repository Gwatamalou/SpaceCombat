import glob

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_TITLE = 'Space_Combat'

CHARACTER_SCALING = 1

PLAYER_MOVEMENT_SPEED = 5
LASER_SPEAD = 10
LASER_GENERATION_INTERVAL = 0.2

PLAYER = glob.glob('player/*')
METEOR = glob.glob('meteor/*')
LASER = glob.glob('laser/*')
