import pygame
from pygame.sprite import Sprite

# class Alien:
# would define a new calss
class Alien(Sprite):
    #Sprite is the superclass that Alien is inheriting properties from 
    """A class to represent a single alien in the fleet."""

    #The constructor:
    # called whenever a new Alien is created.
    # self has to be the first argument
    # of any member method of a class.
    # But when you call the function, say like this:
    # Jerry = Alien('Blue', 'Black screen')
    # You don't write in an argument for 'self'
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        #How to call the constructor for the superclass
        #Make this the first line of a constructor for any subclass!
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    # If someone calls
    # Jerry.blitme()
    # Then this function is run,
    # and the alien is drawn to the screen.
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
