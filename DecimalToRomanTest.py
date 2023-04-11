class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')
    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')
    def test_8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')
    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')
    def test_11(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, 'XI')
    def test_13(self):
        resultado = decimal_to_roman(13)
        self.assertEqual(resultado, 'XIII')
    def test_16(self):
        resultado = decimal_to_roman(16)
        self.assertEqual(resultado, 'XVI')
    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado, 'XXIV')
    def test_35(self):
        resultado = decimal_to_roman(35)
        self.assertEqual
