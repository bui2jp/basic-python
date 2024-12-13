class Cal(object):
    def add_num_and_double(self, x, y):
        """ add and double
        >>> c = Cal()
        >>> c.add_num_and_double(1,2)
        6

        ここにコメントを書いても問題ない。＞＞＞の部分だけ実行される
        ドキュメントのプラスの説明という感じ。本格的なテストではあまり利用されない
        >>> c.add_num_and_double('1','2')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # c = Cal()
    # print(c.add_num_and_double(1,2))
