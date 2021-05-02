class B:
    def __init__(self):
        self.b = A(self)


class A:
    def __init__(self,bb):
        print('abhishek is in init')

    def __del__(self):
        print('in del')



a = B()