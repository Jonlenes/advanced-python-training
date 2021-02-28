from unittest import TestCase, main

def sum(a, b):

    return a + b

class Test(TestCase):
    def test_sum1(self):
        self.assertEqual(sum(5, 5), 10)
    
    def test_sum2(self):
        self.assertLess(sum(5, 5), 11)

if __name__ == '__main__':
    main()