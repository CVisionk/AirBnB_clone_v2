#!/usr/bin/python3
"""
test for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def test_do_quit(self):
        """Test if do_quit exits the program"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_do_EOF(self):
        """Test if do_EOF exits the program"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_do_update(self):
        """Test updating instances"""
        base_model = BaseModel()
        base_model.save()

        # Test with valid input
        self.console.onecmd(
            f"update BaseModel {base_model.id} name \"new_name\"")
        self.assertEqual(base_model.name, "new_name")

        # Test with invalid class name
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update WrongClass 123 name \"new_name\"")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

        # Test with missing instance id
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel name \"new_name\"")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

        # Test with non-existent instance id
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 123 name \"new_name\"")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** no instance found **")

        # Test with missing attribute name
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(
                f"update BaseModel {base_model.id} \"new_name\"")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** attribute name missing **")

        # Test with missing attribute value
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(f"update BaseModel {base_model.id} name")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** value missing **")

        # Test with invalid attribute value
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(
                f"update BaseModel {base_model.id} name wrong_value")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test showing instances"""
        self.console.onecmd("show BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test destroying instances"""
        self.console.onecmd("destroy BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test showing all instances"""
        self.console.onecmd("all")
        self.assertTrue(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test counting instances"""
        self.console.onecmd("count BaseModel")
        self.assertIsNotNone(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test updating instances"""
        self.console.onecmd("update BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_with_args(self, mock_stdout):
        """Test creating instances with arguments"""
        self.console.onecmd('create BaseModel name="test" age="25"')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 3)  # depends on instance ID

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_with_id(self, mock_stdout):
        """Test showing instances with ID"""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"show BaseModel {base_model.id}")
        self.assertIn(base_model.__str__(), mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_with_id(self, mock_stdout):
        """Test destroying instances with ID"""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"destroy BaseModel {base_model.id}")
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_with_class(self, mock_stdout):
        """Test showing all instances of a class"""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd("all BaseModel")
        self.assertIn(base_model.__str__(), mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_with_args(self, mock_stdout):
        """Test updating instances with arguments"""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(
            f"update BaseModel {base_model.id} name new_name")
        self.assertEqual(base_model.name, "new_name")


if __name__ == '__main__':
    unittest.main()
