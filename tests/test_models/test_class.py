#!/usr/bin/python3
"""
Module for testing multiple classes.
"""

import inspect
import pep8


class TestClassDocumentation():
    """
    Class that allows us to test multiple classes.
    """

    def __init__(self, tests, _class):
        """
        Constructor for TestClassDocumentation.

        Args:
            tests (unittest.TestCase): The test case class.
            _class: The class to be tested.
        """
        self.tests = tests
        self.name = _class

        # Get all the methods of class @name
        self.functions = inspect.getmembers(self.name, inspect.isfunction)

    def documentation(self):
        """
        Test documentation of the module, class, and methods.
        """
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):
                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)

        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)

    def pep8(self, files):
        """
        Test linter pep8 over the files.

        Args:
            files (list): List of file paths to be checked.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')

if __name__ == '__main__':
    unittest.main()
