from Test.test import A


class C:
    def foo(self):
        a = A()


if __name__ == "__main__":
    c = C()
    c.foo()
