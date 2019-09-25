import unittest
import camera
import hashlib

class TestMovieCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        '''set up some instances to test'''
        self.cam1 = camera.MovieCamera(frame_rate=30)

    def tearDown(self):
        pass

    def test_capture_frame(self):

        pass

    def test_frame_rate(self):
        self.assertGreater(self.cam1.frame_rate,0)

        with self.assertRaises(ValueError):
            self.cam1.frame_rate = 0
            self.cam1.frame_rate = -3

class TestCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        '''set up some instances to test'''
        self.cam1 = camera.MovieCamera(frame_rate=30)

    def tearDown(self):
        pass

    def test_capture_frame(self):
        with open('test_image.png','r') as f:
            image_at_aperture = self.cam1.display_frame_from_file(f)
            captured_frame = self.cam1.capture_frame(image_at_aperture)
            re_image = self.cam1.display_frame_from_file(captured_frame)

            self.assertEqual(gethash(image_at_aperture),
                             gethash(re_image)
                             )
    def



#redirect to unittest to run its main script
if __name__ == "__main__":
    unittest.main()
