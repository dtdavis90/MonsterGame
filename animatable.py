import abc

class Animatable(metaclass=abc.ABCMeta):

    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'set_animation') and hasattr(subclass, 'next_frame')
               and hasattr(subclass, 'next_animation') and hasattr(subclass, 'key_control'))


    @abc.abstractmethod
    def set_animation(self):
        raise NotImplementedError


    @abc.abstractmethod
    def next_frame(self):
        raise NotImplementedError


    @abc.abstractmethod
    def next_animation(self):
        raise NotImplementedError


    @abc.abstractmethod
    def key_control(self):
        raise NotImplementedError

