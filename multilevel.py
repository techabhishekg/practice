class A:
    def __init__(self):
        print('in class A')

    def test(self):
        print('in class A')


class B:
    def __init__(self):
        print('in class B')

    def bark(self):
        print('in class B')


class C(A, B):
    def __init__(self):
        print('in class C')

    def test(self):
        print('in class C')

c = C()
c.test()
c.bark()
c.test()

print('-------')

# how to call parent level function, need to check



