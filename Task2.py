# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step. Tips: See the documentation for `range` function
class in_range:
    def __init__(self, start, end=None, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.one_parameter_logic()
        self.logic_for_start()

    def one_parameter_logic(self):
        if self.end is None:
            self.end = self.start
            self.start = 0

    def logic_for_start(self):
        self.start -= self.step

    def validate_parameters(self):
        if not isinstance(self.start, int):
            raise TypeError('\'start\' must be an integer')
        if not isinstance(self.end, int):
            raise TypeError('\'end\' must be an integer')
        if not isinstance(self.step, int):
            raise TypeError('\'step\' must be an integer')

    def __iter__(self):
        return self

    def __set__(self, start, end=None, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.one_parameter_logic()
        self.logic_for_start()

    def __next__(self):
        self.start = self.start + self.step
        if self.step > 0:
            if self.start > self.end-self.step:
                raise StopIteration
        elif self.step < 0:
            if self.start < self.end-self.step:
                raise StopIteration
        return self.start


try:
    for i in in_range(10):
        print(i)
except TypeError as massage:
    print(massage)
except StopIteration:
    pass
