# cairo.Matrix
# cairo.ImageSurface
# cairo.Context
# cairo.LinearGradient
# cairo.FORMAT_ARGB32

# PIL = Python Imaging Library
#
import cairo
class Camera(object):

    def __init__(self, frame_rate=30):
        self.daframe_rate = 30
        self.ctx = None
        self.pixel_height = None
        self.pixel_width = None
        self.aperture_height = None
        self.aperture_width = None

    @property

    def frame_rate(self):
        return self.daframe_rate

    @frame_rate.setter
    def frame_rate(self, rate):
        if rate <= 0:
            raise ValueError('Not a valid rate')
        return rate


    def display_frame_from_file(self, file):
        ''' Opens a file from the
        '''
        pass

    def capture_frame_to_file(self):

        pass

class MovieCamera(Camera):
    pass
