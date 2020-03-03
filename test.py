class A():
    def __init__(self):
        self.name = 'A'
        self.__name = 'a'
        pass

    def __len__(self):
        return 5

    def __call__(self, *args, **kwargs):
        return 'call'

    def __str__(self):
        return 'str'

    def call(self):
        return self.__name

    def __int__(self):
        return 7

def main():
    a = A()
    print(a.name)
    print(a.call())
    print(len(a))
    print(a)
    print(a())
    print(str(a))
    print(int(a)+3)
    print(callable(a))

if __name__ == '__main__':
    main()