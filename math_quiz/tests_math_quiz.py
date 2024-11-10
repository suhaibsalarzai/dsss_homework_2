import unittest
from math_quiz import generate_random_integer, choose_random_operator, create_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        # Test if the selected operator is one of the expected ones
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random choices
            operator = choose_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):
        # Define test cases as tuples of (num1, num2, operator, expected_problem, expected_answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 4, '+', '10 + 4', 14),
            (10, 4, '-', '10 - 4', 6),
            (10, 4, '*', '10 * 4', 40)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
