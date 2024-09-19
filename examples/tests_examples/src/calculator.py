from unittest import result

class BasicCalculator():
    def addition(self, first_number:float, second_number:float):
        return first_number + second_number

    def substraction(self, first_number:float, second_number:float):
        return first_number - second_number

    def multiplication(self, first_number:float, second_number:float):
        return first_number * second_number

    def division(self, first_number:float, second_number:float):
        try:
            result = first_number / second_number
        except Exception as e:
            result = False
        return result

    def square_power(self, number:float):
        return number**2