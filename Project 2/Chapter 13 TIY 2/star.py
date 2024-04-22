import pygame
from pygame.sprite import Sprite
 
class Star(Sprite):
    """A class to represent a single star."""

    def __init__(self, stars_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = stars_game.screen

      
        self.image = pygame.image.load('Chapter 13 TIY 2/images/star.png')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height