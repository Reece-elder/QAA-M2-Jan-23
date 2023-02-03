from unittest import TestCase
from controller import *
from service import Service

class test_controller(TestCase):

    # Making a test_contreoller object
    def test_startApp(self):
        # Arrange
        test_cont1 = Controller()
        expect = "It has been added to DB!"

        # Act 
        result = test_cont1.startApp()

        # Assert
        self.assertEquals(result, expect)

class test_service(TestCase):

    def test_getAllData(self):
        # arrange
        expect = [1, "latte", "grande", False, "John Cena"]
        result = []
        test_service = Service()

        # act
        result = test_service.getAllData()

        # assert
        self.assertEqual(result, expect)