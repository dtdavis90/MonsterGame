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

    # def draw_monster(self):
    #     self.animation.next()
    #     surface = self.animation.get()
    #     rect = surface.get_rect .....
    #     blit
    #class surfacse:

    #def get_surface(image):
        #




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