import unittest

import unittest162

class CalTest(unittest.TestCase):
    def setUp(self):
        self.cal = unittest162.Cal()
        print('setUp')
    def tearDown(self):
        print('tearDown')
        del self.cal
    @unittest.skip('skip!')
    def test_aaaa(self):
        c = unittest162.Cal()
        self.assertEqual(c.add_num_and_double(1,1),4)
        self.assertNotEqual(c.add_num_and_double(1,1),5)
        """
        assertはいろいろある
        assertEqual(a.b)
        assertNotEqual(a.b)
        assertFalse(a)
        :
        """
    #例外　withを使うよ
    def test_raise(self):
        c = unittest162.Cal()
        with self.assertRaises(ValueError):
            c.add_num_and_double('1','1')

if __name__ == '__main__':
    unittest.main()