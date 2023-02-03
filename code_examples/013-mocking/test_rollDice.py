from rollDice import rollDiceFunc
from unittest import TestCase
from unittest.mock import Mock, patch

# class diceRollerTests(TestCase):

    # random = Mock()

    # random.randint.return_value = 10

@patch('rollDice.rollDiceFunc')
def test_rollDice(mock_func):

    mock_func.return_value = 10
    result = rollDiceFunc(6)
    
    assertEquals(result, 10)

