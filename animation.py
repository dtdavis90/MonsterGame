from surfaces_cache import SurfacesCacheSingleton

class Animation:
    
    def __init__(self, image_names_list):

        self.animation_list = []
        self.index = 0
        self.cache = SurfacesCacheSingleton.get_cache_instance()
        

        for image in image_names_list:
            #print(f'type of: {type(image_names_list)}')
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

        