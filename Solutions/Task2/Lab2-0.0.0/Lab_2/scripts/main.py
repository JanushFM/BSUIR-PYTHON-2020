from Lab_2.tests import *
import unittest

menu = '\n'.join(
    ["\n", '1) Test Sort', '2) Test JSON', '3) Test Vector', "4) Test Cached", '5) Test Singleton', "or enter 'EXIT',  "])

tests_menu = {
    '1': TestSortMethods,
    '2': TestJsonMethods,
    '3': TestVectorMethods,
    '4': TestDecorator,
    '5': TestSingleton
}

if __name__ == '__main__':
    while True:
        print(menu)
        user_input = input('Enter test number: ')
        if user_input.lower() == 'exit':
            break
        elif user_input in tests_menu:
            test = tests_menu[user_input]
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
            unittest.TextTestRunner().run(suite)
        else:
            print('Inccorect input. Try again !')
