import unittest
from spotify.link import Link

class TestLink(unittest.TestCase):

    def test_string(self):
        s = "spotify:user:winjer:playlist:4gzM1HrVHQXvCnALez6xhr"
        l = Link.fromString(s)
        self.assertEqual(str(l), s)