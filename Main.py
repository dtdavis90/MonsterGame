import pygame
import sys
pygame.init()

window = pygame.display.set_mode((320,500))
FLOOR_Y_POS = 0







class Monster:

    def __init__(self, height, ):
        self.height = height
        self.animation = Animation('a','b')


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
    

    def __init__(self, animation_image_list):
        animation_list = []

        for image in animation_image_list:
            cache = SurfacesCache()
            animation_list.append(cache.get_surface(image))

    def restart_animation():
        comment

    def next_frame():

    def get_current_surface():
        

        







            



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