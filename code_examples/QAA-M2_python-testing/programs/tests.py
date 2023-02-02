from factorial import fact
from sqaures import list_of_squares
from unittest import TestCase

class fact_test(TestCase):

    def test_fact(self):
    # Arrange
        result = 0
        test_num = 5
    # Act
        result = fact(test_num) 
    # Assert
        self.assertEquals(result, 120)

    def test_fact_1(self):
    # Arrange
        result = 0
        test_num = 0
    # Act
        result = fact(test_num) 
    # Assert
        self.assertEquals(result, 1)

class squares_test(TestCase):

    def test_list_of_squares(self):
        # Arrange
        test_num = 5
        result = {}
        expect = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        # Act
        result = list_of_squares(test_num)

        # Assert
        self.assertEquals(result, expect)



# print(fact(5))
# Factorial 5! 1 * 2 * 3 * 4 * 5

 