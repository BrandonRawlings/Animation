import unittest
import camera
import hashlib

class TestCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        '''set up some instances to test'''
        self.cam1 = camera.Camera(frame_rate=30)

    def tearDown(self):
        pass


    def test_frame_rate(self):
        self.assertGreater(self.cam1.frame_rate,0)

        with self.assertRaises(ValueError):
            self.cam1.frame_rate = 0
            self.cam1.frame_rate = -3

    def test_capture_frame(self):
        with open('media/test/tulips.png','r') as f:
            image_at_aperture = self.cam1.display_frame_from_file(f)
            capt_frame = self.cam1.capture_frame_to_file()
            re_image = self.cam1.display_frame_from_file(capt_frame)
            def gethash(x): hashlib.md5(x).hexdigest()
            self.assertEqual(gethash(image_at_aperture),
                             gethash(re_image))

#redirect to unittest to run its main script
if __name__ == "__main__":
    unittest.main()
