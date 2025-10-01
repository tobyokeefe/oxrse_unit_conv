import unittest
from oxrse_unit_conv.units import cm, m


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(cm.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(cm.to_si(1), 1_000)
        self.assertEqual(cm.to_unit(10, cm), 10)


if __name__ == '__main__':
    unittest.main()