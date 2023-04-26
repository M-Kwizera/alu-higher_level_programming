#!/usr/bin.python3
"""test_rectangle module testing rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testTectangle class..."""

    def test_init_2_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_init_3_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_init_4_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertIsNotNone(r.id)

    def test_init_width_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_init_height_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_init_x_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_init_y_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")
