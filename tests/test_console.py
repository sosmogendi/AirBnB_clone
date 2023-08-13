#!/usr/bin/python3
"""
Test for the console
"""

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    TestConsole class:
    ------------------
    This class defines test cases for the HBNBCommand class in the console module.

    Methods:
        create(self): Creates an instance of the HBNBCommand class.
        test_quit(self): Test for the quit method.
        test_EOF(self): Test for the EOF method.
    """

    def create(self):
        """
        Creates an instance of the HBNBCommand class.

        Returns:
            HBNBCommand: An instance of the HBNBCommand class.
        """
        return HBNBCommand()

    def test_quit(self):
        """
        Test for the quit method.
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """
        Test for the EOF method.
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
