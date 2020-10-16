import pygame
from animation_controller import AnimationController

window = pygame.display.set_mode((320,500))

class Monster:

    def __init__(self, height, animation_dictionary):
        #monster should not be initialized with this dictionary, causes issues when creating a second monster with same dictionary
        
        self.height = height
        self.animation_dictionary = animation_dictionary
        print(f'controller id: {AnimationController(self.animation_dictionary)}')
        self.animation_controller = AnimationController(self.animation_dictionary)
        


    def animate(self, animation_name):
        self.animation_controller.set_animation(animation_name)
        


    def draw(self):
        
        
        monster_surface = self.animation_controller.next_frame()
        monster_rect = monster_surface.get_rect(center = (100, (int(window.get_size()[1]/2))-self.height))
        window.blit(monster_surface, monster_rect)

        