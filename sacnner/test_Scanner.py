import unittest
from Scanner import Scanner

obj = Scanner()


class Test(unittest.TestCase):
    def test_int(self):
        print("enter first number")
        first_number = obj.nextInt()

        print("enter second number")
        second_number = obj.nextInt()

        result = first_number + second_number
        print("addition of two numbers", result)
        self.assertEquals(result, result)

    def test_nextLine(self):
        print("enter your name")
        name = obj.nextLine()
        greeting = "Hello " + name + ""
        print(greeting)
        self.assertEquals(greeting, "Hello favour")

    def test_next(self):
        print("enter  the name of the fruit you like")
        fruit = obj.next()

        print(fruit)
        self.assertEquals(fruit, "apple")

    def test_nextDouble(self):
        print("enter a floating number")
        number = obj.nextDouble()
        print(number, "is a float")
        self.assertEquals(number, 5.00)

    def test_nextBool(self):
        print("enter true or false")
        status = ["Ada is a girl.", "Bob is a boy.", "Carol is a girl."]
        obj = Scanner()
        for expected_value in [True, False, True]:
            value = obj.nextBool()
        print("ada is a girl =",value)
        # if expected_value:
        #     self.assertTrue(value)
        # else:
        #     self.assertFalse(value)
        self.assertEquals(value, expected_value)
