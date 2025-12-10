import pygame, random
from pygame.mixer_music import set_volume

# Initialize pygame
pygame.init()
def make_text(font_object, text, color, background_color):
    text_surface = font_object.render(text, True, color)
    text_rect = text_surface.get_rect()

def blit(surface, item, rect):
    surface.blit(item, rect)
    pygame.display.flip()

def fill(surface, color):
    surface.fill(color)
    pygame.display.flip()
    pygame.display.update()

def update_display():
    pygame.display.update()
    pygame.display.flip()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

# Set FPS and clock
FPS = 60
pygame.time.Clock().tick(FPS)

# Set game values
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.9
BUFFER_DISTANCE = 200
SCORE_STARTING = 0
PLAYER_LIVES = PLAYER_STARTING_LIVES
COIN_VELOCITY = COIN_STARTING_VELOCITY

# Set colors
DARKGREEN = 50
GREEN = 20
WHITE = 255
BLACK = 0

# Set fonts
pygame.font.Font()
font_size = 45

# Set text
make_text("Score", WHITE, BLACK, BLACK)
score_rect = font_size * pygame.font.Font(None, font_size)

# Set sounds and music
load_sound(coin_sound)
load_sound(miss_sound)
load_sound("assets/ftd_background_music")
adjust.set_volume()

# Set images

player = player.pygame.image.load("assets/dragon_right.png")
player_rect = player.get_rect()
player_rect.x = 600
player_rect.y = 300
coin = pygame.image.load("assets/coin.png")
coin_rect = coin.get_rect()
BUFFER_DISTANCE
BUFFER_DISTANCE = 200
BUFFER_PADDING = 64

# The main game loop
pygame.mixer.music.play

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

def tick():
 clock.tick(FPS)

def is_still_running():
    global running
    for item in pygame.event.get():
        if item.type == pygame.QUIT:
            running = False

def move_player():
 pygame.key.get_pressed()
up_arrow = y>64
move_player(up_arrow)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
            if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                move_player()

def handle_coin():
    # TODO:
    #   - Move the coin to the left each frame by subtracting coin_velocity from coin_rect.x.
    #   - If the coin passes off the left side of the screen (coin_rect.x < 0):
    #       * Subtract 1 from player_lives.
    #       * Play the miss sound.
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: a random integer between a top margin (e.g., 64) and near the bottom edge.
    pass  # TODO: remove this when finished

def handle_collisions():
    global score, coin_velocity
    if not player_image_react.colliderect(coin_react):
        return
    score += COIN_VELOCITY
    coin_velocity *= COIN_VELOCITY

def update_hud():
    global score, hud_image_react

def game_over_check():
    player_lives = 0
    update_display()
    while running:
        tick()
        if is_still_running():
            player_lives = PLAYER_LIVES
            update_display()
        is_paused = True
        for item in pygame.event.get():
            if item.type == pygame.QUIT:
                reset_score = 0
                reset_player_lives = 0
                reset_player_position = 0
                reset_player_velocity = 0
                reset_player_acceleration = 0
                reset_coin_velocity = COIN_STARTING_VELOCITY
                reset_coin_acceleration = COIN_STARTING_VELOCITY
                reset_pygame.music.stop()

def update_screen():
    display_surface.fill(BLACK)
    blit(score_text, (title_text, lives_text), score_rect)
    blit(title_text, (title_text, lives_text), title_rect)
    blit(lives_text, (lives_text, lives_text), lives_rect)
    update_display()
    pygame.display.update()

while running:
    is_still_running()
    move_player()
    handle_coin()
    handle_collisions()
    update_hud()
    game_over_check()
    update_screen()
    tick()

# End the game
pygame.quit()