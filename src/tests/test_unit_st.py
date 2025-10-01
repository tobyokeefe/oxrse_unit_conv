import unittest
from oxrse_unit_conv.units import st, kg


class TestStone(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(st.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(st.to_si(1), 6.35)
        self.assertAlmostEqual(st.to_unit(10, st), 10, 8)


if __name__ == '__main__':
    unittest.main()
