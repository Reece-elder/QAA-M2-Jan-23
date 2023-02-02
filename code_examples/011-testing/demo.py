from unittest import TestCase
# Bad design to use *, but rules aren't as important in test files
# The testing file is not production code, not gonna bother linting a test file 
from counter import * 

def multiplyTwo(num):
    return num * 2

def returnTrue():
    return True

# print(multiplyTwo(5))

# demo_test (custom object) is a child of TestCase
class demo_test(TestCase):

    # To run a testsuite we use `python -m unittest <name of file>`
    def test_multiplyTwo(self):
        # Arrange - gathering all variables and resources needed
        test_num = 10
        result = 0

        # Act - doing the thing I am testing
        result = multiplyTwo(test_num) # whatever multiplyTwo() returns, that's now result

        # Assert - Checking if our act did as we expected it to
        self.assertEquals(result, 20) # is result equal to __ 

    def test_returnTrue(self):
        # Arrange
        result = False

        # Act
        result = returnTrue()

        # Assert
        self.assertEquals(result, True)
        # self.assertTrue(result)
        # self.assertFalse(result, "Result is actually True..")

    def test_countingApples(self):
        # Arrange
        list = ["apple", "apple", "test"]
        result = 0

        # Act
        result = countingApples(list)

        # Assert
        self.assertEquals(result, 2)

    def test_countingApplesTwo(self):

        self.assertEquals(countingApples(["apple", "kiwi"]), 1)
