import unittest
from oxrse_unit_conv.units import mm, m


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(mm.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(mm.to_si(1), 1_000)
        self.assertEqual(mm.to_unit(10, mm), 10)


if __name__ == '__main__':
    unittest.main()