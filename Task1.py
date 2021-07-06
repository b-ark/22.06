# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
class with_index:
    def __init__(self, iterable, start=0):
        self.iterable = self.validate(iterable)
        self.index = 0
        self.start = start

    @staticmethod
    def validate(iterable):
        if not isinstance(iterable, (list, dict, tuple)):
            raise TypeError(f'\'{type(iterable)}\' object is not iterable')
        if isinstance(iterable, dict):
            iterable = tuple(iterable.keys())
        return iterable

    def __iter__(self):
        return self

    def __set__(self, iterable, start=0):
        self.iterable = self.validate(iterable)
        self.index = 0
        self.start = start

    def __next__(self):
        if self.index > len(self.iterable)-1:
            raise StopIteration
        value = (self.start, self.iterable[self.index])
        self.start += 1
        self.index += 1
        return value


def test(iterable, start=0):
    """Функция для сравнения результатов enumerate() и with_index()"""
    print('***\nwith_index()\n***')
    for i in with_index(iterable, start):
        print(i)
    print('***\nenumerate()\n***')
    for i in enumerate(iterable, start):
        print(i)


list_ = ['Barkov', 'Mihail', 'Viktorovich']
dict_ = {'key1': 1, 'key2': 2}
tuple_ = ('Kyiv', 'Mariupol', 'Dnipro')
try:
    test(list_, -10)
    test(dict_, 100)
    test(tuple_)
except StopIteration:
    pass
except TypeError as massage:
    print(massage)
