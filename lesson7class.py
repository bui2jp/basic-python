print('classの利用')

class Person():
    def __init__(self, name):        
        print('コンストラクタ')
        self.name = name
    def __del__(self):
        print('デストラクタ')

    def say_hello(self):
        print(f'hello {self.name}')

def main():
    p = Person('Mike')
    p.say_hello()
    del p
print('end')

# 
if __name__ == '__main__':
    main()

