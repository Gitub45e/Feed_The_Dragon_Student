import pygame, random

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
PLAYER_VELOCITY=10
COIN_STARTING_VELOCITY=10
COIN_ACCELERATION=0.9
BUFFER_DISTANCE=200
SCORE_STARTING=0
PLAYER_LIVES=PLAYER_STARTING_LIVES
COIN_VELOCITY=COIN_STARTING_VELOCITY

# Set colors
DARKGREEN=50
GREEN=20
WHITE=255
BLACK=0

# Set fonts
pygame.font.Font()
font_size=45

# Set text
# TODO:
#   - Use your make_text function (or font.render directly) to create:
#       * score_text showing "Score: " + current score, with green color, dark green background color
#       * title_text showing "Feed the Dragon", with green color, white background color
#       * lives_text showing "Lives: " + current lives, with green color, and dark green background color
#   - Get rects for each text surface using .get_rect()
#   - Position:
#       * score_rect at the top-left (e.g., (10, 10))
#       * title_rect centered horizontally at the top
#       * lives_rect at the top-right (e.g., (WINDOW_WIDTH - 10, 10))
score_text= SCORE_STARTING= 1
GREEN=20
DARKGREEN=50
title_text= "Feed the Dragon"
lives_text= "Lives"
get_rect()
score_rect=(20,40)
title_rect= (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
lives_rect= WINDOW_WIDTH



# Set sounds and music
# TODO:
#   - Load sound effects for:
#       * catching a coin (e.g., "assets/coin_sound.wav")
#       * missing a coin (e.g., "assets/miss_sound.wav")
#   - Optionally adjust the miss sound volume using set_volume(...)
#   - Load background music (e.g., "assets/ftd_background_music.wav") using pygame.mixer.music.load(...)


# Set images
# TODO:
#   - Load the player image (dragon) from "assets/dragon_right.png" using pygame.image.load(...)
#   - Get its rect with .get_rect() and:
#       * place it near the left side of the screen
#       * center it vertically in the window
#   - Load the coin image from "assets/coin.png"
#   - Get its rect and:
#       * start it off to the right of the window by BUFFER_DISTANCE
#       * give it a random y-position somewhere between a top margin (like 64) and near the bottom


# The main game loop
pygame.mixer.music.play

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

def tick():
    # TODO:
    #   - Use the clock object to pause just enough so the game runs at FPS frames per second.
    #   - Call clock.tick(FPS)
    pass # TODO: remove this when finished


def is_still_running():
    global running
    for item in pygame.event.get():
        if item.type == pygame.QUIT:
            running = False


def move_player():
    # TODO:
    #   - Get the current state of the keyboard using pygame.key.get_pressed()
    #   - If the up arrow is pressed and the player is not above a top limit (e.g., y > 64),
    #       move the player up by PLAYER_VELOCITY.
    #   - If the down arrow is pressed and the player is not below the bottom of the window,
    #       move the player down by PLAYER_VELOCITY.
    pass # TODO: remove this when finished


def handle_coin():
    # TODO:
    #   - Move the coin to the left each frame by subtracting coin_velocity from coin_rect.x.
    #   - If the coin passes off the left side of the screen (coin_rect.x < 0):
    #       * Subtract 1 from player_lives.
    #       * Play the miss sound.
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: a random integer between a top margin (e.g., 64) and near the bottom edge.
    pass # TODO: remove this when finished


def handle_collisions():
    # TODO:
    #   - Check if the player_rect and coin_rect are colliding using colliderect(...)
    #   - If they collide:
    #       * Increase score by 1
    #       * Play the coin sound
    #       * Increase coin_velocity by COIN_ACCELERATION
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: random integer between the same top and bottom margins
    pass # TODO: remove this when finished


def update_hud():
    # TODO:
    #   - Re-create score_text and lives_text each frame using make_text(...),
    #     so they show the updated score and lives values.
    #   - Remember to use the same font and colors (GREEN and DARKGREEN).
    pass # TODO: remove this when finished


def game_over_check():
    player_lives=0
    update_display()
    while running:
        tick()
        if is_still_running():
            player_lives=PLAYER_LIVES
            update_display()
        is_paused=True
        for item in pygame.event.get():
            if item.type == pygame.QUIT:
                reset_score=0
                reset_player_lives=0
                reset_player_position=0
                reset_player_velocity=0
                reset_player_acceleration=0
                reset_coin_velocity= COIN_STARTING_VELOCITY
                reset_coin_acceleration= COIN_STARTING_VELOCITY
                reset_pygame.music.stop()

def update_screen():
    display_surface.fill(BLACK)
    blit(score_text, (title_text, lives_text), score_rect)
    blit(title_text, (title_text, lives_text), title_rect)
    blit(lives_text, (lives_text, lives_text), lives_rect)
    update_display()
    pygame.display.update()

while running:
    # Main game loop steps:
    #   1. Handle quit events.
    #   2. Move the player based on keyboard input.
    #   3. Move the coin and handle misses.
    #   4. Check for collisions between player and coin.
    #   5. Update the HUD text to match the current score and lives.
    #   6. Check if the game is over and either reset or quit.
    #   7. Draw everything on the screen.
    #   8. Tick the clock to control the frame rate.

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
