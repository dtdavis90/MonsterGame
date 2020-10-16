import pygame

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
            image_surface = pygame.image.load(f'../MonsterGame/assets/{image_name}.png')
            self.image_dictionary[image_name] = image_surface
            #f'./assets/{image_name}.png'

        return self.image_dictionary[image_name]
