import pygame
import sys
pygame.init()

window = pygame.display.set_mode((320,500))
FLOOR_Y_POS = 0







class Monster:

    def __init__(self, height, ):
        self.height = height
        self.animation = Animation()


    def create_monster(self):
   
        monster_surface = pygame.image.load('./assets/monster.png')
        #monster_surface = surfaces.get_surface('./assets/monster.png')
        monster_rect = monster_surface.get_rect(center = (100, window.get_size()[1]-self.height - 5))
        window.blit(monster_surface, monster_rect)












class SurfacesCache():

    image_dictionary = {}
    
    def get_surface(self, image_name):
        # if image_name is not found, load and add to dictionary, then return associated surface object(.png)
        if image_name not in self.image_dictionary:
            image_surface = pygame.image.load(f'./assets/{image_name}.png')
            self.image_dictionary[image_name] = image_surface

        return self.image_dictionary[image_name]






class Animation:
    
    def __init__(self, image_names_list):
        self.animation_list = []
        self.index = 0
        self.cache = SurfacesCache()

        for image in image_names_list:
            self.animation_list.append(self.cache.get_surface(image))


    def restart_animation(self):
        self.index = 0


    def next_frame(self):

        if self.index + 1 > len(self.animation_list) - 1:
            self.restart_animation()
        return self.animation_list[self.index]


    def get_current_surface(self):

        return self.cache.get_surface(self.animation_list[self.index])

        





class AnimationController():
    
    monster_animation_dictionary = {}

    def __init__(self, animation_dictionary):

       for animation_name in animation_dictionary:
            animation_list = animation_dictionary[animation_name]
            self.animation_instance = Animation(animation_list)
            self.monster_animation_dictionary[animation_name] = self.animation_instance

    
    def set_animation(self, animation_name):
        monster_animation_dictionary = self.monster_animation_dictionary

        if animation_name in monster_animation_dictionary:
            return monster_animation_dictionary[animation_name]  
        else:
            raise ValueError(f'Animation {animation_name} not found')
            #TO DO -- set index of current animation to 0
        
    def next_frame(self):
        # TO DO -- grab correct animation_instance
        return self.animation_instance.next_frame()
    









def build_floor():
    global FLOOR_Y_POS
    floor = pygame.image.load('./assets/base.png')
    floor_rect = floor.get_rect(center = (window.get_size()[0]/2, window.get_size()[1]-(floor.get_size()[1])/2))
    window.blit(floor, floor_rect)
    FLOOR_Y_POS = floor.get_size()[1]



while True:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    build_floor()
    monster = Monster(FLOOR_Y_POS)
    monster.create_monster()


    pygame.display.update()