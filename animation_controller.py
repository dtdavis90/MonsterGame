from animatable import Animatable
from animation import Animation
import pygame

class AnimationController(Animatable):


    
    def __init__(self, animation_dictionary):
        self.monster_animation_dictionary = dict()
        self.current_animation_list = []
        self.current_animation_name = ""
        self.key_list = []
        print(f'id:{id(self)}')


        for animation_name in animation_dictionary:
            self.animation_list = animation_dictionary[animation_name]
            #print(f'check type:{type(self.monster_animation_dictionary[animation_name])}')
            #value of dictionary is being set to Animation object. may rethink this
            animation_instance = Animation(self.animation_list)
            self.monster_animation_dictionary[animation_name] = animation_instance

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
        print(self.current_animation_name)

    def key_control(self, event):
        if event.key == pygame.K_w:
            self.next_animation()
    
    