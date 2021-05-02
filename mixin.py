class A:
    total = 12344


class B:
    pass


class M(A, B):
    def test_print(self):
        print(self.total)


class C(A, M):
    pass


class D(B, M):
    pass


c = C()
c.test_print()
print(c.total)
