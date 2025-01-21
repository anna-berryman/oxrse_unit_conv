import unittest
from oxrse_unit_conv.units import cal, j


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(cal.si_unit.matches(j))

    def test_basic_conversion(self):
        self.assertEqual(cal.to_si(1), 4.184)
        self.assertAlmostEqual(cal.to_unit(10, cal), 10, 8)


if __name__ == '__main__':
    unittest.main()
