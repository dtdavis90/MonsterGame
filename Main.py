import pygame
import sys
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




class Monster:

    def __init__(self, height, animation_dictionary):
        #monster should not be initialized with this dictionary, causes issues when creating a second monster with same dictionary
        self.height = height
        self.animation_dictionary = animation_dictionary
        self.animation_controller = AnimationController(self.animation_dictionary)
        


    def animate(self, animation_name):
        self.animation_controller.set_animation(animation_name)
        


    def draw(self):
        
        
        monster_surface = self.animation_controller.next_frame()
        monster_rect = monster_surface.get_rect(center = (100, (int(window.get_size()[1]/2))-self.height))
        window.blit(monster_surface, monster_rect)

        



class SurfacesCacheSingleton():

    image_dictionary = {}
    _instance = None

    def __init__(self):
        if SurfacesCacheSingleton._instance is not None:
            raise Exception("Failed to make multiple instances of SurfacesCacheSingleton")
        else:
            SurfacesCacheSingleton._instance = self
        

    @staticmethod
    def get_cache_instance():
        if SurfacesCacheSingleton._instance is None:
            SurfacesCacheSingleton()
        return SurfacesCacheSingleton._instance
    
    def get_surface(self, image_name):
        # if image_name is not found, load and add to dictionary, then return associated surface object(.png)
        if image_name not in self.image_dictionary:
            image_surface = pygame.image.load(f'./MonsterGame/assets/{image_name}.png')
            self.image_dictionary[image_name] = image_surface
            #f'./assets/{image_name}.png'

        return self.image_dictionary[image_name]

    
   

class Animation:
    
    def __init__(self, image_names_list):

        self.animation_list = []
        self.index = 0
        self.cache = SurfacesCacheSingleton.get_cache_instance()

        for image in image_names_list:
            self.animation_list.append(self.cache.get_surface(image))
            


    def restart_animation(self):

        self.index = 0


    def next_frame(self):
        self.index += 1
        if self.index > len(self.animation_list) - 1:
            self.restart_animation()
        
        return self.animation_list[self.index]


    def get_current_surface(self):

        return self.cache.get_surface(self.animation_list[self.index])

        

class AnimationController():
    
    def __init__(self, animation_dictionary):
        self.monster_animation_dictionary = animation_dictionary
        self.current_animation_list = []
        self.current_animation_name = ""
        self.key_list = []

        for animation_name in animation_dictionary:
            animation_list = animation_dictionary[animation_name]
            self.animation_instance = Animation(animation_list)
            self.monster_animation_dictionary[animation_name] = self.animation_instance
        
        self.key_list = list(self.monster_animation_dictionary)
        
        

    
    def set_animation(self, animation_name):

        if animation_name in self.monster_animation_dictionary:
            self.current_animation_list =  self.monster_animation_dictionary[animation_name]
            self.current_animation_name = animation_name  

        else:
            raise ValueError(f'Animation {animation_name} not found')
            
        
    def next_frame(self):
        #current_animation_list is an Animation object
        return self.current_animation_list.next_frame()

    def next_animation(self):
        index = self.key_list.index(self.current_animation_name)
        if index >= len(self.key_list) - 1:
            index = -1
        self.current_animation_list = self.monster_animation_dictionary[self.key_list[index+1]]
        self.current_animation_name = self.key_list[index+1]

    def key_control(self, event):
        if event.key == pygame.K_w:
            self.next_animation()
    

    


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
        # monster2 = Monster(FLOOR_Y_POS, animation_dictionary)
        # monster2.animate('Walking')
        is_created = True
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            monster.animation_controller.key_control(event)
           # key_control(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

           
            
                

    #build_floor()
    monster.draw()
    #monster2.draw()
    pygame.display.update()
    clock.tick(fps)