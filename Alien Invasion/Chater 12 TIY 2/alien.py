import pygame
 
class Alien:
    """A class to manage the bird."""
 
    def __init__(self, alien_game):
        """Initialize the bird and set its starting position."""
        self.screen = alien_game.screen
        self.screen_rect = alien_game.screen.get_rect()

        # Load the Alien image and get its rect.
    
        self.image = pygame.image.load('Chater 12 TIY 2/images/Alienship.bmp')
        self.rect = self.image.get_rect()

        # Start each new Alien at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the Alien at its current location."""
        self.screen.blit(self.image, self.rect)