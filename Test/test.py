class A():
    def __init__(self):
        b = B()
        print(b.a)


class B():
    a = "String"




if __name__ == "__main__":
    a = A()
