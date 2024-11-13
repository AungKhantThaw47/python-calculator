import unittest
import signal
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # Set the timeout signal
    def setUp(self):
        self.calc = Calculator()
        signal.signal(signal.SIGALRM, self.timeout_handler)

    # Define a timeout handler
    def timeout_handler(self, signum, frame):
        raise TimeoutError("Function execution exceeded the time limit.")

    # Method to run with timeout
    def run_with_timeout(self, func, *args, **kwargs):
        # Start the timer for 3 seconds
        signal.alarm(3)
        try:
            # Call the function with provided arguments
            result = func(*args, **kwargs)
        except TimeoutError:
            result = "Timeout reached, function terminated."
        finally:
            # Disable the alarm
            signal.alarm(0)
        return result

    def test_add(self):
        self.assertEqual(self.run_with_timeout(self.calc.add, 1, 2), 3)
        
    def test_add_negative(self):
        self.assertEqual(self.run_with_timeout(self.calc.add, -1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(self.run_with_timeout(self.calc.subtract, 4, 2), 2)
        
    def test_subtract_negative(self):
        self.assertEqual(self.run_with_timeout(self.calc.subtract, -1, -1), 0)
        
    def test_multiply(self):
        self.assertEqual(self.run_with_timeout(self.calc.multiply, 2, 3), 6)
        
    def test_multiply_negative(self):
        self.assertEqual(self.run_with_timeout(self.calc.multiply, -2, 3), -6)
        
    def test_divide(self):
        self.assertEqual(self.run_with_timeout(self.calc.divide, 10, 2), 5)
        
    def test_divide_negative(self):
        self.assertEqual(self.run_with_timeout(self.calc.divide, -10, 2), -5)
        
    def test_modulo(self):
        self.assertEqual(self.run_with_timeout(self.calc.modulo, 10, 3), 1)
        
    def test_modulo_negative(self):
        self.assertEqual(self.run_with_timeout(self.calc.modulo, -10, 3), 2)

if __name__ == '__main__':
    unittest.main()
