print('pytestの利用')
# pip install pytest

import unittest162
import pytest

# 関数でテストを作成
def test_aaa():
    print('aaa')
    cal = unittest162.Cal()
    assert( cal.add_num_and_double(1,1) == 4 )
    # assert( cal.add_num_and_double(1,1) == 5 )

# クラスでテストを作成
class TestCal():

    def setup_method(self, method):
        print(f'setup_method = {method.__name__}')
        self.cal = unittest162.Cal()

    def teardown_method(self,method):
        print(f'teardown_method = {method.__name__}')        
        del self.cal


    def test_bbb(self):
        print('bbb')
        cal = unittest162.Cal()
        assert( cal.add_num_and_double(1,1) == 4 )

    #例外　withを使うよ
    def test_raise(self):
        c = unittest162.Cal()
        with pytest.raises(ValueError):
            c.add_num_and_double('1','1')        

#     @unittest.skip('skip!')
#     def test_aaaa(self):
#         c = unittest162.Cal()
#         self.assertEqual(c.add_num_and_double(1,1),4)
#         self.assertNotEqual(c.add_num_and_double(1,1),5)
#         """
#         assertはいろいろある
#         assertEqual(a.b)
#         assertNotEqual(a.b)
#         assertFalse(a)
#         :
#         """


# if __name__ == '__main__':
#     unittest.main()
