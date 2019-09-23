class Scene(object):
    '''
    A Scene comprises all the elements of the scene that are
    needed for production of the scene and a method to produce.
    '''
    def __init__(self):
        super().__init__()
        self.cameras = None
        self.background = None
        self.lighting = None
        self.animators = None
        self.time = 0
        self.frame = None
        self.credits = None
        pass

    def produce(self):
        '''
        TBD: Provide a method produce, which produces a file
        containing footage.
        '''
        pass

    def get_cameras(self):
        '''
        Returns the camera objects associated with the scene.
        '''
        pass

    def set_cameras(self,*cameras):
        '''
        Sets the camera objects associated with the scene.
        '''
        pass

    def get_lighting(self):
        '''
        Returns the scene lighting object.
        '''
        pass

    def set_lighting(self,*lights):
        '''
        Sets the scene lighting objects.
        '''
        pass

    def get_animators(self):
        '''
        Gets the animators associated with the scene. Actors are the
        objects that appear during the scene.
        '''
        pass

    def set_animators(self,*actors):
        '''
        Sets the animators associated with the scene. Actors are the
        objects that appear during the scene.
        '''
        pass

    def get_credits(self):
        '''
        Gets the credits associated with the scene.
        '''
        pass

    def set_credits(self,*credits):
        '''
        Sets the credits associated with the scene.

        keyword arguments
        '''
        pass

    def get_time(self):
        '''Gets the time state of the scene.'''
        pass

    def set_time(self,time):
        '''
        Sets the time state of the scene.

        Keyword Arguments:
        time -- current time
        '''
        pass

    def increment_time(self, d_time):
        '''
        Increments time.

        Keyword arguments:
        d_time -- the time increment, assumed positive
        '''

        self.time += abs(d_time))
        return




class EndSceneEarlyException(Exception):
    pass
