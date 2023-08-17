import username_check
import unittest


class TestUsernameCheck(unittest.TestCase):

    def test_for_generic(self):
        '''Name adn Surname souldn't be not generic ascqwczX'''
        pass

    def test_for_capitals(self):
        '''Name and Surname should both start from capitals'''
        pass

    def test_for_surname_input(self):
        '''user sould add Surmane and don't leave field empty'''
        self.assertNotEqual(str())  # variable should me None ar space
        pass

    def test_withdatabase_match(self):
        '''first user enters make to db(variable) then we compate it with user login action'''
        pass

    def test_for_symblols(self):
        '''Should be symbols like $#2!3123'''
        pass

    def test_for_numbers(self):
        '''Shouldn't be an any numbers in name or surname'''
        pass
