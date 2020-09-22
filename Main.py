import pygame
import sys
pygame.init()

window = pygame.display.set_mode((320,500))
FLOOR_Y_POS = 0
is_alive = False
fps = 5
clock = pygame.time.Clock()


animation_dictionary = {'Attacking': ['monster_attacking1', 'monster_attacking2',
                         'monster_attacking3', 'monster_attacking4'], "Dying" : ['monster_dead1', 'monster_dead2',
                         'monster_dead3', 'monster_dead4', 'monster_dead5', 'monster_dead6', 'monster_dead7',
                          'monster_dead8', 'monster_dead9', 'monster_dead10', 'monster_dead11', 'monster_dead12',
                          'monster_dead13', 'monster_dead14', 'monster_dead15', 'monster_dead16', 'monster_dead17', 
                          'monster_dead18', 'monster_dead19', 'monster_dead20', 'monster_dead21']}




class Monster:

    def __init__(self, height, animation_dictionary):
        self.height = height
        self.animation_dictionary = animation_dictionary
        #self.animation = Animation()
        self.animation_controller = AnimationController(self.animation_dictionary)
        


    def create_monster(self):
        print("test")
        
        # monster_surface = pygame.image.load('./assets/monster.png')
        # monster_surface = surfaces.get_surface('./assets/monster.png')
        # monster_rect = monster_surface.get_rect(center = (100, window.get_size()[1]-self.height - 5))
        # window.blit(monster_surface, monster_rect)

    def draw(self):
        
        
        monster_surface = self.animation_controller.next_frame()
        monster_rect = monster_surface.get_rect(center = (100, (int(window.get_size()[1]/2))-self.height))
        window.blit(monster_surface, monster_rect)
        # surface = SurfacesCache()
        # monster_surface = surface.get_surface('./MonsterGame/assets/default_monster.png')
        # monster_rect = monster_surface.get_rect(center = (100, (window.get_size()[1]/2)-self.height ))
        # window.blit(monster_surface, monster_rect)
        










class SurfacesCache():

    image_dictionary = {}
    
    def get_surface(self, image_name):
        # if image_name is not found, load and add to dictionary, then return associated surface object(.png)
        if image_name not in self.image_dictionary:
            print(f'image_name:{image_name}')
            image_surface = pygame.image.load(f'./MonsterGame/assets/{image_name}.png')
            self.image_dictionary[image_name] = image_surface
            #f'./assets/{image_name}.png'

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
        self.index += 1
        return self.animation_list[self.index]


    def get_current_surface(self):

        return self.cache.get_surface(self.animation_list[self.index])

        





class AnimationController():
    
    def __init__(self, animation_dictionary):
        self.monster_animation_dictionary = animation_dictionary
        self.current_animation = []

        for animation_name in animation_dictionary:
            animation_list = animation_dictionary[animation_name]
            self.animation_instance = Animation(animation_list)
            self.monster_animation_dictionary[animation_name] = self.animation_instance
        
        

    
    def set_animation(self, animation_name):
        monster_animation_dictionary = self.monster_animation_dictionary

        if animation_name in monster_animation_dictionary:
            self.current_animation =  monster_animation_dictionary[animation_name]  
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


    
    
    if not is_alive:
        monster = Monster(FLOOR_Y_POS, animation_dictionary)
        is_alive = True
        monster.animation_controller.set_animation('Dying')

    monster.draw()
    pygame.display.update()
    clock.tick(fps)