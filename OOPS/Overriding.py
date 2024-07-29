class A:
    def func(self):
        print("Method of A")


class B:
    def func(self):
        print("Overridden method in class B")


B().func()

A().func()
