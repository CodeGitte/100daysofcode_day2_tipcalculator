# Import relevant modules
import unittest
from directions_final import solve

# Define a subclass of unittest.TestCase to contain the test methods
class TestSolve(unittest.TestCase):
    """"
    A test class for the solve() function.

    This class defines several unit tests that verify the behavior of the solve() function
    when provided with different input directions. The tests include valid and invalid input,
    and are designed to ensure that the function behaves correctly in all cases.

    Attributes:
    None

    Methods:
    test_solve: A unit test that checks the behavior of the solve() function with different input directions.
    test_solve_exception: A unit test that checks that the solve() function raises a ValueError when provided with invalid input.
    """

    def test_solve(self):
        # Call the solve function with input directions and expected results, using assertEqual() to check if they are the same
        actual = solve(directions=["SÜDEN", "NORDEN", "WESTEN", "OSTEN", "SÜDEN","SÜDEN","SÜDEN"])
        expected = ["SÜDEN","SÜDEN","SÜDEN"]
        self.assertEqual(actual, expected)

        actual = solve(directions=["SÜDEN", "NORDEN", "WESTEN", "OSTEN", "SÜDEN","SÜDEN","SÜDEN", "NORDEN"])
        expected = ["SÜDEN","SÜDEN"]
        self.assertEqual(actual, expected)

        actual = solve(directions=["SÜDEN", "NORDEN", "WESTEN", "OSTEN", "SÜDEN","SÜDEN", "OSTEN", "NORDEN"])
        expected = ["SÜDEN","SÜDEN", "OSTEN", "NORDEN"]
        self.assertEqual(actual, expected)

    # Define a test method to test the exception handling in the solve function
    def test_solve_exeption(self):
        # Check that solve raises a ValueError when given invalid directions
        with self.assertRaises(ValueError):
            solve(["NORDEN", "SÜDEN", "WESTEN", "EASTEN", "UP", "DOWN"])