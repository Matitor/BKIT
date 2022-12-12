import unittest
from rk1re import Composition, Orchestra, ComOrc, A1, A2, A3

class test(unittest.TestCase):
    
    def setUp(self):
        self.streets = [
            Orchestra(1, 'Оркестр Мариинского театра'),
            Orchestra(2, 'Российский национальный оркестр'),
            Orchestra(3, 'Bavarian Radio Symphony'),
        
            Orchestra(11, 'Vienna Philharmonic Orchestra'),
            Orchestra(22, 'Czech Philharmonic'),
            Orchestra(33, 'Royal Concertgebouw Orchestra'),
        ]
        self.houses = [
            Composition(1, 'Лунная соната', 4.4, 1),
            Composition(2, 'Симфония Бетховена', 12.2, 2),
            Composition(3, 'Симфония Баха', 3, 3),
            Composition(4, 'Симфония Моцарта', 11, 3),
            Composition(5, 'Симфония Сальери', 5.5, 3),
        ]
        self.houses_streets = [
              ComOrc(1,1),
              ComOrc(2,2),
              ComOrc(3,3),
              ComOrc(3,4),
              ComOrc(3,5),
          
              ComOrc(11,1),
              ComOrc(22,2),
              ComOrc(33,3),
              ComOrc(33,4),
              ComOrc(33,5),
        ]
        

    def test_A1(self):
        expected_result = [
            ('Симфония Баха', 3, 'Bavarian Radio Symphony'),
            ('Симфония Моцарта', 11, 'Bavarian Radio Symphony'), 
            ('Симфония Сальери', 5.5, 'Bavarian Radio Symphony'), 
            ('Лунная соната', 4.4, 'Оркестр Мариинского театра'), 
            ('Симфония Бетховена', 12.2, 'Российский национальный оркестр')
        ]

        result = A1(self.streets, self.houses)
        self.assertEqual(result, expected_result)
    
    def test_A2(self):
        expected_result = [
            ('Bavarian Radio Symphony', 19.5), 
            ('Российский национальный оркестр', 12.2), 
            ('Оркестр Мариинского театра', 4.4)
        ]
        result = A2(self.streets, self.houses)
        self.assertEqual(result, expected_result)

    def test_A3(self):
        expected_result = {'Российский национальный оркестр': ['Симфония Бетховена']}
        result = A3(self.streets, self.houses, 'оркестр')
        self.assertEqual(result, expected_result) 
    
if __name__ == '__main__':
    unittest.main()