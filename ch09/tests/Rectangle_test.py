import unittest
import sys
sys.path.append("..")
from Rectangle import Rectangle


class RectangleTest(unittest.TestCase):


    def test_rectangle_is_created(self):
        r =Rectangle()
        self.assertIsInstance(r,Rectangle)

    def test_rectangle_default_init_longueur_largeur(self):
        r =Rectangle()
        self.assertEqual(r.longueur,1)
        self.assertEqual(r.largeur,1)

    def test_rectangle_init_longueur_largeur_0(self):
        self.assertRaises(Exception,Rectangle,0,0)
    
    def test_rectangle_surface(self):
        r =Rectangle(3,4)
        self.assertEqual(r.surface,12)