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
        self.frame_rate = 30

    @property
    def frame_rate(self):
        return self.frame_rate

    @frame_rate.setter
    def frame_rate(self, rate):
        if rate <= 0:
            raise ValueError('Not a valid rate')
        return rate


    def display_frame_from_file(self, file):
        pass

    def capture_frame_to_file(self):

        pass
class MovieCamera(Camera):
    pass
