class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        self.assertEqual(roman_to_decimal('I'), 1)
    def test_II(self):
        self.assertEqual(roman_to_decimal('II'), 2)
    def test_III(self):
        self.assertEqual(roman_to_decimal('III'), 3)
    def test_IV(self):
        self.assertEqual(roman_to_decimal('IV'), 4)
    def test_V(self):
        self.assertEqual(roman_to_decimal('V'), 5)
    def test_VI(self):
        self.assertEqual(roman_to_decimal('VI'), 6)
    def test_VII(self):
        self.assertEqual(roman_to_decimal('VII'), 7)
    def test_VIII(self):
        self.assertEqual(roman_to_decimal('VIII'), 8)
    def test_IX(self):
        self.assertEqual(roman_to_decimal('IX'), 9)
    def test_X(self):
        self.assertEqual(roman_to_decimal('X'), 10)
    def test_XIV(self):
        self.assertEqual(roman_to_decimal('XIV'), 14)
    def test_XIX(self):
        self.assertEqual(roman_to_decimal('XIX'), 19)
    def test_XX(self):
        self.assertEqual(roman_to_decimal('XX'), 20)
    def test_L(self):
        self.assertEqual(roman_to_decimal('L'), 50)
    def test_C(self):
        self.assertEqual(roman_to_decimal('C'), 100)
    def test_D(self):
        self.assertEqual(roman_to_decimal('D'), 500)
    def test_M(self):
        self.assertEqual(roman_to_decimal('M'), 1000)

if __name__ == '__main__':
    unittest.main()
