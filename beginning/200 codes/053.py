class MyClass:
    def __del__(self):
        print('MyClass object is removed from Memory.')

obj = MyClass()
del obj
