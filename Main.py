
import pygame
import sys
from monster import *


pygame.init()

window = pygame.display.set_mode((320,500))
FLOOR_Y_POS = 0
is_created = False
fps = 5
clock = pygame.time.Clock()


animation_dictionary = {'Attacking': ['monster_attacking1', 'monster_attacking2',
                         'monster_attacking3', 'monster_attacking4'], "Dying" : ['monster_dead1', 'monster_dead2',
                         'monster_dead3', 'monster_dead4', 'monster_dead5', 'monster_dead6', 'monster_dead7',
                          'monster_dead8', 'monster_dead9', 'monster_dead10', 'monster_dead11', 'monster_dead12',
                          'monster_dead13', 'monster_dead14', 'monster_dead15', 'monster_dead16', 'monster_dead17', 
                          'monster_dead18', 'monster_dead19', 'monster_dead20', 'monster_dead21',], 'Jumping' : ['monster_jumping1',
                           'monster_jumping1', 'monster_jumping3', 'monster_jumping4', 'monster_jumping5', 'monster_jumping6',
                           'monster_jumping7', 'monster_jumping8', 'monster_jumping9', 'monster_jumping10', 'monster_jumping11',
                           'monster_jumping12', 'monster_jumping13'], 'Standing' : ['monster_still1', 'monster_still2'],
                            'Damage' : ['monster_taking_damage1', 'monster_taking_damage2', 'monster_taking_damage3',
                             'monster_taking_damage4'], 'Walking' : ['monster_walking1', 'monster_walking2', 
                           'monster_walking4', 'monster_walking5', 'monster_walking6']}







class Scene:

    def __init__(self):
        pass


    def build_floor(self):
        floor = pygame.image.load('./MonsterGame/assets/base.png')
        floor_rect = floor.get_rect(center = (window.get_size()[0]/2, window.get_size()[1]-(floor.get_size()[1])/2))
        window.blit(floor, floor_rect)
        FLOOR_Y_POS = floor.get_size()[1]











while True:
    
    
    if not is_created:
        monster = Monster(FLOOR_Y_POS, animation_dictionary)
        monster.animate('Standing')
        monster2 = Monster(FLOOR_Y_POS, animation_dictionary)
        monster2.animate('Walking')
        is_created = True
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            monster.animation_controller.key_control(event)
           # key_control(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

           
            
                
    monster.draw()
    pygame.display.update()
    clock.tick(fps)
