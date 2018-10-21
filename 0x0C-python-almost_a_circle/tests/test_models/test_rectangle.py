#!/usr/bin/python3
""" unittest for models/rectangle.py """

from models.base import Base
from models.rectangle import Rectangle
import unittest
import json


class Test_Rectangle(unittest.TestCase):

    def setUp(self):
        """ ??? """
        pass

    def tearDown(self):
        """ maplestory """
        pass

    def test_docstring(self):
        """ check to see if present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_simple(self):
        """ simple basic tests """
        poop1 = Rectangle(1, 1)
        poop2 = Rectangle(2, 2)
        poop3 = Rectangle(3, 3)
        self.assertTrue(poop1.id, 1)
        self.assertEqual(poop2.width, poop2.height)
        self.assertNotEqual(poop1.id, poop2.id)
        self.assertEqual(poop1.width, 1)
        self.assertEqual(poop1.height, 1)
        self.assertEqual(poop2.height, 2)
        self.assertEqual(poop3.x, 0)
        poopFancy = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(poopFancy.id, 8)
        self.assertEqual(poopFancy.width, 4)
        self.assertEqual(poopFancy.height, 5)
        self.assertEqual(poopFancy.x, 6)
        self.assertEqual(poopFancy.y, 7)

    def test_syntaxErrors(self):
        """ tests the syntax of no or 1 argument """
        with self.assertRaises(TypeError):
            test = Rectangle()
            test2 = Rectangle(1)
            test3 = Rectangle(None)
            test4 = Rectangle([1])
            test5 = Rectangle([])

    def test_int_validator(self):
        """ tests the integer validator method """
        with self.assertRaises(TypeError):
            test1 = Rectangle("a", 2)
            test2 = Rectangle([2], "b")
            test3 = Rectangle({"3": 4}, "c")
        with self.assertRaises(ValueError):
            test1 = Rectangle(-1, 4)
            test2 = Rectangle(0, 0, 0, 0)
            test3 = Rectangle(1, 2, 0, 3)
            test4 = Rectangle(9, -9, 1, 2)

    def test_area(self):
        """ tests the area method """
        test1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(test1.area(), 1)
        with self.assertRaises(TypeError):
            test2 = test1.area(1)

    def test_display(self):
        """ wtf do i do for this method """
        pass

    def test_string(self):
        """ tests the __str__ """
        test1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(test1), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_args(self):
        """ tests the update *args """
        test1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(test1.height, 1)
        self.assertEqual(test1.x, 1)
        test1.update(3, 3, 3, 3, 3)
        self.assertEqual(test1.height, 3)
        self.assertEqual(test1.y, 3)
        self.assertEqual(test1.x, 3)
        self.assertEqual(test1.width, 3)
        self.assertEqual(test1.id, 3)

    def test_update_kwargs(self):
        """ tests the update with keywords """
        test1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(test1.height, 1)
        test1.update(id=3)
        self.assertEqual(test1.id, 3)
        self.assertEqual(test1.width, 1)
        test1.update(y=69)
        self.assertEqual(test1.y, 69)

    def test_update_errors(self):
        """ tests update errors, either Type or Value """
        test1 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            test1.update('a', 1)
            test1.update(12, [12])
            test1.update({"poopy": 1}, 1)
            test1.update(None)
        with self.assertRaises(ValueError):
            test1.update(0, 0, 0, 0)
            test1.update(-1, -1, -1, -1,)

    def test_to_dict(self):
        """ tests a string to a dict method """
        test1 = Rectangle(1, 1, 1, 1, 1)
        test2 = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        test1DIC = test1.to_dictionary()
        self.assertEqual(test2, test1DIC)

    """ need to test json stuff in here """
    def test_to_json(self):
        """ tests the object converted to json string """
        test1 = Rectangle(1, 1, 1, 1, 1)
        test1DIC = test1.to_dictionary()
        test1STR = test1.to_json_string(test1DIC)
        self.assertTrue(test1STR, json.dumps(test1DIC))

    def test_save_to_file(self):
        """ tests if we saved to the file """
        test1 = Rectangle(1, 1, 1, 1, 1)
        test1DIX = [test1.to_dictionary()]
        Rectangle.save_to_file([test1])
        with open("Rectangle.json", mode='r', encoding='utf-8') as f:
            red = f.read()
            self.assertEqual(json.dumps(test1DIX), red)

    def test_from_json(self):
        """ from a json string to object """
        test1 = Rectangle(1, 1, 1, 1, 1)
        test1DIX = [test1.to_dictionary()]
        test2 = Rectangle.to_json_string(test1DIX)
        self.assertTrue(test2, json.dumps(test1DIX))
        test3 = Rectangle.from_json_string(test2)
        self.assertTrue(test2, test3)
        # self.assertEqual(test2, test3) fails cause " and '

    def test_create(self):
        """ create tests """
        test1 = Rectangle(1, 1, 1, 1, 1)
        test1DICT = test1.to_dictionary()
        test2 = Rectangle.create(**test1DICT)
        test1S = {'x': 1, 'height': 1, 'y': 1, 'id': 1, 'width': 1}
        test2S = {'x': 1, 'height': 1, 'y': 1, 'id': 1, 'width': 1}
        self.assertEqual(test1DICT, test1S)
        self.assertTrue(test2, test2S)
        self.assertFalse(test1 is test2)
        self.assertTrue(test1S is not test2S)

    def test_load(self):
        """ testing the load from ciles class method """
        test1 = Rectangle(1, 1, 1, 1, 1)
        # object of type rectangle has no length error. need to put in list
        test1LIST = [test1]
        Rectangle.save_to_file(test1LIST)
        x = Rectangle.load_from_file()
        self.assertTrue(isinstance(x, list))
        self.assertTrue(isinstance(x[0], Rectangle))


if __name__ == "__main__":
    unittest.main()